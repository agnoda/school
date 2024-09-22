# Follow the steps (1-9) in section 1.3.1.6 (Modules and Packages)

#Your first package: step 1

#! /usr/bin/env python3

""" module: alpha """

def funA():
    return "Alpha"

if __name__ == "__main__":
    print("I prefer to be a module.")



#Your first package: step 2 - It looks like a directory structure.

#Your first package: step 4 0- Python expects that there is a file with a very unique name inside the package's folder: __init__.py. -
#The content of the file is executed when any of the package's modules is imported.
