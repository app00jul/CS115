##########################################
# Name: Julian Noeske
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
##########################################

# Import reduce from the functools package
from functools import reduce
#######################################################################################
# Task 1: Use reduce to determine if all elements in a boolean list are true

boolean_list = [False, True, False, False, True]

def all_true():
    final_result = reduce(lambda a, b: a+b, boolean_list)
    print(f'\nFinal result: {final_result}')
    if final_result == len(boolean_list):
        print("The boolean list are true!")
    else:
        print("The boolean list are false!")
    return final_result

all_true()

#######################################################################################
# Task 1.1: Use reduce to determine if AT LEAST one element in a boolean list is true
# Hint: Should be very similar to the above function
def one_true():
    final_result = reduce(lambda a, b: a + b, boolean_list)
    print(f'\nFinal result: {final_result}')
    if final_result > 0:
        print("At least one item of boolean list is true!")
    else:
        print("All the items in boolean list are false!")

one_true()

#######################################################################################
# Task 2: Use map and reduce to return how many elements are True in a boolean list
def count_true():
    final_result = reduce(lambda a, b: a + b, boolean_list)
    print(f'\nThe number of True elements: {final_result}')

count_true()

# This function is provided for you
# Gets a list of strings through the command line
# Input is accepted line-by-line
def getInput():
    lst = []

    inpt = True
    while inpt:
        txt = input("Please enter: ")
        if len(txt) == 0:
            inpt = False
        else:
            lst.append(txt)
            print(lst)
    return lst


# Task 3: Get the longest string in the list using map and reduce, and print it out
# 'strings' is a list of input strings e.g. [ 'hello', 'world' ]
# Hint: The 'map' part of your program should take a string s into a length-2 list [len(s), s].

def getLongestString():
    strings = getInput()

    def find_length(s):
        return [len(s), s]

    list(map(find_length, strings))

    def compare(lst1, lst2):
        if lst1[0] > lst2[0]:
            return lst1
        else:
            return lst2


    print(f"The longest string is {reduce(compare, list(map(find_length, strings)))[1]}")
    # gives you the sub list with the longest string
    return reduce(compare, list(map(find_length, strings)))[1] # access the string by indexing the second element

getLongestString()
