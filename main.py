from stats import get_word_count
from stats import get_character_count
import sys

def get_book_text(filepath):
    text = ""
    
    with open(filepath) as f:
        text = f.read()
        
    return text



def display_char_report(dict):
    for char_pair in dict:
        if char_pair["char"].isalpha():
            print(f"{char_pair["char"]}: {char_pair["num"]}")
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    
    num_words = get_word_count(text)
    char_count = get_character_count(text)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    display_char_report(char_count)
    print("============= END ===============")
    
main()