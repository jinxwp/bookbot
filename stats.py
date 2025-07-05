def number_of_words(text_from_book):
    return len(text_from_book.split())

def number_of_characters(text_from_book):
    characters = {}
    contents = text_from_book.lower()
    for i in contents:
        if i not in characters:
            characters[i] = 1 
        else:
            characters[i] += 1
    return characters

def sorted_dictionary(characters):
    charnum = []
    for char in characters:
        num = characters[char]
        charnum.append({"char": char,"num": num})
    charnum.sort(reverse=True, key=lambda n: n["num"])
    return charnum
