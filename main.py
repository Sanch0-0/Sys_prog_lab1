from collections import Counter

def main():
    read()
    split_words()
    count_chars()
    sort_by_usage()
    write_result()

def read(text):
    with open('Марина_Беляева_Лес_тебя_любит.txt', 'r', 'utf-8') as file:
        lines = file.readlines()

    return lines

def split_words(lines):
    splitted_words = split(lines).strip().lower()
    
    return splitted_words

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

