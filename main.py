import sys
from stats import get_num_words, get_char_counts, chars_sorted_by_count

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    with open(book_path) as f:
        text = f.read()

    word_count = get_num_words(book_path)
    print(f"Found {word_count} total words")

    char_counts = get_char_counts(text)
    sorted_chars = chars_sorted_by_count(char_counts)

    print("\nCharacter counts:")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()
