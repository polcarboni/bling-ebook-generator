import requests
from bs4 import BeautifulSoup
import os

base_url = "https://www.projekt-gutenberg.org/grimm/khmaerch/"
chapters = 204

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

def generate_chapter_list(chapters_number):
    if chapters_number <= 0 or not isinstance(chapters_number, int):
            raise ValueError("The highest number must be a positive integer.")
    chapters = [f"chap{str(i).zfill(3)}.html" for i in range(1, chapters_number + 1)]
    return chapters

chapters = generate_chapter_list(chapters)
print(chapters)

def scrape_chapter(url):
    # Request the page content
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    page_content = response.text


    starting_string = "in unserem Shop +++"
    ending_string = '<hr size="1" color="#808080">'
    # Find the starting point: the text after "in unserem Shop +++"
    start_index = page_content.find(starting_string)
    if start_index == -1:
        return ""

    # Find the ending point: before the "<hr size=\"1\" color=\"#808080\">"
    end_index = page_content.find(ending_string, start_index)
    if end_index == -1:
        end_index = len(page_content)
    
    # Extract the relevant part of the text
    relevant_text = page_content[start_index + len(starting_string):end_index-len(ending_string)+1]
    
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
    
    # Replace multiple newlines with a single newline and strip leading/trailing whitespace
    clean_text = '\n'.join(line.strip() for line in clean_text.splitlines() if line.strip())
    
    for placeholder, umlaut in encoding_correction.items():
        clean_text = clean_text.replace(placeholder, umlaut)
    clean_text = clean_text.replace("Â", "")

    print(type(clean_text))
    
    return clean_text

subdirectory_name = "kinder-und-hausmärchen"
subdirectory_path = os.path.join("/home/pol/bling_ebook/txt_source_files", subdirectory_name)
# Main script to scrape all chapters and save the extracted text to files
os.makedirs(subdirectory_path, exist_ok=True)

for i, chapter in enumerate(chapters, start=1):
    url = base_url + chapter
    chapter_text = scrape_chapter(url)

    # Define the output filename
    filename = f"chapter_{i:03}.txt"
    filepath = os.path.join(subdirectory_path, filename)
    
    # Write the chapter text to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(chapter_text)
    
    print(f"Chapter {i} saved to {filename}")