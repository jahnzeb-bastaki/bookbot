def word_count(text):
  words = text.split()
  return len(words)

def char_count(text):
  char = {}
  for c in text:
    c = c.lower()
    if c in char:
      char[c] += 1
    else:
      char[c] = 1
  return char

def sort_on(items):
  return items["num"]

def sorted_dictionaries(character_dict):
  sorted_list = []
  for key in character_dict:
    sorted_list.append({"char": key, "num": character_dict[key]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list
  