def get_num_words(path: str) -> int:
    word_count = 0
    try:
        with open(path) as file:
            for line in file:
                word_count += len(line.split())
        return word_count
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return 0

def get_char_counts(text: str) -> dict:
    char_count = {}
    text = text.lower()
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def chars_sorted_by_count(char_count_dict):
    def sort_by_count(item):
        return item["num"]
    
    char_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(key=sort_by_count, reverse=True)
    return char_list
