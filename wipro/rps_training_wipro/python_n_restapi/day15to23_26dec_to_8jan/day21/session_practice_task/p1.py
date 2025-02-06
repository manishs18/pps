'''
AttributeError: module 'calc_v01' has no attribute 'add'

import calc_v01 as calc

calc.add(10,20) # we need to create an obj of the calc
'''

import calc_v01

calc = calc_v01.calcv01()

print(calc.add(10,20))
