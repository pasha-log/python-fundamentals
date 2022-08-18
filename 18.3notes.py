# Packing and Unpacking

# Can 'unpack' iterables:
point = [10, 20]
x, y = point 

a = 2 
b = 3 
b, a = (a, b)

names = ['charlie', 'lucy']
name1, name2 = names 
name1 # 'charlie' 
name2 # 'lucy' 

point = (100,58)
x,y = point 
x # 100 
y # 58 

# Can gather rest using * before variable: 
letters = ["a", "b", "c"]
first, *rest = letters 

sorted_scores = [2400, 2350, 2100, 1960]
top_score, *scores = sorted_scores 
top_score # 2400 
scores # [2350, 2100, 1960] 
sorted_scores # [2400, 2350, 2100, 1960] 
 
first_name = 'Xander' 
initial, *rest = first_name 
initial # 'X'
rest # ['a', 'n', 'd', 'e', 'r']

point = (40,50,20)
x,y,z = point 
x # 40 
y # 50 
z # 20 
(x,y,z) = (40,50,20) 

color_pairs = [['red', 'green'], ['purple', 'orange']]
pair1, pair2 = color_pairs 
pair1 # ['red', 'green'] 
pair2 # ['purple', 'orange'] 
((primary1, secondary1), (primary2, secondary2)) = color_pairs 
primary1 # 'red' 
secondary2 # 'orange'

grades = {
    'A': 12, 
    'B': 19, 
    'C': 30
}

for pair in grades.items()
    print(pair) 

# ('A', 12)
# ('B', 19)
# ('C', 30)
 
# Or 
for (k,v) in grades.items()
    print(k,v)

# A 12 
# B 19 
# C 30 

########################################################### 

# Spread 

# Can 'spread' iterables:
fruits = {'apple', 'berry', 'cherry'}
foods = ['kale', 'celery', *fruits] 

nums = [2,4,6,8] 
# JS: [...]
[*nums] # [2,4,6,8]
[-2,0,*nums] # [-2, 0, 2, 4, 6, 8]
 
odds = [1,3,5,7,9]
[*odds, *nums]
[1,3,5,7,9,2,4,6,8] 

['hello']
[*'hello'] # ['h', 'e', 'l', 'l', 'o']
{*'hello'} # {'e', 'h', 'l', 'o'}
{*'hello', 45} # {45, 'e', 'h', 'l', 'o'}

rainfall = {'Jan': 2.5, 'Feb': 4.9}
{*rainfall} # {'Feb', 'Jan'}
{'Dec': 0.5, *rainfall} # SyntaxError 
{'Dec': 0.5, **rainfall} # {'Dec': 0.5, 'Jan': 2.5, 'Feb': 4.9}
{'Dec': 0.5, **rainfall, 'Jan': 4.0} # {'Dec': 0.5, 'Jan': 4.0, 'Feb': 4.9}

print(2,3,4,5,6) # 2 3 4 5 6
nums = [1,2,3,4,5,6,7,8,9]
print(nums) # [1,2,3,4,5,6,7,8,9] 
print(*nums) # 1 2 3 4 5 6 7 8 9
print(*'hello') # h e l l o 

############################################################### 

# Error Handling 

# In general, Python raises errors in places JS returns undefined: 
# - Provide too few/too many arguments to a function 
# - Index a list beyond length of list 
# - Retrieve item from dictionary that doesn't exist 
# - Use missing attribute on an instance 
# - Conversion failures (eg, converting "hello" to an int)
# - Division by zero 
# - and more!

# In general, in Python: explicit is better than implicit 

# Catching Errors 

# try to convert this to a number 
try:
    age = int(data_we_received)
    print("You are", age)
except:
    print("Hey", you, that's not an age!")
# next line is run either way 

def get_days_alive(person):
    days = person['age'] * 365 
    print(f'You have been alive for {days}')

{'name': 'princess kitty', 'age': 10}

get_days_alive({'age': 50})
# You have been alive for 18250 days 
get_days_alive({}) # Error!

# LBYL 

def get_days_alive(person):
    if 'age' in person:
      days = person['age'] * 365 
      print(f'{person['name']}' has been alive for {days} days')

# EAFP 

def get_days_alive(person):
    try:
        days = person['age'] * 365 
        print(f'You have been alive for {days}')
    except:
        print("Missing key: age")

get_days_alive({}) # Missing key: age  

def get_days_alive(person):
    try:
        days = person['age'] * 365 
        print(f'You have been alive for {days}')
    except KeyError as exc:
        print('EXC=>', exc)
        print(f"Missing key: {exc}")
    except TypeError:
        print("Expected person to be a dict")

get_days_alive(1) # Expected person to be a dict 

get_days_alive({'age': 19}) # Missing key: age (at first)

get_days_alive({'age': 19}) 
# EXC => 'name'
# Missing key: age 
get_days_alive({'age': 19}) 
# Missing key: 'name' 
get_days_alive({}) 
# Missing key: 'age'
get_days_alive(23) 
# Expected person to be a dict

#######################################################

# Raising Exceptions 

# In Python, it's common for you to "raise" errors to signal problems:
if color not in {'red', 'greem', 'blue'}:
    raise ValueError('Not a valid color!')

raise ValueError("I dont like that value")
# ValueError: I dont like that value 

# Error Handling Pattern 
# Raise exception when you know it should be an error 
# Handle it at the point you can give good feedback 
def bounded_avg(nums):
    "Return avg of nums (makes sure nums are 1-100)"
    for n in nums: 
        if n < 1 or n > 100: 
            raise ValueError("Outside bounds of 1-100")
    return sum(nums) / len(nums)
def handle_data():
    "Process data from database"
    # ages = get_ages(from_my_db)
    ages = [10,40,50,99,103,2,0]
    try: 
        avg = bounded_avg(ages)
        print("Average was", avg)
    except ValueError as exc:
        # exc is exception object -- you can examine it! 
        print("Invalid age in list of ages")

################################################################

# Docstrings & Doctests

def bounded_avg(nums):
    """returns average of list of nums (nums must be between 1-100)"""

    for n in nums: 
        if n < 1 or n > 100: 
            raise ValueError("Outside bounds of 1-100")

    return sum(nums) / len(nums)

%run doctests.py 
help(bounded_avg) # returns average of list of nums (nums must be between 1-100)

# Doctests 
# Doctests are snippets of interactive demonstration on a docstring:
def bounded_avg(nums):
    """returns average of list of nums (nums must be between 1-100)

        >>> bounded_avg([1,2,3])
        2

        >>> bounded_avg([1,2,101])
        Traceback (most recent call last):
            ... 
        ValueError: Outside bounds of 1-100 
    """
    for n in nums: 
        if n < 1 or n > 100: 
            raise ValueError("Outside bounds of 1-100")

    return sum(nums) / len(nums)

# Can run this test: 
# $ python3 -m doctest -v your-file.py 
# (use the doctest module, verbosely showing tests found & run)

####################################################################

# Importing

# Python includes a 'standard library' of dozens of useful modules. 
# These are not in the namespace of your script automatically. 
# You have to import them 

math.ceil(10.7) # NameError: name 'math' is not defined 
import math 
math.ceil(10.7) # 11 

# choice(seq) is a useful function: given a sequence, it returns a random item
from random import choice 
print("Let's play", choice(games)) 

choice([4,6,8,10]) # A random element from that iterable 
choice('adhhjdhjas') # Works with strings 

from random import randint 
randint(10,20) # 11 

from statistics import mean, median 
mean([2,3,4,5,6,7]) # 4.5 

import random 
random.randrange() 

from random import choice as pick_a_thing 
pick_a_thing(games)

############################################################## 

# Installing Libraries 

# docs.python.org/library/ 

from colorsys import rgb_to_hls 
rgb_to_hls(255, 0, 30) 
# (0.980392156..., 127.5, -1.0079...)

import calendar 
cal = calendar.TextCalendar()
cal.prmonth(2025,4) # Gets a real calendar
calendar.HTMLCalendar().formatmonth(2020,3) # Corresponding html calendar 

import webbrowser 

url = 'http://docs.python.org/'

# Open URL in a new tab, if a browser window is already open. 
webbrowser.open_new_tab(url)
# True

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done() 
# Running this will open a new window, drawing a picture. 

############################################################# 

# Sharing Code Between Files 
import random 

# now, we have the obj 'random', with all the funcs/classes
# within available to us 

random.choice(games)

# score.py 
def get_high_score():
    ... 
def save_high_score():
    ... 
# (unlike JS, nothing needed to "export")

# game.py 
from score import get_high_score 
high = get_high_score()

# File called helpers.py
from random import randint, choice
def get_rand_year():
    return randint(1900, 2020)
def get_rand_month():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return choice(months)

# Another file (people.py)
import helpers
def make_person(name, favColor):
    return {
        'name': name,
        'favColor': favColor,
        'birth_year': helpers.get_rand_year(),
        'birth_month': helpers.get_rand_month()
    }

%run people.py 
make_person('tommy', 'purple')
# {'name': 'tommy',
#         'favColor': 'purple',
#         'birth_year': 1965,
#         'birth_month': 'Jun'}

# Or: 
from helpers import get_rand_year, get_rand_month

def make_person(name, favColor):
    return {
        'name': name,
        'favColor': favColor,
        'birth_year': get_rand_year(),
        'birth_month': get_rand_month()
    }

############################################################

# Installing Third Party Libraries 

# ipython had to be installed 

# Using Pip to install a new package: 
$ pip3 install forex_python
... pip output here... 

$ ipython 
In [1]: from forex_python.converter import convert 
In [2]: convert("USD", "GBP", 10)
7.6543 

# Pip Installs Packages = PIP 

$ pip3 list # shows the packages that we installed  

# forex-python gives us methods like CurrencyRates(), and the convert function which connects to an API to get the answer. 

# ipython
from forex_python.bitcoin import BtcConverter 

b = BtcConverter()
b.get_latest_price('USD') # 8258.4317 
b.get_latest_price('USD') # 8261.185

########################################################## 

# Virtual Environments 

# Normally, pip makes the installed library available everywhere. This is concenient, but a little messy:

# - you might not need it for every project 
# - you might want to more explicitly keep track of which libraries a project needs 
# - you might want a new version of a library for one project, but not another 
# Python can help us by using a "virtual environment"

# Creating a virtual environment 
$ cd my-project-directory 
$ python3 -m venv venv 

$ mkdir DemoApp 
$ cd DemoApp/ # $ cd my-project-directory 
$ ls
$ 
$ python3 -m venv venv # ("using venv module, make a folder, venv, with all the needed stuff")
$ ls 
venv 
$ cd venv 
$ ls 
bin     include     lib        pyvenv.cfg 
# That makes the virtual environment folder - but you're not using it yet! 

# Using Your Virtual Environment 
$ source venv/bin/activate 
(venv) $   <-- notice shell prompt! 

# - You only need to create the virtual environment once 
# - You need to use source every time you open a new terminal window 

# What does it mean to be "using" a virtual environment? 
# - Makes certain python is the version of Python used to create the venv 
# - You have acces to the standard library of Python 
# - You don't have access to globally installed pip stuff 
# - You get to explicitly install what you want - and it will be only for here!

$ touch app.py 

# app.py 
from forex_python import bitcoin
# Works in normal python you already have.
# But on the virtual environment just created, ModuleNotFoundError 
# You install all sorts of other packages that won't conflict with the existing global installs.

# Installing into Virtual Environment 
# - Make sure you're using your venv - do you see it in your prompt? 
# - Use pip install, as usual 
# -- But now it's downloaded & installed into that venv folder 
# -- It won't be available/confuse global Python or other venvs - tidy! 

$ pip install Faker 

#app.py 
from faker import Faker
fake = Faker()

for x in range(10):
    print(fake.name())

$ python app.py 
# Whole list of 10 fake names 

# Leaving Virtual Environments 
# Use the deactivate shell command to leave the venv 

#############################################################

# Venv Continued 

# Tracking Required Libraries 
# To see a list of installed libraries in a venv:
$ pip3 freeze 
... list of installed things... 

# It's helpful to save this info in a file (typically named "requirements.txt"):
$ pip freeze > requirements.txt 
$ cat requirements # now has the list 

$ pip freeze > requirements.txt # to add more packages, and don't forget to commit 

########################################################### 

# Windows Working With Venv 

# Be in folder 
$ python3 -m venv venv 
# May get a Failing Command. 
$ sudo apt-get install python3-venv 
$ ls 
$ ls -a 
$ rm -rf venv 
$ python3 -m venv venv # should work now 
$ source venv/bin/activate # in a venv
$ python # 3.8.5 

######################################################## 

# Installing Dependencies 

# Recreating a Virtual Environment
# When using a new Python project: 
$ git clone http://path-to-project 
$ cd that-project 
$ python3 -m venv venv 

# Then, as usual when working with a venv: 
$ source venv/bin/activate 
(venv) $ pip3 install -r requirements.txt 
... pip output here ... 

$ python app.py # runs the random app  

#########################################################

# Files 
# You can open an on-disk file open(filepath,mode)
# - filepath: absolute or relative path to file 
# - mode: string of how to open file(eg, "r" for reading or "w" for writing)
# This returns an file-type instance 

file = open("morse.txt", "r")

$ python3 files.py 
$ ipython 
%run files.py 
file # <_io.TextIOWrapper ...>
help(file)

close(self, /) 
read(self, /) 
truncate()
write()

# Reading 
# Line-by-line: 
file = open("/my/file.txt")
for line in file: 
    print("line =", line)
file.close()

# All at once:
file = open("/my/file.txt")
text = file.read()
file.close()

file.seek(0) # should make 'text' work

# Writing 
file = open("/my/file.txt", "w")

file.write("This is a new line.") # Overwrites what is already in the file.
file.write("So is this.")

file.close()

# Append is just "a"

input_file = open("morse.txt", "r") 
output_file = open("translated.txt", "w")
for line in file:
    output_file.write(get_english(line))

input_file.close()
output_file.close()

