#!/usr/bin/python3


"""A python program that determines if all boxes in a two-D list can be opened"""


def canUnlockAll(boxes):
    """Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes."""

    if len(boxes) <= 1:
        return True

    available_keys = []
    temp_collection = []
    needed_keys = []

    for i in range(len(boxes)):
        needed_keys.append(i+1)

    needed_keys.pop()

    for key in boxes[0]:
        if key not in available_keys and key <= (len(boxes) - 1):
            available_keys.append(key)

    i = 0
    count = 0
    curr_key = available_keys[i]

    while count < (len(boxes) - 1):
        for key in boxes[curr_key]:
            if key not in available_keys and key <= (len(boxes) - 1) and key > 0:
                available_keys.append(key)
            if key > (len(boxes) - 1):
                temp_collection.append(key)
        i += 1
        if i <= (len(available_keys) - 1):

            curr_key = available_keys[i]

        count += 1

    contents = [element for sublist in boxes for element in sublist]

    contents = set(contents)
    needed_keys = set(needed_keys)

    collected_contents = set(available_keys)

    if 0 in collected_contents:
        collected_contents.remove(0)

    if collected_contents == needed_keys:
        return True
    return False
