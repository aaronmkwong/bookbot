def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    book_words = book_text.split()
    return len(book_words)

def count_characters(book_text):
    text_lower = book_text.lower()
    set_characters = sorted(list(set(text_lower)))
    set_characters.pop(0)
    dict_characters = {}
    for char in set_characters:
        dict_characters[char] = text_lower.count(char)
    return dict_characters



