from stats import get_num_words
from stats import get_letter_count
from stats import get_report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)       

if sys.argv[1] == None:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
        return book_contents

def main():
    full_contents = get_book_text(path)

    count_str = str(get_num_words(full_contents))

    letter_dictionary = get_letter_count(full_contents)
    sorted_letters = get_report(letter_dictionary)

    print("============ BOOKBOT ============")
    print("Analyzing book found at", path)
    print("----------- Word Count ----------")
    print("Found", count_str, "total words")
    print("--------- Character Count -------")
    for entry in get_report(letter_dictionary):
        if entry["char"].isalpha() == True:
            print(entry["char"] + ":", entry["num"])
    print("============= END ===============")

path = sys.argv[1]

main()