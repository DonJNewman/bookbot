def text_split(filestring):
    text_word_count=len(filestring.split())
    print(f"{text_word_count} words found in the document")
    return text_word_count

def char_counter(filestring):
    for char in filestring:
        print(char)
    return None


#iterate through string
#convert current iterated string to lower case
# update a dictionary w a counter for that char