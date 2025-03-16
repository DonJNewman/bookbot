def text_split(filestring):
    text_word_count=len(filestring.split())
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

def sort_on(dictionary_list):
    return dictionary_list["count"]

def sort_list(char_dict):

    list_of_dicts=[]
    for key, value in char_dict.items():
        list_of_dicts.append({"char" :key, "count":value})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def print_report(sorted_list, wordcount):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print('----------- Word Count ----------')
    print(f"Found {wordcount} total words")
    print("-------------Character Count----------")
    for item in sorted_list:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}:")
    print("============= END ===============")
    return None