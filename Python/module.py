# the steps (1-12) in section 1.3.1.2 (Modules and Packages)


#Your first module: step 3
print("I like to be a module.")

# first module: step 5
print("I like to be a module.")
print(__name__)

#Your first module: step 6
if __name__ == "__main__": # tests to check if the functions work properly.
    print("I prefer to be a module.")
else:
    print("I like to be a module.")

#Your first module: step 7 -  know how many times the functions have been invoked, you need a counter initialized to zero when the module is being imported.

counter = 0

if __name__ == "__main__": # _ (one underscore) or __ (two underscores), but remember, it's only a convention. that they may read it, but that they should not modify it
    print("I prefer to be a module.")
else:
    print("I like to be a module.")


#Your first module: step 9

#a string (maybe a multiline) placed before any module instructions (including imports) is called the doc-string,
#the functions defined inside the module (suml() and prodl()) are available for import;

#!/usr/bin/env python3

""" module.py - an example of a Python module """

__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)

# Your first module: step 11

import sys

for p in sys.path:
    print(p)






