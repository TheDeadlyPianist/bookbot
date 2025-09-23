from stats import get_word_count
from stats import letter_count
from stats import convert_count_to_list_and_sort
import sys

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        num_words = get_word_count(book_path)
        sorted_letters = convert_count_to_list_and_sort(letter_count(book_path))

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for sorted_letter in sorted_letters:
            letter=sorted_letter["char"]
            num=sorted_letter["num"]
            print(f"{letter}: {num}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

main()