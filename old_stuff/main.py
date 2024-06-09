from Translator import translate_book
from epub_generator import generate_epub
from preprocessing import preprocessing

rattenfanger = "/home/pol/bling_ebook/txt_source_files/Der Rattenf¨anger von Hameln.txt"

#translate_book("de", "en", rattenfanger)
path_de = "/home/pol/bling_ebook/txt_original/de_Der Rattenf¨anger von Hameln.txt"
path_en = "/home/pol/bling_ebook/txt_translated/en_Der Rattenf¨anger von Hameln.txt"

print(type(path_de), type(path_en))
print("aaaa")

#generate_epub(path_de, path_en, "Rattenfanger", "ratten.epub")

chap = "/home/pol/bling_ebook/txt_source_files/kinder-und-hausmärchen/chapter_005.txt"
translate_book("de", "en", chap)



