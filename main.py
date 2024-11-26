from collections import Counter
import sys
import os

def main():
    if len(sys.argv) < 2: #нужно чтобы пользователь передал 2 аргумента.
        print("Usage: python script.py <filename>")
        sys.exit(1)

    input_file = sys.argv[1]

    text = read(input_file)

    words = split_words(text)

    clean_words = clean_words(words)


def read(file):
    with open(file, 'r', encoding='utf-8') as file:

        return file.read()


def split_words(text):
    split_words = text.split().lower()
    
    return splitted_words


def clean_words(splitted_words):
    cleaned_words = [word.strip(".,!?;:\"'()[]{}-") for word in splitted_words]
    
    return " ".join(cleaned_words)


def count_chars(splitted_words):
    for char in splitted_words:
        cnt = Counter(char)

    return dict(cnt)


def sort_by_usage():
    pass


def write_result():
    pass


if __name__=="__main__":
    main()

