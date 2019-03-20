#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = '9aylas'
__bof__ = '19/03/2019 - 00:00'
__eof__ = '20/03/2019 - 23:54'

import os
from googletrans import Translator as t
from PIL import Image as IMG, ImageDraw as IMGD, ImageFont as IMFont


def logo():
	HelloWorld = ' Google TransLate '
	ifont = IMFont.truetype('arial.ttf',13)
	size = ifont.getsize(HelloWorld)
	image = IMG.new('1', size, 1)
	draw = IMGD.Draw(image)
	draw.text((0, 0), HelloWorld, ifont=ifont)
	for rownum in range(size[1]): 
		line = []
		for colnum in range(size[0]):
			if image.getpixel((colnum, rownum)): line.append(' '),
			else: line.append(','),
		print(''.join(line))

def main():
	os.system("cls & color 1a")
	logo()
	print('\n')
	translator = t()
	text = input('# Gimme your Text :\n' + ' _'*33 + '\n [*] ')
	print(" -"*33)
	ds = input('\n# Your Language | Ex: en, es, ru...etc : \n# ')
	target = translator.translate(text, dest=ds)  ## auto detector
	final = target.text
	print('\n* From "' + target.src + '" To --> "' + target.dest+'" ~')
	print(" _"*33)
	print(' [*] '+ final)
	print(" -"*33)
	again = input('\n * Translate again (y/n) ?\n*_ ')
	if again == "Y" or again == "y":
		os.system("cls & color 1a")
		main()
	else:
		print("\nThanks... see u later! ")
		
main()