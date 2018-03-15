#!/usr/bin/python

import sys
import re

from args import ArgPolynomClass, abs_value, print_reduced
from graph import print_graph

equation_parts_tab = str(sys.argv[1]).split('=')

# 5 * X^0 + 4 * X^1 - 9.3 * X^24 -> [('', '5', '0'), ('+', '4', '1'), ('-', '9.3', '24')]
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
power_args = []
# Array of all powers from input
power_tmp = []

# Create a ArgPolynomClass for each degree/power and put it in power_args
for arg in all_args:
	if not arg.power in power_tmp:
		power_tmp.append(arg.power)
		power_args.append(ArgPolynomClass(1, 0, arg.power))


# Addition of values with the same degree
degree = 0
for power in power_tmp:
	for arg in all_args:
		if arg.power == power:
			for elem in power_args:
				if elem.power == power:
					elem.value += arg.sign * arg.value
		if arg.power > degree:
			degree = arg.power

# Format value and sign 1, -5.0, 0 -> -1, 5, 0
for elem in power_args:
	abs_value(elem)

print_reduced(power_args)

# Print degree max
print "Polynomial degree: {:.6g}".format(degree)

for power in power_tmp:
	if power != 0 and power != 1 and power != 2:
		sys.exit('The polynomial degree is stricly greater than 2 or strictly less than 0 or a float, I can\'t solve.')

power_zero_args = ArgPolynomClass(1, 0, 0)
power_one_args = ArgPolynomClass(1, 0, 1)
power_two_args = ArgPolynomClass(1, 0, 2)

for arg in power_args:
	if arg.power == 0:
		power_zero_args = arg
	elif arg.power == 1:
		power_one_args = arg
	elif arg.power == 2:
		power_two_args = arg

if power_one_args.value == 0 and power_two_args.value == 0:
	if power_zero_args.value == 0:
		print 'Any real number can be a solution.'
	else:
		print 'No solution.'
elif power_one_args.value != 0 and power_two_args.value == 0:
	x = - (float(power_zero_args.value * power_zero_args.sign) / (power_one_args.value * power_one_args.sign))
	x = {True: int(x), False: x}[x == 0]
	print 'The solution is:'
	print "{:.6g}".format(x)
elif power_two_args.value != 0:
	delta = power_one_args.value ** 2 - 4 * float(power_two_args.value) * power_two_args.sign * power_zero_args.value * power_zero_args.sign

	if delta >= 0:
		x1 = (- power_one_args.value * power_one_args.sign + (delta ** 0.5)) / (2 * power_two_args.value * power_two_args.sign)
		x2 = (- power_one_args.value * power_one_args.sign - (delta ** 0.5)) / (2 * power_two_args.value * power_two_args.sign)
		x1 = {True: int(x1), False: x1}[x1 == 0]
		x2 = {True: int(x2), False: x2}[x2 == 0]
		if delta != 0:
			print 'Discriminant is strictly positive (value = {}), the two solutions are:' + "{:.6g}".format(delta)
			print "{:.6g}".format(x2)
		if delta == 0:
			print 'Discriminant is null.\nThe solution is:'
		print "{:.6g}".format(x1)

	else:
		x1 = (- float(power_one_args.value) * power_one_args.sign) / (2 * power_two_args.value * power_two_args.sign)
		x1 = {True: int(x1), False: x1}[x1 == 0]
		x1_delta = (abs(delta) ** 0.5) / (2 * power_two_args.value * power_two_args.sign)
		print "The discriminant is strictly negative, so it has two conjugates complexes solutions"
		print "{} + i * {}".format("{:.6g}".format(x1), "{:.6g}".format(abs(x1_delta)))
		print "{} - i * {}".format("{:.6g}".format(x1), "{:.6g}".format(abs(x1_delta)))
		sys.exit()

# Bonus: Graphical representation

print_graph(power_zero_args, power_one_args, power_two_args)
