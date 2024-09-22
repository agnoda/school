# the steps (1-12) in section 1.3.1.2 (Modules and Packages)
#Follow the steps (1-9) in section 1.3.1.6 (Modules and Packages)

#translates its contents into a somewhat compiled shape.  it's internal Python semi-compiled code, ready to be executed by Python's interpreter
import module

#
#Your first module: step 5
#when a file is imported as a module, its __name__ variable is set to the file's name (excluding .py)

#Your first module: step 8

import module
print(module.counter)

#Your first module: step 10,  searched in order to find a module which has been requested by the import instruction.

from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))


#Your first module: step 12

from sys import path

path.append('..\\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))




#Follow the steps (1-9) in section 1.3.1.6 (Modules and Packages)


