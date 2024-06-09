
import json

def generate_book_json(file_path, title, author, publication_year, genre, description):
    
    book_data = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "description": description
    }

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(book_data, json_file, ensure_ascii=False, indent=4)

    print(f"JSON file created at {file_path}")