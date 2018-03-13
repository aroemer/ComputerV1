#!/usr/bin/python

import sys
import re

from args import ArgPolynomClass, Complex, abs_value, print_reduced

equation_parts_tab = str(sys.argv[1]).split('=')

#5 * X^0 + 4 * X^1 - 9.3 * X^24 -> [('', '5', '0'), ('+', '4', '1'), ('-', '9.3', '24')]
parse_left_args = re.findall(r"(\+|\-|=)?\s*(\d+\.?\d*)\s*\*\s*[Xx]\^(\-?\d+\.?\d*)\s*", equation_parts_tab[0])
parse_right_args = re.findall(r"(\+|\-|=)?\s*(\d+\.?\d*)\s*\*\s*[Xx]\^(\-?\d+\.?\d*)\s*", equation_parts_tab[1])

# List of parsed Polynom arguments
left_args = []
right_args = []

# str -> number
# ('', '5', '0') -> 1, 5.0, 0
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
error_power = False
degree = 0
for arg in all_args:
	if arg.power == 0:
		power_zero_args.value += arg.sign * arg.value
	elif arg.power == 1:
		power_one_args.value += arg.sign * arg.value
	elif arg.power == 2:
		power_two_args.value += arg.sign * arg.value
	else:
		error_power = True
	if arg.power > degree:
		degree = int(arg.power)

# Format value and sign 1, -5.0, 0 -> -1, 5, 0
abs_value(power_zero_args)
abs_value(power_one_args)
abs_value(power_two_args)

# Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
# Polynomial degree: 2
# Discriminant is strictly positive, the two solutions are:
# 0.905239
# -0.475131

print_reduced(power_zero_args, power_one_args, power_two_args)

print "Polynomial degree: {}".format(degree)

if error_power:
	sys.exit('The polynomial degree is stricly greater than 2, I can\'t solve.')

if power_one_args.value == 0 and power_two_args.value == 0:
	if power_zero_args.value == 0:
		print 'Any real number can be a solution.'
	else:
		print 'No solution.'
elif power_one_args.value != 0 and power_two_args.value == 0:
	x = - (float(power_zero_args.value * power_zero_args.sign) / (power_one_args.value * power_one_args.sign))
	print 'The solution is:'
	print "{:.6f}".format(x).rstrip('0').rstrip('.')
elif power_two_args.value != 0:
	delta = power_one_args.value ** 2 - 4 * float(power_two_args.value) * power_two_args.sign * power_zero_args.value * power_zero_args.sign

	if delta >= 0:
		x1 = (- power_one_args.value * power_one_args.sign + (delta ** 0.5)) / (2 * power_two_args.value * power_two_args.sign)
		x2 = (- power_one_args.value * power_one_args.sign - (delta ** 0.5)) / (2 * power_two_args.value * power_two_args.sign)
		if delta != 0:
			print 'Discriminant is strictly positive (value = {}), the two solutions are:'.format(delta).rstrip('0').rstrip('.')
			print "{:.6f}".format(x2).rstrip('0').rstrip('.')
		if delta == 0:
			print 'The solution is:'
			print "{:.6f}".format(x1).rstrip('0').rstrip('.')

	else:
		x1 = (- float(power_one_args.value) * power_one_args.sign) / (2 * power_two_args.value * power_two_args.sign)
		x1_delta = (abs(delta) ** 0.5) / (2 * power_two_args.value * power_two_args.sign)
		print "The discriminant is strictly negative, so it has two conjugates complexes solutions"
		print "{} + i * {}".format("{:.6f}".format(x1).rstrip('0').rstrip('.'), "{:.6f}".format(x1_delta)).rstrip('0').rstrip('.')
		print "{} - i * {}".format("{:.6f}".format(x1).rstrip('0').rstrip('.'), "{:.6f}".format(x1_delta)).rstrip('0').rstrip('.')




print '''
---------------------------------
expected result:
Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.905239
-0.475131'''
