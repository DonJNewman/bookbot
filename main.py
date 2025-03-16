from stats import text_split, char_counter, sort_list, print_report
import sys
def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
    return file_contents

def main():
    print(len(sys.argv))
    if len(sys.argv) == 1:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        gotten_book = get_book_text(sys.argv[1])
        counted_characters = char_counter(gotten_book)
        split_text = text_split(gotten_book)
        sorted_list = sort_list(counted_characters)
        print_report(sorted_list, split_text)
main()
