#!/usr/bin/python

# Bonus: Graphical representation

import numpy as np
import matplotlib.pyplot as plt

def print_graph(power_zero_args, power_one_args, power_two_args):
	if power_two_args.value != 0:
		a = power_two_args.value * power_two_args.sign
		b = power_one_args.value * power_one_args.sign
		c = power_zero_args.value * power_zero_args.sign
		x = np.linspace( -b - 100 , b + 100, 256, endpoint = True)
		y = (a * (x * x)) + (b * x) + c

		eq = 'y='

		if a == -1:
			eq += '-'

		if a != 1 and a != -1:
			eq += str(a)
		eq += 'x^2'

		if b != 0:
			if b == -1:
				eq += '-'
			if b != 1 and b != -1:
				if b > 0:
					eq += '+'
				eq += str(b)
			eq += 'x'

		if c != 0:
			if c > 0:
				eq += '+'
			eq += str(c)


		plt.plot(x, y, '-g', label='\n' + r'${}$'.format(eq))

		axes = plt.gca()
		axes.set_xlim([x.min(), x.max()])
		axes.set_ylim([y.min() - 10, y.max()])

		plt.xlabel('x')
		plt.ylabel('y')
		plt.title('Polynomial Curve')
		plt.legend(loc='upper left')

		plt.show()
	elif power_one_args != 0:
		b = power_one_args.value
		c = power_zero_args.value

		x1 = 0
		x2 = 5
		y1 = b * x1 + c
		y2 = b * x2 + c

		eq = 'y = '

		if b != 0:
			if b != 1:
				eq += str(b)
			eq += 'x '

		if c != 0:
			eq += '+ ' + str(c)

		plt.plot([x1, x2], [y1, y2], '-g', label=r'$' + eq + '$')

		plt.xlabel('x')
		plt.ylabel('y')
		plt.title('Polynomial Curve')
		plt.legend(loc='upper left')

		plt.show()
	elif power_zero_args != 0:
		b = power_one_args.value * power_one_args.sign

		x1 = 0
		x2 = 5
		y1 = b * x1
		y2 = b * x2

		eq = 'y = '

		if b != 0:
			if b != 1:
				eq += str(b)
			eq += 'x'


		plt.plot([x1, x2], [y1, y2], '-g', label=r'$' + eq + '$')

		plt.xlabel('x')
		plt.ylabel('y')
		plt.title('Polynomial Curve')
		plt.legend(loc='upper left')

		plt.show()
