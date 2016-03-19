import glob
import random
from random_words import RandomWords


def chain(iterable_one, iterable_two):
    for iter1 in iterable_one:
        yield iter1
    for iter2 in iterable_two:
        yield iter2

# print(list(chain(range(0, 4), range(4, 8))))


def compress(iterable, mask):
    for element in zip(iterable, mask):
        if element[1]:
            yield element[0]

# print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))


def cycle(iterable):
    while True:
        for item in iterable:
            yield item


def input_f():
    space = input("Push space and enter")
    return space == " "


def book_reader():
    path = 'Book/*.txt'
    files = glob.glob(path)

    for i in range(0, len(files)):
        name = files[i]
        # print(name)
        with open(name, 'r') as f:
            data = f.read().split("#")
            for el in data:
                if "Chapter" in el and input_f():
                    yield el

r = book_reader()
for el in r:
    print(el)


def book_generator():
    chapters_count = input("Enter chapters count: ")
    print("Enter length range (in words)")
    from_num = input("From: ")
    to = input("To: ")

    for i in range(0, chapters_count):
        words_count = random.randint(from_num, to)
        rw = RandomWords()
        words = rw.random_words(count=words_count)
        print(words)
        for word in words:
            yield word


def main():
    b = book_generator()
    for el in b:
        print(el)

if __name__=='__main__':
    main()