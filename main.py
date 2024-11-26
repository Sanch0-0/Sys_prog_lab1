from collections import Counter
import sys
import re

def main():
    if len(sys.argv) < 2:  # Проверка на наличие аргумента
        print("Usage: python script.py <filename>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Чтение
    text = read(input_file)

    # Разделение на слова
    words = split_words(text)

    # Очистка слов
    cleaned_words = clean_words(words)

    # Подсчет слов
    word_counts = count_words(cleaned_words)

    # Запись результатов
    write_counted_words(word_counts, output_file='result\\text_words.txt')

    # Получение статистики
    stats = get_statistics(cleaned_words, text)

    # Запись статистики
    write_statistics(stats, output_file='result\\text_stats.txt')


def read(file):
    with open(file, 'r', encoding='utf-8') as file:
      
        return file.read()


def split_words(text):

    return text.split()


def clean_words(splitted_words):

    return [word.strip(".,!?;:\"'()[]{}-") for word in splitted_words]


def count_words(cleaned_words):

    return Counter(cleaned_words)


def write_counted_words(word_counts, output_file):

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Подсчет слов:\n")
        for word, quantity in word_counts.most_common():
            file.write(f"{word}: {quantity}\n")


def get_statistics(words, text):

    unique_words = len(set(words))
    word_lengths = Counter(len(word) for word in words)
    punctuation = re.findall(r'[.,!?;:\-…]', text)  # Позволяет найти знаки препинания
    punctuation_count = len(punctuation)

    return {
        "unique_words": unique_words,
        "word_lengths": word_lengths,
        "punctuation_count": punctuation_count,
    }


def write_statistics(stats, output_file):

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"Уникальных слов: {stats['unique_words']}\n")
        file.write("Длина слов из:\n")
        for length, count in sorted(stats['word_lengths'].items()):
            file.write(f"  {length} букв.   Встречается {count} раз.\n")
        file.write(f"Знаков пунктуации: {stats['punctuation_count']}\n")


if __name__ == "__main__":
    main()


