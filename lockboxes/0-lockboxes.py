#!/usr/bin/python3
"""Module that solves the lockboxes problem."""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened"""

    if len(boxes) == 0:
        return True

    opened = [0]
    keys = list(boxes[0])

    while keys:
        key = keys.pop()

        if key < len(boxes) and key not in opened:
            opened.append(key)
            keys.extend(boxes[key])
    return len(opened) == len(boxes)
