"""
"Kick Butt, Chew Gum"
A Duke Nukem-esque quote generator

version 1.0 (August 17, 2018) by Matthew Petry

inspired by a tweet by @foone

noun list from http://www.desiquintans.com/nounlist
verb list from http://www.enchantedlearning.com/wordlist/verbs.shtml
"""


import os
import random
import sys
import time

print("Kick Butt, Chew Gum Quote Generator activated!")

with open(os.path.dirname(sys.argv[0])+"/verbs.txt", "r") as verbfile:
	verbarray = verbfile.read().splitlines()
	
with open(os.path.dirname(sys.argv[0])+"/nouns.txt", "r") as nounfile:
	nounarray = nounfile.read().splitlines()
	
verblen = len(verbarray) - 1
nounlen = len(nounarray) - 1

def verbnum():
	return random.randrange(0,verblen)

def nounnum():
	return random.randrange(0,nounlen)

while True:
	outtathing = nounarray[nounnum()]
	print("I came to " + verbarray[verbnum()] + " " + nounarray[nounnum()] + " and " + verbarray[verbnum()] + " " + outtathing + ", and I'm all out of " + outtathing + ".")
	time.sleep(1)
	
"""
Copyright 2018 Matthew Petry

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
"""