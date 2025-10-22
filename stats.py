def get_num_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    char_count = {}
    for char in text:
        lower = char.lower()
        if lower in char_count:
            char_count[lower] += 1
        else:
            char_count[lower] = 1
    return char_count

def sort_dict(dict):
    char_list = []
    for char, num in dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})
    
    def get_num(item):
        return item["num"]
    
    char_list.sort(reverse=True, key=get_num)
    
    return char_list