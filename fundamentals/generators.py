#!/usr/bin/env python3


def take(count, iterable):
    """Take items from the front of an iterable.

    Args:
        count: The maximum number of item to retrieve.
        iterable: The source series

    Yeilds:
        At mount 'count' item from the iterable

    """
    counter = 0
    for item in iterable:
        if counter == count:
            return

        counter += 1
        yield item


def distinct(iterable):
    """Returns unique items by eliminating duplicates.

    Args:
        iterable: The source series.

    Yields:
        Unique elements in order from iterable

    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def gen123():
    yield 1
    yield 2
    yield 3


def main():
    print("Take")
    x = take(2, gen123())
    for i in x:
        print(i)

    print("\nDistinct")
    items = [5, 7, 7, 6, 5, 5]
    for i in distinct(items):
        print(i)

    print("\nPipeline")
    items = [3, 6, 6, 2, 1, 1]
    for i in take(3, distinct(items)):
        print(i)

    print("\nGenerator Expression")
    million_squares = (x*x for x in range(1, 1000001))
    for i in (take(10, million_squares)):
        print(i)

    print("\nSum or first million squares")
    print(sum(million_squares))

if __name__ == "__main__":
    main()
