import os
import re

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
    'Ã': 'Ü'
}


def preprocessing(filepath, source_lang):
    
    with open(filepath, 'r') as file:
        text = file.read()
        #print(text[:500])
    text = text.replace('\n', '=+=')

    def replace_periods(text):
        if re.search(r'\d\.', text):
            print("FOUND")
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

    text = text.replace("=+=", "=+=.")

    sentences = re.split(r'([.;])', text)
    sentences = [sentences[i] + sentences[i+1] for i in range(0, len(sentences) - 1, 2)]

    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    # Replace the unique placeholder back with a period
    sentences[0] = sentences[0].replace('##PLACEHOLDER##', '.')
    print(sentences)
    filename = os.path.basename(filepath)
    filepath = f"/home/pol/bling_ebook/txt_original/{source_lang}_{filename}"

    
    #Wtite txt function (same for original and translated version).
    with open(filepath, 'w') as file:
        for sentence in sentences:
#            if not sentence.endswith("."):
#                sentence = sentence + "."
            file.write(sentence + "\n")
    print(f"Source language txt preprocessed and saved!")

    return sentences

    