


def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
        print('hey_')
        print(file_contents)

    return file_contents


def main(): 
    get_book_text("books/frankenstein.txt")

main()