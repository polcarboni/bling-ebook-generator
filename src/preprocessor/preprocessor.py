import os
import re
import glob
from typing import List

umlaut_map = {
    '¨a': 'ä',
    '¨o': 'ö',
    '¨u': 'ü',
    '¨A': 'Ä',
    '¨O': 'Ö',
    '¨U': 'Ü'
}

encoding_correction = {
    'Ã¼': 'ü',
    'Ã': 'ß',
    'Ã¤': 'ä',
    'Ã¶': 'ö',
    'Ã': 'Ä',
    'Ã': 'Ö',
    'Ã': 'Ü',
    '.Â': '.',
    '  ': ' ',
    'Ã´': 'ô'
}


class Preprocessor:

    def __init__(self, lang: str):
        self.lang = lang #Might implement differnt functions for different languages
        self.saving_path = None

    def preprocess_chapter(self, filepath):

        with open(filepath, 'r') as file:
            text = file.read()
        
        def replace_periods(text):
            if re.search(r'\d\.', text):
            # Find the first occurrence of a period preceded by a number and replace it with a unique placeholder
                text = re.sub(r'(\d)\.', r'\1##PLACEHOLDER##', text, count=1)
            return text
        text = replace_periods(text)
        text = text.replace('. ', '. \n')
        text = text.replace("¨ ", "¨")

        for placeholder, umlaut in umlaut_map.items():
            text = text.replace(placeholder, umlaut)

        for placeholder, umlaut in encoding_correction.items():
            text = text.replace(placeholder, umlaut)

        text = text.replace('- ¨', '')
        text = text.replace('¨', '')
        text = text.replace('“ ', '"')
        text = text.replace(".«", "«")
        text = text.replace("Â", "")

        text = text.replace("=+=", "=+=.")

        sentences = re.split(r'([.;])', text)
        sentences = [sentences[i] + sentences[i+1] for i in range(0, len(sentences) - 1, 2)]

        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

        # Replace the unique placeholder back with a period
        sentences[0] = sentences[0].replace('##PLACEHOLDER##', '.')

        return sentences


    def save_chapter(self, sentences: List, filename: str):

        #filename = f"chapter_.txt"
        filepath = os.path.join(self.saving_path, filename)

        with open(filepath, 'w') as file:
            for i in range(len(sentences)):
                file.write(sentences[i] + "\n")
                print("Chapter text preprocessed and saved!")
            

    def generate_saving_directory(self, directory_path):
        
        directory_name = os.path.basename(directory_path)
        print(directory_name)
        subdirectory_path = os.path.join("data/preprocessed", directory_name)
        print("Generated preprocessed data directory: " + subdirectory_path)
        os.makedirs(subdirectory_path, exist_ok=True)
        self.saving_path = subdirectory_path

        return subdirectory_path

    def preprocess_book(self, raw_directory_path):
        
        #Generate new subdirectory for saving preprocessed text 

        for filename in os.listdir(raw_directory_path):
            filepath = os.path.join(raw_directory_path, filename)
            sentences = self.preprocess_chapter(filepath)
            self.save_chapter(sentences, filename)
        
