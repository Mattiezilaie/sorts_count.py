# Author: Mahtab Zilaie
# Date: January 28 2020
# Description: insertion sort and bubble sort that counts the number of comparisons and the number of
# exchanges made while sorting a list and returns a tuple (comparisons first, exchanges
# second).


def bubble_count(a_list):
    """bubble sort called bubble_count that sorts a_list
    counts the number of comparisons and exchanges made"""

    comparisons = 0
    exchanges = 0  # sets comparisons and exchanges
    for index in range(len(a_list)):  # loop through each item in list
        for i in range(len(a_list) - 1):
            comparisons += 1  # adds 1 for every comparision
            if a_list[i] > a_list[i + 1]:  # compares each item
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]  # changes the element
                exchanges += 1
    return comparisons, exchanges


def insertion_count(a_list):
    """an insertion sort called insertion_count that sort through a_list
     counts the comparisions and exchanges between values being sorted """

    comparisons = 0
    exchanges = 0  # sets comparisons and exchanges
    for index in range(len(a_list)):  # loop through list
        j = index
        if not (j>0 and a_list[j]<a_list[j-1]):
            comparisons += 1  # adds 1 for every comparision
        while j > 0 and a_list[j] < a_list[j - 1]:
            a_list[j], a_list[j - 1] = a_list[j - 1], a_list[j]  # swapping
            exchanges += 1
            comparisons += 1
            j -= 1

    return comparisons, exchanges



