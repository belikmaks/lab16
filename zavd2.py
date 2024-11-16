import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

nltk.download('stopwords')
nltk.download('wordnet')

input_file = "input_text.txt"
output_file = "processed_text.txt"

try:
    with open(input_file, 'r') as file:
        text = file.read()
    print(f"Текст успішно зчитано з файлу: {input_file}")
except FileNotFoundError:
    print(f"Файл {input_file} не знайдено.")
    text = ""
except Exception as e:
    print(f"Помилка при читанні файлу {input_file}: {e}")
    text = ""

if text:
    tokens = text.split()

    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()

    stop_words = set(stopwords.words('english'))
    processed_tokens = []

    for word in tokens:
        word_cleaned = word.translate(str.maketrans('', '', string.punctuation)).lower()
        if word_cleaned and word_cleaned not in stop_words:
            lemma = lemmatizer.lemmatize(word_cleaned)
            stem = stemmer.stem(lemma)
            processed_tokens.append(stem)

    processed_text = ' '.join(processed_tokens)

    try:
        with open(output_file, 'w') as file:
            file.write(processed_text)
        print(f"Оброблений текст успішно записано у файл: {output_file}")
    except Exception as e:
        print(f"Помилка при записі у файл {output_file}: {e}")
