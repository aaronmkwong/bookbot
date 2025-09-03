from stats import get_book_text, count_words, count_characters
import sys 

if len(sys.argv) == 2:
    
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)

    words = count_words(book_text)

    characters = count_characters(book_text)

    print(
    f"""============ BOOKBOT ============ 
    Analyzing book found at {book_path}
    ----------- Word Count ----------
    Found {words} total words
    --------- Character Count -------
    """)

    for key, value in characters.items():
        if key.isalpha():
            print(key + ": " + f"{value}")

else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


