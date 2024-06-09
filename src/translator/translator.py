import os
from typing import List
from deep_translator import GoogleTranslator

class Translator():

    def __init__(self, source_lang: str, target_lang: str, source_directory: str):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.source_directory = source_directory
        self.source_dir_name = os.path.basename(self.source_directory)
        self.saving_location = self.generate_saving_directory() #FIND GOOD NAME


    def generate_saving_directory(self):
        dir_name = os.path.basename(self.source_directory)
        subdir_path = os.path.join("data/translated", dir_name)
        print("Generated translated data directory: " + subdir_path)
        os.makedirs(subdir_path, exist_ok=True)

        return subdir_path
    

    def save_chapter(self, translated_sentences: List, filename: str):
        filepath = os.path.join(self.saving_location, filename)
        with open(filepath, 'w') as file:
            for i in range(len(translated_sentences)):
                file.write(translated_sentences[i] + "\n")
            
            print(f"Translated {filename} saved in {self.saving_location}!")


    def extract_text(self, file_path: str):
        with open(file_path, 'r') as file:
            lines = file.readlines()

            return [line.strip() for line in lines]  


    #2 VERSIONS: directly from list of strings or from txt file
    def translate_book(self):
        translator = GoogleTranslator(source=self.source_lang, target=self.target_lang)
        
        for file_name in os.listdir(self.source_directory):
            sentences = []
            translated_sentences = []
            print(f"Translating {file_name}")
            file_path = os.path.join(self.source_directory, file_name)
            sentences = self.extract_text(file_path)

            for sentence in sentences:
                translated_sentences.append(translator.translate(sentence))

            self.save_chapter(translated_sentences, file_name)
