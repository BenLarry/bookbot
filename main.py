def main():
    path = "./books/frankenstein.txt"
    text = open_book(path)
    report(count_word(text), dict_to_sorted_list(count_letters(text)), path)
        
def count_word(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for char in text.lower():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1  
    return letters

def sort_on(dict):
    return dict["num"]

def report(word_amount, character_amount, book):
    print(f"--- Begin report of {book} ---")
    print(f"{word_amount} words found in the document \n")
    for character in character_amount:
        print(f'The {character["char"]} character was found {character["num"]} times')
    

def dict_to_sorted_list(dict):
    sorted_list = []
    for char in dict:
        if char.isalpha():
            sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def open_book(path):
    with open(path) as f:
        return f.read()



main()
