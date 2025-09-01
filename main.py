import sys
from stats import get_num_words, count_characters, sort_dict

def main():
    # check if a filepath was passed as an argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]  # grab the first argument after the script name
    counting = count_characters(filepath)
    return get_num_words(filepath), sort_dict(counting)

main()
