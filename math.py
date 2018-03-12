#!/usr/bin/python

class ArgPolynomClass:
	def __init__(self, sign, value, power):
		self.sign = sign
		self.power = power
		self.value = value

	def print_arg(self):
		str1 = '' if self.sign == 1 else '- '
		if self.value.is_integer():
			str1 += str(int(self.value))
		else:
			str1 += str(self.value)
		str1 += ' * X^' + str(self.power)
		return str1

def printPolynom(C, B, A):
	print(C + B + A)

class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart
