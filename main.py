def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
        print('file contents read successfully')
    return file_contents

def main(): 
   
    text_split(
        get_book_text("books/frankenstein.txt")
        )

def text_split(filestring):
    text_word_count=len(filestring.split())
    print(f"{text_word_count} words found in the document")
    return text_word_count


main()



# text split function, takes file_contents and returns number of words
#split method will turn into list, return length of list
# print {num_words} words found in the document