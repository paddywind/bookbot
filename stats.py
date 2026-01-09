def count_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        array_of_words = file_contents.split()
        return len(array_of_words)



def count_characters(file_path):
    character_count_dict = {}
    with open(file_path) as f:
        file_contents = f.read()
        array_of_words = file_contents.split()
        for word in array_of_words:
            for char in word:
                if char.isalpha():
                    char_lower = char.lower()
                    if char_lower in character_count_dict:
                        character_count_dict[char_lower] += 1
                    else:
                        character_count_dict[char_lower] = 1
    return character_count_dict



def sort_on(items):
    return items["num"]

    
def dict_sorter(dict):
    my_array = []
    for word in dict:
        d = {}
        d["char"] = word
        d["num"] = dict[word]
        my_array.append(d)
    my_array.sort(reverse=True, key=sort_on)
    return my_array