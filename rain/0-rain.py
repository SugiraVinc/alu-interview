#!/usr/bin/python3
""" rain
    caluculation
"""


def rain(walls):
    """ calculations for rain """
    first_list = []
    sec_list = []
    third_list = []
    base = 0
    result = 0
    if len(walls) > 0:
        for x in walls:
            if x > 0:
                first_list.append("*")
            else:
                first_list.append(x)

        for y in range(0, len(walls)):

            if first_list[y] == "*":
                if base > 0:
                    third_list.append(base)
                sec_list.append(walls[y])
                base = 0

            if first_list[y] == 0 and y != 0:
                base += 1

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
            output = 7

    return result
