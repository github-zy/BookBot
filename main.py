from stats import count_words, get_character_dict, chars_dict_to_sorted_list
import sys

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()

def print_report(file_path: str, word_count: int, sorted_char_list: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_list:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============ END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_dict = get_character_dict(book_text)
    sorted_char_list = chars_dict_to_sorted_list(char_dict)
    print_report(book_path, word_count, sorted_char_list)