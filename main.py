def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    get_num_chars(text)


def get_num_chars(text):
    lowered_string = text.lower()
    char_count = {}
    for char in lowered_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
