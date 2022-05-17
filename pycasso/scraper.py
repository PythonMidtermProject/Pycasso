import os, json, random
from serpapi import GoogleSearch

def get_google_images(search_input):
    # returns url of random image from input search
    search = search_input
    params = {
        "api_key": os.getenv('API_KEY'),
        "engine": "google",
        "q": f"{search}",
        "tbm": "isch"
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    i = random.randint(1, 100)
    return results['images_results'][i]['original']

