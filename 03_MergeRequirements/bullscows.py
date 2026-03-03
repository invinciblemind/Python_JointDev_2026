from random import randint
import sys
import urllib.request

def bullscows(guess: str, word: str) -> (int, int):
    bulls = 0
    guess2, word2 = '', ''
    for i in range(len(guess)):
        if guess[i] == word[i]:
            bulls += 1
        else:
            guess2 += guess[i]
            word2 += word[i]
    cows = len(set(word2)) + len(set(guess2)) - len(set(word2) | set(guess2))
    return bulls, cows


def ask(prompt: str, valid: list[str] = None) -> str:
    print(prompt, end='')
    word = input()
    if valid != None:
        while word not in valid:
            print(prompt, end='')
            word = input()
    return word


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    word = words[randint(0, len(words) - 1)]
    guess = ask("Введите слово: ", words)
    a = 1
    b, c = bullscows(guess, word)
    inform("Быки: {}, Коровы: {}", b, c)
    while guess != word:
        guess = ask("Введите слово: ", words)
        a += 1
        b, c = bullscows(guess, word)
        inform("Быки: {}, Коровы: {}", b, c)
    return a


s = sys.argv[1]
if len(sys.argv) == 3:
    length = int(sys.argv[2])
else:
    length = 5
if '://' in s:
    dct = urllib.request.urlopen(s).read().decode()
else:
    dct = open(s).read()
words = list(filter(lambda s: len(s) == length, dct.split('\n')))
print(gameplay(ask, inform, words))
