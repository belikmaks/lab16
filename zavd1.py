import matplotlib.pyplot as plt
from nltk.corpus import gutenberg
import string
from collections import Counter

text = " ".join(gutenberg.words('chesterton-brown.txt'))

def count_words(text):
    words = text.split()
    return len(words)

def most_used_words(text):
    text_cleaned = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text_cleaned.split()
    word_counts = Counter(words)

    most_common_words = word_counts.most_common(10)

    x = [word for word, _ in most_common_words]
    y = [count for _, count in most_common_words]

    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті")
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()


print(f"Загальна кількість слів у тексті: {count_words(text)}")
most_used_words(text)
