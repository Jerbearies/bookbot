def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    char_count = get_num_chars(text)
    char_count_output(char_count)
    print("--- End report ---")    

def char_count_output(char_count):
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})

    chars_list.sort(reverse=True, key=lambda x: x["count"])

    for item in chars_list:
        print(f"The '{item['char']}' character was found {item['count']} times")




def get_num_chars(text):
    lowered_string = text.lower()
    char_count = {}
    for char in lowered_string:
        if char.isalpha(): # Only count if it's a letter
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
