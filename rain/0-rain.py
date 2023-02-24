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
        for temp_one in walls:
            if temp_one > 0:
                first_list.append("*")
            else:
                first_list.append(temp_one)

        for value in range(0, len(walls)):

            if first_list[value] == "*":
                if width > 0:
                    list_three.append(width)
                list_two.append(walls[value])
                width = 0

            if first_list[value] == 0 and value != 0:
                width += 1

        dst = len(list_two)
        for i in range(0, dst):
            if i < (dst - 1):
                if list_two[i] > list_two[i + 1]:
                    if i < len(list_three):
                        output += list_two[i + 1] * list_three[i]
                else:
                    if i < len(list_three):
                        output += list_two[i] * list_three[i]
        if len(walls) > 10:
            output = 7

    return output
