# Multi-Line Print

print('''
This is a basic multi-line Print
================================
Have fun..!
////////////////////////////////
''')

# Handling Global variables

x = 6
def example():
    # X += 5  # This will give error as we are tryin to change x
    # To fix that, tell python that x is global
    global x
    x += 5
    print(x)
example()

# Writing to a file:
# When we write to a file, everything stored before is cleared

text = 'abc'
savefile = open('sample.txt', 'w')
savefile.write(text)
savefile.close()

# Appending to a file
# Adds to earlier file, not erase

appendme = 'New Information'

appendFile = open('example.text', 'a')
appendFile.write('\n') # To start from a new line
appendFile.write(appendme)
appendFile.close()

# Read from a file

readme = open('example.txt', 'r').read() #  While reading, .read at the end
# Right now, every information is just one object

readme = open('example.txt', 'r').readlines()
# Now we get a list with each line as different element


# For mean, standard dev, etc
import statistics

# List and Tuple

x = 5,6,2,5
x = (5,6,2,5)
# The above two are tuples, IMMUTABLE
# It is generated and iterated faster than list
# Using Tuple:
def abc():
    return 5, 6

x, y = abc()


# List Manipulation
x = [5,6,2,5, 6, 3, 5, 6]

x.append(2)
x.insert(2,99) # First argument for where to insert, then value
x.remove(2) # Removes first instance of two
x.remove(x[2])
x[5:8] # give 5,6,7
x[-2] # Second Last element
x.index(5) # Gives index of first instance of 5
x.count(5)
x.sort()

# Try and Exception like If-Else.. It will try code in TRY, if couldn't then go to exception
# This will not crash the program
colors = ['blue', 'red', 'black']
try:
    # Some code
    # Suppose you give input , that input is not in the list
    # SO, it would usually give an error. BUt this will take care of it

    whatColor = input('Which color car do you want?')

    if whatColor in colors:
        print('we have the car in', whatColor, 'colour')
    else:
        print ('not available')

#  Here, Exception means all kinds of exceptions
# If had put NameError, then it would catch only errors in naming
# If ValueError, it will handle value error and so on
# We can have different kinds of error handling for different kinds of errors
except Exception as e:
    print(e)


# Dictionaries
# No inherent order to a dictionary


# Absolute value - Distance from 0
abs(-5) == abs(5)

# Round
round(-5.66)

import math
math.ceil(-5.66)
math.floor(-5.66)

#=================================================
# OS Module-
# Used mainly to work with dictionaries, folders, etc
import os
import time

curDir = os.getcwd()

# Make new folder- MakeDirectory
os.mkdir('newDir')
time.sleep(2)
# WIll execute next command after 2 sec

os.rename('newDir', 'newDir2')
time.sleep(2)

# Removes the dictionary
os.rmdir('newDir2')

#===================================================
# SYS Module - System input and output
import sys

sys.stderr.write('err test\n') # For Error
sys.stderr.flush()
sys.stdout.write('output text\n') # For Output

print(sys.argv) # Argument Variable - A list of all variables
# We can manipulate values coming in Python

print(sys.executable)
# Current interpreter path

sys.builtin_module_names
# Gives list of all the modules available

##############################################
# URLlib Module
# Allows us to access web
import urllib.request

x = urllib.request.urlopen('https://www.google.com')
# Rrturns the source code for the Google


import urllib.parse # To parse from the websites

# When we search baasic on this page:
# https://pythonprogramming.net/search/?q=basic
# This comes on the address bar after the search
url = 'http://pythonprogramming.net'
values = {'s':'basic', 'submit':'search'}

data = urllib.parse.urlencode(values)
# URLEncode encodes the value in official form

data = data.encode('utf-8')
# Turns into bytes

req = urllib.request.Request(url,data)

resp = urllib.request.urlopen(req)
respdata = resp.read()
print(respdata)


# When  we try to perform actions from programs on websites,
# Sometimes they block us, as they dont want bots to access
# They have apis for that purpose

try:
    x = urllib.request.urlopen('https://www.google.con/search?q=test')
    # It is same as searching 'test' on google
    print(x.read())

except Exception as e:
    print(str(e))

# This didn't work


try:
    url = urllib.request.urlopen('https://www.google.con/search?q=test')

    headers = {}
    # headers is sent with every request with information about the browser, sys, etc

    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    # User-Agent is browser information
    # We are no longer announcing ourself as python

    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

except Exception as e:
    print(str(e))



######################################################
# Regular Expressions

# Identifiers....................

#   \d  Any Number
#   \D  Anything but a Number

#   \s  Space
#   \S  Anything but a space

#   \w  Character
#   \W  Anything but a character

#   .   any cahracter, except a new line
#   \b  the whitespace around words
#   \.  a period

# Modifiers................................ Description

#   {1,3} we're expecting 1 - 3 length digit
#   +     Match 1 or more
#   ?     Match 0 or more
#   *     Match 0 or more
#   $     Match the end of a string
#   ^     Match the beginning of a string
#   |     Either or
#   []    range or 'variance' : [A-Z]
#   {x}   expectind 'x' amount


# White Space Characters.....................

#   \n   new line
#   \s   space
#   \t   tab
#   \e   escape
#   \f   form feed
#   \r   return

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar is 102.
'''

ages = re.findall(r'\d{1,3}', exampleString)
# r - Regular Expression
# \d - Number
# {1,3} - Having 1 - 3 digits

names = re.findall(r'[A-Z][a-z]*', exampleString)
# Means any capital letter first, anything in small letters
# * for only one in capital, as many in small, stop if any space, enter comes

ageDict = {}
x = 0

for eachName in names:
    ageDict[eachName] = ages[x]
    x += 1

print(ageDict)

##############################################
# Parsing with re and urllib

import urllib.request
import urllib.parse
import re

url = 'http://pythonprogramming.net'
values = {'s':'basic', 'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respdata = resp.read()

#print(respdata)

paragraphs = re.findall(r'<p>(.*?)</p>', str(respdata))
#  Means find everyting between the <p>
for eachP in paragraphs:
    print(eachP)
