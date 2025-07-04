def main():
    path_to_file = "books/frankenstein.txt"
    text_from_book = get_book_text(path_to_file)
    numbers = number_of_words(text_from_book)
    print(f"{numbers} words found in the document")    

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def number_of_words(text_from_book):
    return len(text_from_book.split())

main()





