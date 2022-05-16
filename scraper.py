import os, json 
from serpapi import GoogleSearch

class Scraper:
    def search():
        input("What can I find for you?")
    def get_google_images():
        search()
        params = {
        "api_key": os.getenv('API_KEY'),
        "engine": "google",
        "q": f"{search}",
        "tbm": "isch"
        }
        search = GoogleSearch(params)
        results = search.get_dict()

        for i in range(9):
            print(json.dumps(results['images_results'][i]['original'], indent=2, ensure_ascii=False))

    #get_google_images()
