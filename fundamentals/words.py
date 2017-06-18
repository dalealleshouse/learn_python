#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>

"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

     Args:
         url: The URL of a UTF-8 text document.

     Returns:
         A list of string containing the words

    """
    with urlopen(url) as story:
        story_word = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_word.append(word)

    return story_word


def print_items(items):
    """Print items one per line.

    Args:
        items: An iterable series of printable items.

    """
    for item in items:
        print(item)


def main(url='http://sixty-north.com/c/t.txt'):
    """Print each word from a text document from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    """
    if(len(sys.argv) > 1):
        url = sys.argv[1]

    print_items(fetch_words(url))


if __name__ == '__main__':
    main()
