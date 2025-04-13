import sys
from stats import words_total
from stats import count_characters
from stats import sort_characters_by_count

def get_book_text(file_path):

    with open(file_path) as f:
        file_content = f.read()
        return file_content
    
def print_report(book_path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        char = item['char']
        count = item['count']
        print(f"{char}: {count}")
    
    print("============= END ===============")
    

     
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = words_total(book_text)
    char_dict = count_characters(book_text)
    sorted_chars = sort_characters_by_count(char_dict)
    print_report(book_path, word_count, sorted_chars)

main()