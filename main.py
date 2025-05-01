def get_book_text(filepath):
    text = ""
    
    with open(filepath) as f:
        text = f.read()
        
    return text

def main():
    path = "./books/frankenstein.txt"
    print(get_book_text(path))
    
main()