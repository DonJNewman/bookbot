def text_split(filestring):
    text_word_count=len(filestring.split())
    print(f"{text_word_count} words found in the document")
    return text_word_count

def char_counter(filestring):
    char_dict={}
    for char in filestring:
        lowercase = char.lower()
        if not lowercase in char_dict:
            char_dict[lowercase] = 1
        else:
             char_dict[lowercase] += 1    
    return char_dict 