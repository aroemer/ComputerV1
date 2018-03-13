#!/usr/bin/python

class ArgPolynomClass:
	def __init__(self, sign, value, power):
		self.sign = sign
		self.power = power
		self.value = value

class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

def abs_value(arg):
	if arg.value < 0:
		arg.value = abs(arg.value)
		arg.sign = -1
	if arg.value and arg.value.is_integer():
		arg.value = int(arg.value)

def print_reduced(power_zero, power_one, power_two):
	final = 'Reduced form: '
	sign = ''

	if power_zero.value != 0:
		if power_zero.sign == 1:
			sign = ''
		else:
			sign = '- '
		final += "{}{} * X^0 ".format(sign, power_zero.value)

	if power_one.value != 0:
		if power_one.sign == 1:
			if power_zero.value:
				sign = str('+ ')
		else:
			sign = str('- ')
		final += "{}{} * X^1 ".format(sign, power_one.value)

	if power_two.value != 0:
		if power_two.sign == 1:
			if power_zero.value or power_one.value:
				sign = str('+ ')
		else:
			sign = str('- ')
		final += "{}{} * X^2 ".format(sign, power_two.value)

	final += '= 0'
	print final
