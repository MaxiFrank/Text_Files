# Maxine Liu
# 10/22/2018
# COSC 1
# This file contains partition and quicksort functions

# partition function chooses a pivot point and sort a list into two parts - on the left is the list of numbers
# smaller than the pivot and on the right is the list of numbers larger than pivot.
# The left and right list of numbers will not be sorted to be in decreasing order.

def partition(the_list, p, r):
    i = p - 1
    j = p
    pivot = the_list[r]

    # While loop uses the pivot point set in the above line and sort the list into two lists with indices i and j.
    while j < r:
        if the_list[j] <= pivot:
            i += 1
            temp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = temp
        j += 1

    # why doesn't the tupple below work for my code?
    # the_list[r], the_list[i+1] = the_list[r], the_list[i+1]

    temp = the_list[i + 1]
    the_list[i + 1] = the_list[r]
    the_list[r] = temp

    return i + 1

# quicksort function calls the partition function and recursively sorts the left and right sub-lists.

def quicksort(the_list, p=0, r=None):

    # base case when r is empty, then the index r references to the last number in the list.

    if r == None:
        r = len(the_list) - 1

    # recursive cases where the number indexed by i+1 from the partition function is the pivot.
    # quicksort sorts sub-lists indexed from q to q - 1 and q + 1 to r.
    if p < r:
        q = partition(the_list, p, r)
        quicksort(the_list, p, q - 1)
        quicksort(the_list, q + 1, r)
