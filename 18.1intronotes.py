# // Why Python?
# // Fast, powerful, popular.
# // Express concepts at a high level.
# // super clean syntax.
# // Runs on servers(but not in a browser)
# // Particularly used for data science, machine learning, making servers, etc.
# // Learning a 2nd language helps you see many of the similarities between languages.

# // Type in python3 into the terminal, and you'll get what is a REPL(Read Evaluate Print Loop).
# // It's kind of like the chrome console, but more full featured and powerful.

# // You can type help(), topics. q to back up, and quit() to get back to the normal terminal.
# // Or ctrl + d. 
# // pip3 install ipython
# // With JavaScript you have to include jQuery or Bootstrap in HTML. But with Python
# // you use pip3. We install packages.

# // Declaring variables in Python

# // like_this (lower-snake-case), not camel-case

# // There is no keyword like let, const, var. 

# // On ipython on the WSL, chickens = 13. not let chickens=13;

# // You can redefine a simply as chickens = 20

# // Uppercase terms can indicate a constant, but they can still obviously be reassigned.

# // "Lexical function scoped", like JS variables are defined within the scope of a function.

# // Numbers - very much like JS
# // - Separate types for integers (can be any size) or floating-point.
# // -- In JS there are only floating-point numbers
# // -- Separate type for complex numbers

# // In python there is 5, and then 5.0. 
# // There is type() like typeof in JS. 
# // type(5) - 'int'
# // type(5.0) - 'float'
# // There's also complex numbers, involve imaginary numbers, which can't be expressed with regular numbers.
# // complex(3, 32) - (3+32j)
# // complex_num = complex(3, 32)
# // type(complex_num) - 'complex'

# // 2//5 - "0"
# // 10/3 - "3.3333333333333335"
# // 10//3 - "3"

# // 10 % 3 - 1 (just like JS)
# // 2/0 - "ZeroDivisionError..."

# // int(4.22223) - "4"
# // round(3.14159) - "3"
# // round(3.14159, 2) - "3.14"
# // round(3.14159, 4) - "3.1416"

# // 4.56.is_integer() - "False"
# // 4.000.is_integer() - "True"

# // Strings
# // "" and '' are the same. 
# // There are also ''' for multiple line strings.

# // '''
# // <div>
# //   <h1>HI</h1>
# // </div>
# // '''

# // Output - '\n<div>\n <h1>HI</h1>\n</div>\n'

# // Can interpolate expressions with f-strings: 
# // food = "cheese"
# // print(f"I love {food})
# // The 'f' indicates a formated string.

# // f"2+2={2+2}" - '2+2=4'

# // first = "Channing"
# // last = "Tatum"
# // full = f"Mr. {first} - {last}"
# // full - 'Mr. Channing - Tatum'
# // They are like string template literals in JS.

# // '\t' is the tab character. 
# // print(1,2,3) - "1 2 3"
# // print('\t hello') - 'hello'

# // Lists 

# // Python analog to JS arrays.
# // Ordered, can be heterogeneous [1, "apple", 13.5]
# // people = ["John", "Ringo", 45]
# // type(people) - "list"

# // Booleans
# // Python uses capitalized True and False or else you get a "NameError"

# // [False, True, 34, 'hi']
# // 3 < 5 - "True"
# // 3 <= 3 - "True"
# // 3 > 5 - "False"
# // '1' > 1 - "TypeError..."

# // Equality

# // == - equal
# // JS == means loose equality like 7 == "7"
# // === strict equality 7 === "7" is false 
# // Objects & arrays only equal when same identity.

# // Python == equality(strict about types) 7 == "7" # False
# // Structures with same items are equal [1,2,3] == [1,2,3]
# // Use 'is' to check obj identity [1,2] is [1,2] # False
# // != is 'not equal'
# // 1 != '1' - "True"

# // [1,2,3] is [1,2,3] - "False"
# // nums = [1,2,3]
# // copy = nums
# // nums is copy - "True"
# // There's also 'is not', negated object identity.

# // Indentation

# // In many langauges, you use {} to show blocks.
# // Python is different. All that matters is indentation. 

# // if age >= 18:
#     // print("Please go vote!")
#     // register_to_vote()

# // is very different than:

# // if age >= 18:
#     // print("Please go vote!")
# // register_to_vote()

# // In Python everyone agrees with 4 spaces of indentation
# // However Python doesn't actually care, as long as you are consistent.

# // age = 17
# // if age < 18:
#         // print("YOU ARE A CHILD") Python automatically idents. 

# // Running Files

# // .py for vscode file for Python file. 
# // There is no browser for it though. Straight from the command line is the first way, python3 mygame.py
# // Runs Python, loads mygame.py, executes the code, returns to the terminal when done.

# // Alternatively, ipython 
# // %run nameoffile

# // If_Elif_Else

# // if, elif, else
# //if:
#     //jfksjdf
# //elif:
#     //lkls;dfk
# //else:
#     //lkdfsld

age = 19
isBirthday = True

if age >= 21:
    print("YOU CAN DRINK.")
    if isBirthday:
        print("HAPPY BIRTHDAY, HERE IS A FREE MARTINI!")
elif age >= 18:
    print("YOU CAN COME IN BUT NO DRINKING!")
    if isBirthday:
        print("HAPPY BIRTHDAY, HERE IS A FREE APPLE JUICE!")
else:
    print("SORRY GO HOME KID!")

# Ternary 

# let msg = (age >= 18) ? "go vote!" : "go play!" JS
# msg = "go vote!" if (age >= 18) else "go play!" Python

color = 'teal'
print("GOOD CHOICE") if color == 'teal' else print("MEH")
# do_if_true if CONDITION else do_if_false 

# condition ? do_if_true : do_if_false

# Boolean

# JS: &&, ||, !
# Python: and, or, not

age = 68

if age < 10 or age >= 65:
    print("Your ticket is $5")
else:
    print("Your ticket is $10")

# Your ticket is $5

age = 40 

if age < 10 or age >= 65:
    print("Your ticket is $5")
else:
    print("Your ticket is $10")

# Your ticket is $10 

not age == 40 
# False 

# Because of false precedence, it is the same as:

not (age == 40)

# Parentheses go first, which is true, and then negated with not.

# Python Truthiness and Falsiness

# JS: 0, 0.0, "", undefined, null, NaN, false are falsy.
# JS: perhaps unexpectedly, these are truthy... [], {}

# Python: 0, 0.0, "", None, False, [](empty list), {}(empty dictionary), set()(empty set) are falsy.

# None is like the Python version of NaN. 

jobs = ['walk dog']

if jobs:
    print("CANT GO HOME YET, MORE WORK TO DO!")

# CANT GO HOME YET, MORE WORK TO DO!

jobs = []

if jobs: 
    print("CANT GO HOME YET, MORE WORK TO DO!")

# *nothing* 

# JS is not as easy: 
# let jobs = []
# if(jobs) console.log("CAN'T GO HOME") - CAN'T GO HOME
# if (jobs.length) console.log("CAN'T GO HOME") - *nothing*

# While Loops

count = 10 

while count > 0:
    print(count)
    count = count - 1 # or "count -= 1", but not "count--"
print("Liftoff!")

num = 0 

while num <= 100:
    print(num)
    num = num + 10 # num += 10

print("ALL DONE") 

# JS: 
# while(num <= 100) {
#     console.log(askd)
#     num += 10
# }

# num++ doesn't exist in Python

num = 0 

while num <= 100:
    if num == 50:
        break 
    print(num)
    num += 10

print("ALL DONE")

##################

guess = input("enter your guess")

# enter your guess40123

# guess - '40123'

target = 37 
guess = None

while guess != target:
    guess = input("Please enter a guess...")
    if guess == 'q' or guess == 'quit'
        break
    guess = int(guess)
print("ALL DONE")

# For Loops 

# JS: for(let i= 10; i < 50; i++){

# }

# In Python, they are like JS for...of loops:
for snack in ["peanut", "Twizzler", "Mars Bar"]:
    print("I ate a", snack)

colors = ['red', 'orange', 'yellow', 'green']
for color in colors:
    print(color)

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(char)

for num in "abcde":
    print("HELLO")

# Can also use range() function:
 for num in range(5): # makes [0, 1, 2, 3, 4]
    print(num)

# JS: 
for(let i = 0; i < 10; i++){

}

# Python Ranges

range(9)
# output - range(0, 9) 
# Doesn't print out the range of numbers by itself.

for num in range(9):
    print(num)

list(range(10))
# [0,1,2,3,4,5,6,7,8,9]

list(range(5,10))
# [5,6,7,8,9]

list(range(1,10,2))
# [1,3,5,7,9]

list(range(10,0,-1))
# [10,9,8,7,6,5,4,3,2,1]

# Python Functions

def add_numbers(a, b):
    sum = a + b 
    print("doing math!")
    return sum

def greet(person):
    return f"Hello there, {person}"

greet()

# Functions that don't explicitly 'return' return None

return_val = greet('charles')
# Hello there, charles
type(return_val)
# NoneType

def divide(a, b):
    return a/b 

type(3) 
# True

type(3) is int
# True

type(3.4) is int
# False 

def divide(a,b):
    if type(a) is int and type(b) is int:
        return a/b 
    return 'a and b must be integers!'

# Function Arguments

# Providing too many/too few arguments is an error (in JS, this is ignored / becomes undefined)

def add_three_numbers(a,b,c):
    return a + b + c 
add_three_numbers(10, 20, 30) # 60, yay!
add_three_numbers(10, 20) # error!
add_three_numbers(10, 20, 30, 40) # error!

def three_things(a,b,c):
    print("HI")

three_things(1,2,3) 
# HI
three_things(1,2)
# TypeError

def send_email(to_email, from_email, subject, cc, bcc, body)
    email = f"""
      to: {to_email}
      from: {from_email}
      subject: {subject}
      ---------------------
      body: {body}
    """
    print(email)

send_email('blue@cat.com', 'colt@human.com', 'meow',) # Gets annoying to remember the exact order of parameters.

send_email(subject="MEOW", to_email="blue@gmail.com", 
from_email="colt@humans.com", body="Hi blue, you are my cat. I love you!") # Order doesn't matter anymore.

# terminal says this when %run functions.py:

# to: blue@gmail.com
# from: colt@humans.com
# subject: MEOW
# ----------------
# body: Hi blue, you are my cat. I love you!

# In the terminal you can also write
# help(send_email) - gives signature of that function.
# Hit q to get out. 

def power(num, power=2):
    return num ** power

# power(4,3) - 64

# Docstring_help_dir_comments

# dir() 
# "Show me the methods and attributes of this object"
# dir([])
# ['__add__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# help()
# Welcome to Python 3.7's help utility!
# You can access all the syntax you basically need. 
# help(print) - gives info about print.

# help(25) - gets internal documentation. 
# help(str) - built in documentation, how it works and methods. 
# dir(str) - gives directory of different methods and properties. help() gets even more info.

# Comments and Docstrings
# '#:' rest of line is comment ( use to explain complex code)
# String as very first thing in file/function is "docstring"
# - Use to document what the function/file does 
# - Shown when you ask for help(some_function)

def add_limited_numbers(a,b):
    """Add two numbers, making sure sum caps at 100."""

    sum = a + b 

    #If this required explanation, comment like this

    if sum > 100:
        sum = 100
    
    return sum 

# In the terminal, if you help(add_limited_numbers)
# "Add two numbers, making sure sum caps at 100." shows up.

# Triple quotes are used even though the string fits on one line. This makes it easy to later expand it.

# Most libraries, especially the popular ones we'll be using, have great internal documentation. 
# Their codes has a bunch of docstrings, so you can ask for help() at any point.