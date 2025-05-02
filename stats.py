def get_word_count(text):
    split_text = text.split()
    return len(split_text)

def sort_list(dict):
    return dict["num"]


def get_character_count(text):
    character_count = {}
    
    for i in text:
        char = i.lower()
        if char not in character_count:
            # Add key with value 1
            character_count[char] = 1
        else:
            # Add 1 to key
            character_count[char] += 1
            
    list_of_char = []
    for key in character_count:
        list_of_char.append({"char":key, "num":character_count[key]})
    
    list_of_char.sort(reverse=True, key=sort_list)
            
    return list_of_char