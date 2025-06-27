from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content


def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # path = "books/frankenstein.txt"
    path = sys.argv[1]
    book_text = get_book_text(path)
    char_count = count_characters(book_text)
    sorted_d = sorted_chars(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print(f"--------- Character Count -------")
    for d in sorted_d:
        k,v = list(d.items())[0]
        if k.isalpha():
            print(f"{k}: {v}")

main()