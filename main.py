from stats import get_num_words, count_char, sort_dict
import sys

    
def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = (sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    book_text = get_book_text(book_path)
    print("----------- Word Count ----------")
    print(f'Found {get_num_words(book_text)} total words')
    sort_dict(count_char(book_text))
    print("-------- Character Count --------")
    char_count = count_char(book_text)
    sorted_chars = sort_dict(char_count)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()
