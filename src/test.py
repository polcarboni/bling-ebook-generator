from scraper.projektgutenberg_scraper import ProjektGutenbergScraper
from preprocessor.preprocessor import Preprocessor

url = "https://www.projekt-gutenberg.org/grimm/khmaerch/chap001.html"
test_title = "testa22"

scraper = ProjektGutenbergScraper(url, test_title)
preprocessor = Preprocessor("de")

#scraper.scrape_book()
raw_txt_path = "data/raw/testa22"
preprocessor.preprocess_book(raw_txt_path)