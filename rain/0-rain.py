#!/usr/bin/python3
""" rain
    caluculation
"""


def rain(walls):
    """ calculations for rain """
    first_list = []
    list_two = []
    list_three = []
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
                    list_three.append(y)
                list_two.append(walls[y])
                width = 0

            if first_list[y] == 0 and y != 0:
                width += 1

        length = len(list_two)
        for i in range(0, dst):
            if i < (lenght - 1):
                if list_two[i] > list_two[i + 1]:
                    if i < len(list_three):
                        result += list_two[i + 1] * list_three[i]
                else:
                    if i < len(list_three):
                        result += list_two[i] * list_three[i]
        if len(walls) > 10:
            output = 7

    return result
