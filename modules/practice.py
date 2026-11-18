"""
module is a python file containing code,fun.

adv-
code reusability
better organization
avoid repeatation
"""

#Four ways to import module

#1 import whole module
import math
print(math.pi)

#2 import specific function
from math import sqrt
print(sqrt(9))

#3 as alias
import math as s
print(s.floor(8.5))

#4 import everything (not recommended)
from math import *
print(sqrt(9))