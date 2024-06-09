import os

from deep_translator import GoogleTranslator
from preprocessing import preprocessing

def translate_book(source_lang, target_lang, filepath):

    
    book_sentences = preprocessing(filepath, source_lang)
    
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    
    translated_book_sentences = []

    for sentence in book_sentences:
        if sentence == "=+=.":
            translated_book_sentences.append("=+=")
        else:
            translated_book_sentences.append(translator.translate(sentence))

    print(translated_book_sentences)
    filename = os.path.basename(filepath)
    filepath = f"/home/pol/bling_ebook/txt_translated/{target_lang}_{filename}"

    with open(filepath, 'w') as file:
        for sentence in translated_book_sentences:
            #if not sentence.endswith("."):
            #sentence = sentence + "."
            file.write(sentence + "\n")
    print(f"Book translated and saved from {source_lang} to {target_lang}!")
