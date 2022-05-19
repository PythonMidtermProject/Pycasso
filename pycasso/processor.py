import io
import os, sys
import requests
import PIL
import pickle
import torch
import cv2
import imutils
import numpy as np
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import torchvision.transforms as T
import torchvision.transforms.functional as TF

from dall_e          import map_pixels, unmap_pixels, load_model
from IPython.display import display, display_markdown
def stack(search):
    alpha = 3.0
    beta = 0
    howMany = input("How many images would you like to combine?")
    if howMany == "1":
      img1 = imutils.url_to_image(google[0])
      img2 = imutils.url_to_image(google[0])
    elif howMany == "2":
      img1 = imutils.url_to_image(google[0])
      img2 = imutils.url_to_image(google[1])
    else: 
      howMany = input("pick one or two please")     

    fin1 = cv2.resize(img1, (512, 512))
    fin2 = cv2.resize(img2, (512, 512))
    both = cv2.add(fin1, fin2)
    new_image = cv2.convertScaleAbs(both, alpha=alpha, beta=beta)
    final = cv2_imshow(both)
    return both
both_img = stack(google)
def preprocess(img):
    img1 = torch.squeeze(T.ToTensor()(img), 0)
    finalTen = torch.unsqueeze((img1), 0)
    srs = map_pixels(finalTen)
    pls = np.squeeze(srs)
    return pls


