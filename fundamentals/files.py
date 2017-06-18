#!/usr/bin/env python3
import sys

f = open('wasteland.txt', mode='wt', encoding='utf-8')
f.write("What are the roots that clutch, ")
f.write("what branches grow\n")
f.write("Out of this stony rubbish? ")
f.close()

g = open('wasteland.txt', mode='rt', encoding='utf-8')
# print(g.read())
g.seek(0)

print(g.readline())
print(g.readline())
# print(g.readline())

g.seek(0)

l = g.readlines()
print(l)

g.close()

# mode=at - append, text
h = open('wasteland.txt', mode='at', encoding='utf-8')
h.writelines(
    ['Son of man \n',
     'You cannot say, or guess, ',
     'for you know only,\n',
     'A heap of broken images, ',
     'where the sun beats\n'])
h.close()


def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line)
        print(line)

    f.close()

if __name__ == '__main__':
    main(sys.argv[1])
