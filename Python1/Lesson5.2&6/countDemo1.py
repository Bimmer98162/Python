#统计文件单词频率
import string


def count_words():
    with open("example.txt", "r") as file:
        text = file.read()

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(word_count)

    with open("word_count.txt", "w") as f:
        for word, count in word_count.items():
            f.write(f"{word}: {count}\n")

count_words()