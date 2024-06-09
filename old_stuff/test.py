from scraper_3 import Scraper
url = "https://www.projekt-gutenberg.org/grimm/khmaerch/chap001.html"

scraper = Scraper("title", url, "de")
scraper.count_chapters()