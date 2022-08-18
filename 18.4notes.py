# Intro OOP Python 

# OO Review 
# - class (blueprint for new objects, defines attributes & methods)
# - method (function defined on class, can see/change attributes on instance)
# - class method (function defined on class, called on class, not individual instance)

# Instances 
# Like JS you make an instance by calling the class: 
from collections import Counter 
# make instance of a counter 
counts = Counter("hello world")

type(counts) # 'collections.Counter'

isinstance(counts, Counter) # True 

my_counter = Counter("OOMPA LOOMPA")
my_counter # Counter({'O': 4, 'M': 2, 'P': 2, 'A': 2, ' ': 1, 'L': 1})
type(my_counter) # collections.Counter 

isinstance(my_count, Counter) 
# True 

my_counter.most_common()
[('O', 4), ('M', 2), ('P', 2), ('A', 2), (' ', 1), ('L', 1)]

from datetime import date 
date() # error 

int(), list(), str() # are instances of classes

my_date = date(2020,2,14)

my_date.day # 14 
my_date.year # 2020 
my_date.weekday() # 4 

# Instances 
# JS: 
# - get/set attr of obj: o.name or o['name']
# - call method: o.method() or o['method']()

# Python: 
# - get/set attr of obj: o.name 
# - call method: o.method()
# - retrieve value from dictionary: o['my-key']
# -- not the same thing! 

# What can I do with this obj?
help(obj) # Show help about obj and methods
dir(obj) # List methods/attrs of obj 

#########################################################

# Class Syntax 

# Making classes similar to JS:
from math import sqrt 

class Triangle: 
    "Right triangle."

    def __init__(self, a, b):
        "Create triangle from a and b sides."
        self.a = a 
        self.b = b 

    def det_hypotenuse(self):
        "Get hypotenuse (length of 3rd side)."
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def get_area(self):
        "Get area of triangle."
        return (self.a * self.b) / 2 

    def describe(self):
        return f"My area is {self.get_area()}"

# JS:
class Triangle {
    funtion constructor(a,b){
        this.a = a;
        this.b = b;
    }
}

my_counter = Counter("OOMPA LOOMPA")
my_counter # Counter({'O': 4, 'M': 2, 'P': 2, 'A': 2, ' ': 1, 'L': 1})
# ^ This is calling the __init__ on the Counter class.

# Self 
# self is similar to 'this'
# - 'this' is a bit magical: it automatically gets created 
# - 'self' is explicit: you must list it as the first argument of methods 
# -- It's just a normal variable, otherwise 

%run triangle 
t = Triangle(3,4) 
t # <__main__.Triangle at 0x108c47710> 
type(t) # __main__.Triangle 

import math # Must import in order to use sqrt
math.sqrt

t.get_hypotenuse() # 5.0 

dir(t) # includes 'a', 'b', 'get_hypotenuse' as instances of t 

t.get_area() # 6.0 

t2 = Triangle(9, 12) 
t2.get_hypotenuse() # 15.0 
t2.get_area() # 54.0 

########################################################## 

# Class Methods 

# Less common than instance methods 
# Factory method is a common class method

from math import sqrt 
from random import randint

class Triangle: 
    """
    A class used to represent a right triangle.

    Attributes 
    ---------------

    a: int
        length of side a 
    b: int
        length of side b
    """

    def __init__(self, a, b):
        "Create triangle from a and b sides."
        self.a = a 
        self.b = b 

    def __repr__(self):
        return f"Trianle(a={self.a}, b={self.b})"
    @classmethod # called a 'decorator'
    def random(cls):
        """Class method which returns Triangle with random sides"""
        # print(cls)
        # return cls(234,54) 
        return cls(randint(1,20), randint(1,20))

    def det_hypotenuse(self):
        "Get hypotenuse (length of 3rd side)."
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def get_area(self):
        "Get area of triangle."
        return (self.a * self.b) / 2 

    def describe(self):
        # return f"My area is {self.get_area()}"
        return f"I am a triangle with sides: {self.a} & {self.b}" 

%run triangle.py 
Triangle.random() # <class '__main__.Triangle'> 

# If I remove the decorator, I get a TypeError 

t = Triangle.random()
t # <__main__.Triangle at 0x1048bffd0>
t.a # 234 
t.b # 54 
t.get_hypotenuse() # 240.14995...

t=Triangle.random()
t # <__main__.Triangle at 0x10330cb00>
t.a # 15 
t.b # 5 
t.get_hypotenuse() # 15.811...

######################################################### 

# Inheritance 

# Like in JS, classes can subclass other objects: 
from triangle import Triangle 

class ColoredTriangle(Triangle):
    """Triangle that has a color.""" 
    def __init__(self, a, b, color):
        # get parent class ['super()'], call its '__init__()' 
        super().__init__(a,b)
        
        self.color = color 

    def describe(self):
        # return f"I am a triangle with sides: {self.a} & {self.b}. I am {self.color}"
        msg = super().describe() + f" I am {self.color}" # Works the same.
        return msg
# Super 
# Like JS, super finds parent class: 
# JS: super is parent, super(...) calls parent constructor func 
# Python: super() is parent, super().__init__(...) is parent initializer 

%run colored_triangle.py 

t = ColoredTriangle(3,4,'purple')
t # <__main__.ColoredTriangle at ...> 
t.a # 3  
t.b # 4 
t.color # purple 
t.get_area() # 6.0 
t.get_hypotenuse() # 5.0 

# After adding: return f"I am a triangle with sides: {self.a} & {self.b}. I am {self.color}"
t.describe() # 'I am a triangle with sides: 3 & 4'

##############################################################

# Class Docstrings

# As always, good style to have comment explaining purpose of class & methods. 
# (Like with the Triangle classes)

##############################################################

# Dunder methods 

# Documenting Instance 
# We can do this by making a __repr__(representation) method:

# for the Triangle class: 
def __repr__(self): 
    return f"<Triangle a={self.a} b={self.b}>"

>>> tri = Triangle(3,4) 
>>> tri # <Triangle a=3 b=4> 

# When you print an instance/examine in Python shell, often not helpful: 

>>> tri = Triangle(3,4) 
>>> tri # <__main__.Triangle object at 0x1012a6358> 

# Would be nicer to see values for a and b 

# Many special methods on the Python docs.

t = Triangle(9,12) 
t # Triangle(a=9, b=12)

repr('hello')
# "'hello'" 
repr(list())
# '[]' 
repr(t)
# 'Triangle(a=9, b=12)' 

eval("4+4") # 8

# __repr__(self) and __str__(self) are both string representations of obj classes 

# repr is unambiguous. Should include any info necessary to reconstruct whatever the object is. 
# str is about creating a human readable version of your object. 

# We can add in the Triangle class: 
def __str__(self): 
    return self.describe() 

tri = Triangle(3,4) 
tri # Triangle(a=3, b=4) 

repr(tri) # 'Triangle(a=3, b=4)'
str(tri) # 'I am a triangle with sides: 3 & 4' 

print(tri) # I am a triangle with sides: 3 & 4 

tri2 = Triangle(3,4) 
tri == tri2 # False 

def __eq__(self, other):
    return self.a == other.a and self.b == other.b 

t1 = Triangle(3,4) 
t2 = Triangle(3,4) 
t1 == t2 # True 

t2.a = 4 
t1 == t2 # False