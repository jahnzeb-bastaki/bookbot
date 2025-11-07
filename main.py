from stats import word_count

def get_book_text(filepath):
  with open(filepath) as file:
    return file.read()

def main():
  book = get_book_text("./books/frankenstein.txt")
  num_words = word_count(book)
  print(f"Found {num_words} total words")

main()