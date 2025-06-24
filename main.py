from stats import get_num_words
from stats import get_num_chars
from stats import sort_on
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    sorted_dict = sort_on(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_dict:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
