#!/usr/bin/python

import sys
import re

print 'Argument List:', str(sys.argv[1])

equation = str(sys.argv[1])

equation_tab = equation.split(' ')

# print(equation_tab) 


class ArgPolynomClass:
	def __init__(self, sign, value, power):
		self.sign = sign
		self.power = power
		self.value = value

class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart



error_power = False

power_tab = []

equation_parts_tab = equation.split('=')

left_args_tab = re.findall(r"(\+|\-|=)?\s*(\d+\.?\d*)\s*\*\s*[Xx]\^(\-?\d+\.?\d*)\s*", equation_parts_tab[0])
right_args_tab = re.findall(r"(\+|\-|=)?\s*(\d+\.?\d*)\s*\*\s*[Xx]\^(\-?\d+\.?\d*)\s*", equation_parts_tab[1])


left_arg_polynom_tab = []

right_arg_polynom_tab = []

for arg in left_args_tab:
	left_arg_polynom_tab.append(ArgPolynomClass(arg[0], arg[1], arg[2]))

for arg in right_args_tab:
	right_arg_polynom_tab.append(ArgPolynomClass(arg[0], arg[1], arg[2]))

for i in left_arg_polynom_tab:
	print(i.sign, i.value, i.power)

for i in right_arg_polynom_tab:
	print(i.sign, i.value, i.power)

for arg in equation_tab:
	if arg.find('X^') == 0:
		power_tab.append(int(filter(str.isdigit, arg)))
		if int(filter(str.isdigit, arg)) > 2:
			error_power = True

Arg1 = ArgPolynomClass(-1 , 3, 4)

print(power_tab)

print(Arg1.power)

if error_power:
	sys.exit('The polynomial degree is stricly greater than 2, I can\'t solve.')

