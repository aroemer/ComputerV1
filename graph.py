#!/usr/bin/python

# Bonus: Graphical representation

import numpy as np
import matplotlib.pyplot as plt

def print_graph(power_zero_args, power_one_args, power_two_args):
	if power_two_args.value != 0:
		a = power_two_args.value
		b = power_one_args.value
		c = power_zero_args.value
		x = np.linspace(-100 - power_one_args.value , 100 - power_one_args.value, 256, endpoint = True)
		y = (a * (x * x)) + (b * x) + c

		test = 'y = '

		if a != 1:
			test += str(a)
		test += 'x^2'

		if b != 0:
			test += ' + '
			if b != 1:
				test += str(b)
			test += 'x '

		if c != 0:
			test += '+ ' + str(c)
		test = '\n' + r'${}$'.format(test)

		plt.plot(x, y, 'b', label=test)

		axes = plt.gca()
		axes.set_xlim([x.min(), x.max()])
		axes.set_ylim([y.min() - 10, y.max()])

		plt.xlabel('x')
		plt.ylabel('y')
		plt.title('Polynomial Curve')
		plt.legend(loc='upper left')

		plt.show()
