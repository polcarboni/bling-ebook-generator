from abc import ABC, abstractmethod
import requests
import json


#Define the abstract methods needed by the scraper
class ScraperStrategy(ABC):
    @abstractmethod
    def count_chapters(self, url: str, starting_string: str, ending_string: str):
        pass

#Implementation for each site
class ProjektGutenbergStrategy(ScraperStrategy):
    
    def count_chapters(self, url: str, starting_string: str, ending_string: str):
            chapter_number = 1
            num_chapters = 0
            # Extract the base URL
            base_url = self.url.rsplit('/', 1)[0] + '/chap'

            while True:
                chapter_url = f"{base_url}{chapter_number:03d}.html"
                response = requests.get(chapter_url)
                response.raise_for_status()
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


    
#Here I can define the methods shared by all site scrapers
class Scraper:
    def __init__(self, title: str, url: str, lang: str, config_path: str = 'scraper_config.json'):
        self.title = title
        self.url = url
        self.lang = lang
        self.config_path = config_path
        self.starting_string = None
        self.ending_string = None
        self.strategy = None
        self.load_config()

        print(self.ending_string, self.starting_string, self.strategy)

        
    def load_config(self):
        with open(self.config_path, 'r') as f:
            config = json.load(f)

            for site, params in config['sites'].items():
                if site in self.url:
                    self.starting_string = params['starting_string']
                    self.ending_string = params['ending_string']
                    self.strategy = params['strategy']
                    break
            if not self.starting_string or not self.ending_string or not self.strategy:
                raise ValueError(f"No configuration found for URL: {self.url}")

    def count_chapters(self):
        if self.strategy:
            print("OK")
            test = globals()
            print(test)
            strategy_class = globals()[self.strategy]
            strategy_instance = strategy_class()
            strategy_instance.count_chapters(self.url, self.starting_string, self.ending_string)
        else:
            raise ValueError("No strategy found for the given site")