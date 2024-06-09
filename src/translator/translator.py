import os
from typing import List

class Translator():

    def __init__(self, source_lang: str, target_lang: str, source_directory: str):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.source_directory = source_directory
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

    

    #2 VERSIONS: directly from list of strings or from txt file
    def translate_chapter(self):



        #check how to get to this point:
            #from list: just import it from the preprocessor
            #They need to be stored anyway: it runs all of the preprocessing and then this
            #IDEA: just do everything all at once (tricky to mantain and debug)

            #2. load txt and extract lines as the translator does (more easy and modular)

        sentences = []