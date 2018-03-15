#!/usr/bin/python

class ArgPolynomClass:
	def __init__(self, sign, value, power):
		self.sign = sign
		self.power = power
		self.value = value

def abs_value(arg):
	if arg.value < 0:
		arg.value = abs(arg.value)
		arg.sign = -1
	if arg.value and arg.value.is_integer():
		arg.value = int(arg.value)

def print_reduced(power_args):
	final = 'Reduced form: '
	sign = ''

	for elem in power_args:
		if power_args.index(elem) == 0:
			if elem.sign == 1:
				sign = ''
			else:
				sign = '- '
			final += "{}{} * X^{} ".format(sign, "{:.6g}".format(elem.value), "{:.6g}".format(elem.power))
		else:
			if elem.sign == 1:
				if elem.value:
					sign = str('+ ')
			else:
				sign = str('- ')
			final += "{}{} * X^{} ".format(sign, "{:.6g}".format(elem.value), "{:.6g}".format(elem.power))

	final += '= 0'
	print final
