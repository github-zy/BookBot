def count_words(text: str) -> int:
    return len(text.split())

def get_character_dict(text: str) -> dict[str, int]:
    char_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(char: tuple[str, int]) -> int:
    return char[1]

def chars_dict_to_sorted_list(char_dict: dict[str,int]) -> list[tuple[str, int]]:
    char_list = []
    for char in char_dict:
        char_list.append((char, char_dict[char]))
    char_list = sorted(char_list, key=sort_on, reverse=True)
    return char_list