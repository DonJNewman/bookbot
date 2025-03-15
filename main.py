from stats import text_split, char_counter
def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
    return file_contents

def main(): 
    gotten_book = get_book_text("books/frankenstein.txt")
    counted_characters = char_counter(gotten_book)

    text_split(gotten_book)
    print(counted_characters)
main()