def word_count(text):
    words = text.split()
    return len(words)
def character_count(text):
    characters = {" " : 0}
    for c in text:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters
def sort_on(items):
    return items["count"]
def sorted(characters):
    dict_list = []
    for i in characters:
      if i.isalpha():
        char = i
        count = characters[i]
        char_count = {"char": char, "count": count}
        dict_list.append(char_count)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


