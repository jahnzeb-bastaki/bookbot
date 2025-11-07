from stats import word_count, char_count, sorted_dictionaries
import sys

def get_book_text(filepath):
  with open(filepath) as file:
    return file.read()

def main():
  if len(sys.argv) >= 2:
    print("============ BOOKBOT ============")
    path = sys.argv[1]
    print(f"Analyzing book found at {path}...")
    book = get_book_text(f"./{path}")
    print("----------- Word Count ----------")
    num_words = word_count(book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    count = char_count(book)
    sorted_list = sorted_dictionaries(count)
    for entry in sorted_list:
      if entry["char"].isalpha():
        print(f"{entry["char"]}: {entry["num"]}")
  else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()