def main():
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    try:
        text = get_book_text(book_path)
    except Exception as e:
        print(e)
        print("Please provide valid path.")
        return
    num_words = word_count(text)
    characters = character_count(text)
    sorted_characters = sorted(characters)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_characters:
        print(f"{i['char']}: {i['count']}")
    print("============= END ===============")
def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import word_count
from stats import character_count
from stats import sorted


main()
