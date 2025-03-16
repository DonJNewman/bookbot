from stats import text_split, char_counter, sort_list, print_report
def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
    return file_contents

def main(): 
    gotten_book = get_book_text("books/frankenstein.txt")
    counted_characters = char_counter(gotten_book)
    split_text = text_split(gotten_book)
    sorted_list = sort_list(counted_characters)
    print_report(sorted_list, split_text)
main()