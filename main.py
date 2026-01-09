from stats import count_words, count_characters, dict_sorter
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = count_words(sys.argv[1])
    num_chars = count_characters(sys.argv[1])
    char_dict = dict_sorter(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in char_dict:
        print(f"{x['char']}: {x['num']}")
    print("============= END ===============")
    pass

    
main()