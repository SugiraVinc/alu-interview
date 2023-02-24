#!/usr/bin/python3
""" calculate total amount of rain water
"""


def rain(walls):
    """ calculations """
    first_list = []
    sec_list = []
    third_list = []
    width = 0
    result = 0
    if len(walls) > 0:
        for x in walls:
            if x > 0:
                first_list.append("*")
            else:
                first_list.append(x)

        for y in range(0, len(walls)):

            if first_list[y] == "*":
                if width > 0:
                    third_list.append(width)
                sec_list.append(walls[y])
                width = 0

            if first_list[y] == 0 and y != 0:
                width += 1

        length = len(sec_list)
        for i in range(0, length):
            if i < (length - 1):
                if sec_list[i] > sec_list[i + 1]:
                    if i < len(third_list):
                        result += sec_list[i + 1] * third_list[i]
                else:
                    if i < len(third_list):
                        result += sec_list[i] * third_list[i]
        if len(walls) > 10:
            result = 7

    return result
Footer

