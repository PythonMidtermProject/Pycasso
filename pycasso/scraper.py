import os, json, random
from serpapi import GoogleSearch

def get_google_images(search_input):
  # returns url of random image from input search
    search = search_input
  # "api_key": os.getenv('API_KEY'),
    params = {
      "api_key": "6a4bd7e2a839c31c2082c98bf00cbd8d341769a99caf82e75a2bb96d67e54b4c",
      "engine": "google",
      "q": f"{search}",
      "tbm": "isch"
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    i = random.randint(1, 100)
    return results['images_results'][i]['original']


def get_many_images(search_input):
  # returns url of random image from input search
    search = search_input
  # "api_key": os.getenv('API_KEY'),
    params = {
      "api_key": "6a4bd7e2a839c31c2082c98bf00cbd8d341769a99caf82e75a2bb96d67e54b4c",
      "engine": "google",
      "q": f"{search}",
      "tbm": "isch"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    list = []
    for i in range(9):
      num = random.randint(1, 99)
      list.append(results['images_results'][num]['original'])

    return list
