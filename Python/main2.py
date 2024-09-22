# Follow the steps (1-9) in section 1.3.1.6 (Modules and Packages)

#Your first package: step 7

import module

from sys import path
path.append('..\\packages')

from extra.iota import FunI # tirckery, case sensitive
print(FunI())


#Your first package: step 8

from sys import path

path.append('..\\packages')

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())


#Your first package: step 9

from sys import path

path.append('..\\packages\\extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())