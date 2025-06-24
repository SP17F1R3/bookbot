def get_num_words(book_text):
    words = book_text.split()
    total_words = len(words)
    return total_words

def get_num_chars(book_text):
    converted_text = book_text.lower()
    character_count = {}
    for character in converted_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_on(char_dict):
    def sort_helper(list_char_dicts):
        return list_char_dicts["num"]
    list_char_dicts = []
    for char, count in char_dict.items():
        new_dict = {"char": char, "num": count}
        list_char_dicts.append(new_dict)
    list_char_dicts.sort(reverse=True, key=sort_helper)
    return list_char_dicts

