from stats import get_word_count

def get_book_text(filepath):
    text = ""
    
    with open(filepath) as f:
        text = f.read()
        
    return text

def main():
    path = "./books/frankenstein.txt"
    num_words = get_word_count((get_book_text(path)))
    print(f"{num_words} words found in the document")
    
main()