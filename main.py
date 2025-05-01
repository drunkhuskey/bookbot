from stats import get_word_count
from stats import get_character_count

def get_book_text(filepath):
    text = ""
    
    with open(filepath) as f:
        text = f.read()
        
    return text

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    
    num_words = get_word_count(text)
    char_count = get_character_count(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"{num_words} words found in the document")
    print("--------- Character Count -------")
    print(char_count)
    print("============= END ===============")
    
main()