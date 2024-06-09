import requests
from utils import sites

class Scraper:

    def __init__(self, title: str, url: str, lang: str):
        self.title = title
        self.url = url
        self.lang = lang
        self.starting_string = None
        self.ending_string = None

    def count_chapters(self):
        if "projekt-gutenberg" in self.url:
            chapter_number = 1
            # Extract the base URL
            base_url = self.url.rsplit('/', 1)[0] + '/chap'

            while True:
                chapter_url = f"{base_url}{chapter_number:03d}.html"
                response = requests.get(chapter_url)
                response.raise_for_status()  # Raise an error for bad status codes
                page_content = response.text

                start_index = page_content.find(self.starting_string)
                end_index = page_content.find(self.ending_string, start_index)

                # Extract the relevant part of the text
                relevant_text = page_content[start_index + len(self.starting_string):end_index-len(self.ending_string)+1]

                if response.status_code == 404:
                    break

                chapter_number += 1

            num_chapters = chapter_number - 1
            print("Number of chapters:", num_chapters)