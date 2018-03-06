#!/usr/bin/env python3
import sys
import random
from collections import defaultdict

if len(sys.argv) != 2:
    sys.exit("Provide book text file as an argument")

the_book = sys.argv[1]


def get_book_text():
    with open(the_book, "r") as f:
        return f.read()


def make_words(text):
    # include any other translations
    return text.replace("\n", " ").lower().split()


def main():
    text = get_book_text()
    words = make_words(text)

    trigrams = defaultdict(list)

    # create trigrams
    for idx in range(len(words) - 2):
        key = (words[idx], words[idx + 1])
        trigrams[key].append(words[idx + 2])

    # find random word pair to start with
    key = random.choice(list(trigrams))

    new_words = []

    while True:

        if not trigrams.get(key):
            break

        word = random.choice(trigrams[key])

        # remove this line if you would like to re-use words for longer final text
        trigrams[key].remove(word)

        new_words.extend(list(key) + [word])

        key = tuple(new_words[-2:])

    print(" ".join(new_words))



if __name__ == "__main__":
    main()
