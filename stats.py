def get_book_text(file_path: str):
    with open(file_path) as file:
        return file.read()

def get_word_count(file_path: str):
    book_contents = get_book_text(file_path)
    num_words = len(book_contents.split())
    return num_words

def letter_count(file_path: str):
    book_contents = get_book_text(file_path).lower()
    letter_count = {}
    for letter in book_contents:
        if letter in letter_count and letter.isalpha():
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def convert_count_to_list_and_sort(full_count: dict[str, int]):
    letter_list = []
    for letter in full_count:
        letter_list.append({
            "char": letter,
            "num": full_count[letter]
        })
    letter_list.sort(key=lambda x: x["num"], reverse=True)
    return letter_list