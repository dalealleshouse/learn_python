#!/usr/bin/env python3
"""Demonstrate raiding a refrigerator."""

from contextlib import closing


class RefrigeratorRaider:
    """Raid a refrigerator"""

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print("Finding {}...".format(food))
        if food == "deep fried pizza":
            raise RuntimeError("Health Warning!")

        print("Taking {}".format(food))

    def close(self):
        print("Close the fridge door.")


def raid(food):
    # the closing context manager will always close the door
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
