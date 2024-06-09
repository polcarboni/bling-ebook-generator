from bs4 import BeautifulSoup
import requests
import os

class ProjektGutenbergScraper:

    def __init__(self, url: str, book_title: str):
        
        self.url = url
        self.starting_string = "in unserem Shop +++"
        self.ending_string = '<hr size="1" color="#808080">'
        self.base_url = self.url.rsplit('/', 1)[0] + '/chap'
        self.chapters_num = None
        self.book_title = book_title
        self.saving_path = None


    def scrape_chapter(self, chapter_url):
        
        response = requests.get(chapter_url)
        #response.raise_for_status()
        page_content = response.text
        response_flag = True

        if response.status_code == 404:
            response_flag = False
            print("connection error")

        start_index = page_content.find(self.starting_string)
        end_index = page_content.find(self.ending_string, start_index)

        relevant_text = page_content[start_index + len(self.starting_string):end_index-len(self.ending_string)+1]

        # Remove HTML tags to get the clean text
        clean_text = '' 
        in_tag = False  
        for char in relevant_text:  
            if char == '<': 
                in_tag = True   
            elif char == '>':   
                in_tag = False  
            elif not in_tag:    
                clean_text += char  

        clean_text = '\n'.join(line.strip() for line in clean_text.splitlines() if line.strip())

        return clean_text, response_flag
        

    def save_chapter(self, chapter_number: int, text: str):
        
        filename = f"chapter_{chapter_number}.txt"
        saving_path = os.path.join(self.saving_path, filename)
        with open(saving_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Chapter {chapter_number} saved in {saving_path}")


    def scrape_book(self):
        
        subdirectory_name = self.book_title
        self.saving_path = os.path.join("/home/pol/bling_ebook/data/raw", subdirectory_name)
        os.makedirs(self.saving_path, exist_ok=True)

        chapter_number = 1
        chapters_not_end = True

        while chapters_not_end:
            chapter_url = f"{self.base_url}{chapter_number:03d}.html"
            text, chapters_not_end = self.scrape_chapter(chapter_url)
            self.save_chapter(chapter_number, text)

            chapter_number += 1



        