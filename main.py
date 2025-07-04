from stats import number_of_words
from stats import number_of_characters
from stats import sorted_dictionary
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]
    text_from_book = get_book_text(path_to_file)
    numbers = number_of_words(text_from_book)
    characters = number_of_characters(text_from_book)
    sorted_chars = sorted_dictionary(characters)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {numbers} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()





