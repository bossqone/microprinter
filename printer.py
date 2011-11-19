# -*- coding: utf-8 -*-
import serial

class Printer:
	def __init__(self, port):
		""" vytvorenie spojenia s tlačiarňou """
		self.serial = serial.Serial(port)
		self.serial.write('\x1b\x40')
		self.serial.write('\x1b\x21\x00') #nastaví normálny text

	def write(self, text):
		""" vytlačí text """
		self.serial.write(text)

	def newLine(self):
		""" presunie sa na nový riadok """
		self.serial.write('\x0d') #CR
		self.serial.write('\x0a') #LF

	def writeln(self, text):
		""" vytlačí text a presunie sa na nový riadok """
		self.serial.write(text)
		self.serial.write('\x0d') #CR
		self.serial.write('\x0a') #LF

	def underline(self, on=1):
		""" zapnutie/vypnutie podčiarknutého písma """
		self.serial.write('\x1b\x2d' + chr(on))

	def bold(self, on=1):
		""" zapnutie/vypnutie hrubého písma """
		self.serial.write('\x1b\x45' + chr(on))

	def left(self):
		""" zarovnanie vľavo """
		self.serial.write('\x1b\x61\x00')

	def center(self):
		""" zarovnanie do stredu """
		self.serial.write('\x1b\x61\x01')

	def right(self):
		""" zarovnanie vpravo """
		self.serial.write('\x1b\x61\x02')