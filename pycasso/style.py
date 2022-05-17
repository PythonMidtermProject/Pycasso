# my imports
import functools
import os
from matplotlib import gridspec
import matplotlib.pylab as plt
import tensorflow as tf
import tensorflow_hub as hub

# Define image loading and visualization functions

def crop_center(image):
  """ Returns a cropped square image """
  shape = image.shape
  new_shape = min(shape[1], shape[2])
  offset_y = max(shape[1] - shape[2], 0) // 2
  offset_x = max(shape[2] - shape[1], 0) // 2
  image = tf.image.crop_to_bounding_box(image, offset_y, offset_x, new_shape, new_shape)
  return image

@functools.lru_cache(maxsize=None)
def load_image(image_url, image_size=(256, 256), preserve_aspect_ratio=True):
  """ Loads and preprocesses images """
  # Cache image file locally.
  image_path = tf.keras.utils.get_file(os.path.basename(image_url)[-128:], image_url)
  # Load and convert to float32 numpy array, add batch dimension, and normalize to range [0, 1]
  img = tf.io.decode_image(tf.io.read_file(image_path), channels=3, dtype=tf.float32)[tf.newaxis, ...]
  img = crop_center(img)
  img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
  return img

def show_n(images, titles=('',)):
  n = len(images)
  image_sizes = [image.shape[1] for image in images]
  w = (image_sizes[0] * 6) // 320
  plt.figure(figsize=(w * n, w))
  gs = gridspec.GridSpec(1, n, width_ratios=image_sizes)
  for i in range(n):
    plt.subplot(gs[i])
    plt.imshow(images[i][0], aspect='equal')
    plt.axis('off')
    plt.title(titles[i] if len(titles) > i else '')
  plt.show()


def handler(original, style):

  # The content image size can be arbitrary.
  content_img_size = (384, 384)
# The style prediction model was trained with image size 256 and it's the 
# recommended image size for the style image (though, other sizes work as 
# well but will lead to different results).
  style_img_size = (256, 256)

  content_image = load_image(original, content_img_size)
  style_image = load_image(style, style_img_size)
  style_image = tf.nn.avg_pool(style_image, ksize=[3,3], strides=[1,1], padding='SAME')


  # Load TF Hub module -transfer learning

  hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
  hub_module = hub.load(hub_handle)

  # The signature of this hub module for image stylization is:

  outputs = hub_module(content_image, style_image)
  stylized_image = outputs[0]

  # Stylize content image with given style image.
  # This is pretty fast on a GPU (a few milliseconds).

  outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
  stylized_image = outputs[0]

  #return content_image, style_image, stylized_image

  show_n([content_image, style_image, stylized_image], titles=['Original content image', 'Style image', 'Stylized image'])