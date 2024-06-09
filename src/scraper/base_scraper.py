import os

class BaseScraper:
    def __init__(self, url):
        self.url
    
    def scrape(self):
        pass
    
    def save_text(self, text, dir_path, chapter_name):
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, f'{chapter_name}.txt')

        with open(file_path, 'w') as file:
            file.write(text)

        return file_path