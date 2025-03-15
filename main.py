from stats import text_split
def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
        print('file contents read successfully')
    return file_contents

def main(): 
   
    text_split(
        get_book_text("books/frankenstein.txt")
        )
main()