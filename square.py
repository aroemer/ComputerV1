#!/usr/bin/python

import sys
import re

from math import ArgPolynomClass
from math import Complex
from math import printPolynom

print 'Argument List:', str(sys.argv[1])

equation = str(sys.argv[1])

equation_tab = equation.split(' ')

# print(equation_tab) 


error_power = False

power_tab = []

equation_parts_tab = equation.split('=')

#5 * X^0 + 4 * X^1 - 9.3 * X^24 -> [('', '5', '0'), ('+', '4', '1'), ('-', '9.3', '24')]
parse_left_args = re.findall(r"(\+|\-|=)?\s*(\d+\.?\d*)\s*\*\s*[Xx]\^(\-?\d+\.?\d*)\s*", equation_parts_tab[0])
parse_right_args = re.findall(r"(\+|\-|=)?\s*(\d+\.?\d*)\s*\*\s*[Xx]\^(\-?\d+\.?\d*)\s*", equation_parts_tab[1])

# List of parsed Polynom arguments
left_args = []
right_args = []

# str -> number
# ('', '5', '0') -> 1, 5.0, 0.0
for arg in parse_left_args:
	left_args.append(ArgPolynomClass(int(arg[0] + '1'), float(arg[1]), float(arg[2])))

for arg in parse_right_args:
	right_args.append(ArgPolynomClass(-1 * int(arg[0] + '1'), float(arg[1]), float(arg[2])))

all_args = left_args + right_args


# Args of reduced form
power_zero_args = ArgPolynomClass(1, 0, 0)
power_one_args = ArgPolynomClass(1, 0, 1)
power_two_args = ArgPolynomClass(1, 0, 2)

# Addition of values with the same degree
for arg in all_args:
	if arg.power == 0:
		power_zero_args.value += arg.sign * arg.value
	elif arg.power == 1:
		power_one_args.value += arg.sign * arg.value
	elif arg.power == 2:
		power_two_args.value += arg.sign * arg.value

# Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
# Polynomial degree: 2
# Discriminant is strictly positive, the two solutions are:
# 0.905239
# -0.475131
print('Reduced form: ')
if power_zero_args.value != 0:
	power_zero_args.print_arg()
	# print(power_zero_args.value + '* X^0')

if power_one_args.value != 0:
	power_one_args.print_arg()

if power_two_args.value != 0:
	power_two_args.print_arg()

printPolynom(power_zero_args.print_arg(), power_one_args.print_arg(), power_zero_args.print_arg())

print '= 0'


for arg in equation_tab:
	if arg.find('X^') == 0:
		power_tab.append(int(filter(str.isdigit, arg)))
		if int(filter(str.isdigit, arg)) > 2:
			error_power = True


# print(power_tab)


if error_power:
	sys.exit('The polynomial degree is stricly greater than 2, I can\'t solve.')

