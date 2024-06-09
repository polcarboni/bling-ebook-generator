from ebooklib import epub
from bs4 import BeautifulSoup
import os


def extract_lines_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def extract_chapters(path):
    chapters = []
    for filename in filter(lambda p: p.endswith("txt"), os.listdir(path)):
        filepath = os.path.join(path, filename)
        chapter = extract_lines_from_txt(filepath)
        chapters.append(chapter)
    return chapters



def generate_epub(path1, path2, epub_title, output_file):
    
    bling_chapters = {}

    #path1 and path 2 are to directory of chapters: one per txt file.
    chapters_l1 = extract_chapters(path1)
    chapters_l2 = extract_chapters(path2)

    for chapter_num in path1, path2:
        chapter_name = f"chapter_{chapter_num}"

        chapter_l1 = chapters_l1[chapter_num]
        chapter_l2 = chapters_l2[chapter_num]
        
        bling_chapters.update({chapter_name: [chapter_l1, chapter_l2]})

        chapter
    
    # Create an EPUB book
    book = epub.EpubBook()

    # Set metadata
    book.set_identifier('id123456')
    book.set_title(epub_title)
    book.set_language('en')

    #chapters = None 

    for chapter_num, chapter in bling_chapters.items():
        
        
        
        # Create a chapter
        title = "".join(c for c in list[0] if c.isalpha())
        num = "".join(c for c in list[0] if c.isdigit())
        chapter = epub.EpubHtml(title=title, file_name=f'chap_{num}.xhtml', lang='en')

        # Create alternating content
        content = ""
        for i in range(max(len(chapter[0][chapter_num]), len(chapter[1][chapter_num]))):
            if i < len(chapter[0][chapter_num]):
                content += f'<p style="font-size: small; color: black;">{chapter[0][chapter_num] + "\n"}'
            if i < len(chapter[1][chapter_num]):
                content += f'<br><span style="font-size: small; color: grey; font-style: italic;">{list2[i]}</span></p>'
            else:
                content += '</p>'

        # Add content to chapter
        chapter.content = BeautifulSoup(content, 'html.parser').prettify()
        book.add_item(chapter)

        # Define Table Of Contents
        book.toc = (epub.Link(f'chap_{num}.xhtml', f'Chapter {num}', f'chapter{num}'),)

        # Add default NCX and Nav files
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        # Define CSS style
        style = 'BODY { font-family: Times, serif; }'
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
        book.add_item(nav_css)

        # Create the spine
        book.spine = ['nav', chapter]

    # Write to the file
    epub.write_epub(output_file, book, {})
