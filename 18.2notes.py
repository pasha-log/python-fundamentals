# Len 

# __len__, a dunder special convention in Python. You are not supposed to call them directly but you can.

"hello world".__len__()
# 11
[1,2,3,4].__len__()
# 4

# Length of Structure 
# Generic len(x) returns length of x:
# - # chars in string, # items in list, dictionary, and a set.

len("alksjdaksl")
# 10 
len([])
# 0

# Lists in more detail

# Lists are just like JS arrays. 
# O(n) to search, add, delete. Except when at end O(1).

# One way to make a list is using the constructor function, list().
# This will make list from iterating over argument:
letters = list("apple") # ['a', 'p', 'p', 'l', 'e']

list(range(10,20,2)) # [10,12,14,16,18]

# Membership - can check for membership with in:
if "taco" in foods:
    print("Yum!")
if "cheese" not in foods:
    print("Oh no!")

vegan_no_nos = ['eggs', 'meat', 'milk', 'fish', 'figs']

pie_ingredients = ['flour', 'apples', 'sugar', 'eggs', 'salt']

for food in pie_ingredients:
    if food in vegan_no_nos:
        print(f"OH NO, CANNOT EAT {food}! IT'S NOT VEGAN!")
    else: 
        print(f"YUM, I LOVE {food}!") 

# Retrieving By Index - can retrieve/mutate item with [n]:
print(fav_foods[0])
fav_foods[0] = "taco"

vegan_no_nos[-1] # 'figs' 

vegan_no_nos[2] = 'dairy'
vegan_no_nos = ['eggs', 'meat', 'dairy', 'fish', 'figs']

# List Slicing

# Can retrieve list from list : 
lst[start:stop:step]
# start: Index to begin retrieval (default start)
# stop: Index to end retrieval before (default: end)
# step: Number to step (default: 1)

# Lists are references types like arrays. 
copy = vegan_no_nos
copy[0] = "EGGGGGSSSSS"
copy # ['EGGGGGSSSSS', 'meat', 'milk', 'fish', 'figs']
vegan_no_nos # ['EGGGGGSSSSS', 'meat', 'milk', 'fish', 'figs']

copy is vegan_no_nos # True 
[1,2,3] is [1,2,3] # False
[1,2,3] == [1,2,3] # True 

vegan_no_nos # ['EGGGGGSSSSS', 'meat', 'milk', 'fish', 'figs']
vegan_no_nos[2:4:1] # ['milk', 'fish']
vegan_no_nos[0:5:1] # ['EGGGGGSSSSS', 'meat', 'milk', 'fish', 'figs']
vegan_no_nos[0:5:2] # ['EGGGGGSSSSS', 'milk', 'figs']

nums = list(range(0,100,1))
nums[50:60:1] # [50,51,52,53,54,55,56,57,58,59]
# The start is inclusive, but not the end.

alpha = ['a', 'b', 'c', 'd', 'e']

alpha[2:] # ['c', 'd', 'e']
alpha[2:4] # ['c', 'd']
alpha[:3] # ['a', 'b', 'c']
alpha[::2] # ['a', 'c', 'e']
alpha[3:0:-1] # ['d', 'c', 'b']
alpha[::-2] # ['e', 'c', 'a']

nums[::-10] # [99,89,79,69,59,49,39,29,19,9]

nums[10:20:-1] # []

nums[20:10:-1] # [20,19,18,17,16,15,14,13,12,11]

# Splicing 

# Can assign a list to a splice:
alpha = ['a', 'b', 'c', 'd', 'e']
alpha[2:] = ['y', 'z']
print(alpha) # ['a', 'b', 'y', 'z']

alpha[1:3] = []
print(alpha) # ['a', 'z']

colors = ['red', 'orange', 'yellow']

colors[0:1] = ['dark red', 'pink']
colors # ['dark red', 'pink', 'orange', 'yellow']

colors[3:] = ['dark yellow', 'green', 'blue', 'purple']
colors # ['dark red', 'pink', 'orange', 'dark yellow', 'green', 'blue', 'purple']

colors[5:] = []
colors # ['dark red', 'pink', 'orange', 'dark yellow', 'green']

colors[::2] = ['LOL', 'LOL', 'LOL']
colors # ['LOL', 'pink', 'LOL', 'dark yellow', 'LOL']

colors[0:2] = []
colors # ['LOL', 'dark yellow', 'LOL']

colors[::] = []
colors # []

# List methods

chickens = ['butters', 'lady gray', 'stevie chicks']
len(chickens) # 3 

chickens.append('henry')
chickens # ['butters', 'lady gray', 'stevie chicks', 'henry']

# append() takes exactly one argument (2 given)

copy_flock = chickens 
copy_flock.append('lucy') 
# copy_flock is not a copy for now, but just a reference to chickens.

copy_flock = chickens.copy()

copy_flock is chickens 
# False  

copy_flock == chickens 
# True 

chickens.append('romeo')

chickens.count('butters')
# 1 
chickens.append('butters')
chickens.count('butters')
# 2 
chickens.count('aklsjd')
# 0 

chicks = ['herbert', 'annabelle']
chickens.extend('chicks') 
chicks 
# ['herbert', 'annabelle']
chickens 
# ['butters', 'lady gray', 'stevie chicks', 'henry', 'lucy', 'romeo', 'butters', 'herbert', 'annabelle']

help(extend)
# Extend list by appending elements from the iterable.

chickens.extend("HELLO")
chickens # ['butters', 'lady gray', 'stevie chicks', 'henry', 'lucy', 'romeo', 'butters', 'herbert', 'annabelle', 'H', 'E', 'L', 'L', 'O']

chickens.index('henry')
# 3
chickens[3] 
# 'henry'

chickens.index('L')
# 11 
# Gives only the first matching index just like in JS 

chickens.index('chuck')
# 'chuck' is not in list. ValueError

chickens.insert(0, 'tina')
# Adds 'tina' to the beginning of the list 

chickens.insert(9, ['harry', 'hermione'])

chickens.pop()
# 'O'
# Just like JS, you can remove the end of a list. 

chickens.pop(0)
# 'tina' 
# Removes 'tina' 

chickens.reverse() 
# Reverses an entire list. 

chickens.sort() 
# Orders the list in alphabetical order.

nums = [45, 62,33,12,1,-9,-99,0,1234]
nums.sort()
nums
# [-99, -9, 0, 1, 12, 33, 45, 62, 1234]

nums.sort(reverse=True)
# [1234,62,45,33,12,1,0,-9,-99]

nums.append('HELLO I AM DEFINITELY A NUMBER')
nums.sort() 
# TypeError: '<' not supported between instances of 'str' and 'int' 

# More on strings 
price = 3.50 
qty = 7 
print(f"Your total is ${price * qty}")
# Your total is $24.5 

nums = [1,2,3]
str(nums) # "[1,2,3]"

3 in nums 
# True 

price = '$56.99'
'$' in price # True 

# Can slice to retrieve substring ("apple"[1:3] == "pp")
# Cannot splice; strings are immutable!

price[0] = '#'
# TypeError: 'str' object does not support item assignment 

'#' + 'asd'
# '#asd'

'!' * 10 
# '!!!!!!!!!!'

msg = 'hcehlilcok!e!n'
msg[0] # 'h' 
len(msg) # 14 
msg[13] # 'n' 
msg[5:] # 'ilcok!e!n'
msg[0:5] # 'hcehl'
msg[::2] # 'hello!!'
msg[1::2] # 'chicken'

# Can iterate over, get letter-by-letter:
for letter in word:
    print("Letter")

# String Methods 

# zfill(self, width, /)
    # Pad a numeric string with zeros on the left, to fill a field of the given width.

    # The string is never truncated.

'92'.zfill(5) # '00092'
'9245'.zfill(5) # '09245'
'92453'.zfill(5) # '92453'

msg # 'hcehlilcok!e!n' 

msg.count('h') # 2

msg.count('H') # 0 

msg.endswith('n') # True 

msg.endswith('!') # False 

msg.endswith('!n') # True 

person = "Mr. Jones"

person.startswith('Mr.') # True 

person.startswith('Mr. ') # True 

person.find('.') # 2 

msg # 'hcehlilcok!e!n'
msg.find('!') # 10
msg.find('!e!') # 10 

person.find('Mr.') # 0 
person.find('J') # 4 
person.find(' ') # 3 
person.find('?') # -1 
person[-1] # 's' 
person[-2] # 'e'

'hello4'.isdigit() # False
'4'.isdigit() # True
'434323423'.isdigit() # True

chickens = ['annabelle', 'butters', 'butters', 'henry', 'herbert', 'lady gray', 'lucy', 'romeo', 'stevie chicks']
'|'.join(chickens) # 'annabelle|butters|butters|henry|herbert|lady gray|lucy|romeo|stevie chicks'
'.'.join('LOL') # 'L.O.L'
''.join(chickens) # 'annabellebuttersbuttershenryherbertlady graylucyromeostevie chicks'

'LOL'.lower() # 'lol'
'lololSA'.upper() # 'LOLOLSA'
'mrs kitty cat'.capitalize() # "Mrs kitty cat"
"LOL".isupper() # True 
"LOl".isupper() # False

things= 'apples-tomatoes-pickles'
things.replace('-', '=') # 'apples=tomatoes=pickles'
things.replace('-', '=', 1) # 'apples=tomatoes-pickles'

text = "I hate you so much"
text.replace(' ', '...') # 'I...hate...you...so...much'

tweet = 'YOLO hahah omg #YOLO' 
tweet.replace('YOLO', '') # ' hahah omg #'
tweet.replace('YOLO', '', 1) # ' hahah omg #YOLO'
tweet.replace('YOLO', '', -1) # ' hahah omg #'

animals = 'goats,chickens,ducks,pigs,alpacas' 
animals.split(',') # ['goats', 'chickens', 'ducks', 'pigs', 'alpacas']

text = text.replace(' ', '...')
text # 'I...hate...you...so...much' 
text.split('...') # ['I', 'hate', 'you', 'so', 'much']
"YOLO".split('') # ValueError: empty separator 
"YOLO".split() # ['YOLO'] 
list('YOLO') # ['Y', 'O', 'L', 'O']

""" 
Hello 
I
Love 
You
""".splitlines() # ['', 'Hello ', 'I ', 'Love', 'You']

# strip(self, chars=None, /)
#     Return a copy of the string with leading and trailing whitespace removed.

#     If chars is given and not None, remove characters in chars instead.

user_input = '   catlady  '
user_input.strip() # 'catlady'
user_input = '   ca  t lady  '
user_input.strip() # 'ca  t lady'

# Dictionaries Intro 

# They are key-value pair data structures.
# Mutable, ordered mapping of keys -> values 
# O(1) runtime for adding, retrieving, deleting items (like JS object or Map)
# Confusingly enough, there are also objects in Python.  

# In JS, dictionaries are a type of object.

const person = {first: 'nikolai', last: 'zarkoface', age: 45}

person = {'first':'henry'0}

# On the console:
const thing = {45: 'forty-five'}
thing # {45: "forty-five"}
thing['45'] # "forty-five"
thing[45] # "forty-five"

# Making Dictionaries
# Values can be any type.
# Keys can be any immutable type 
my_dict = {
    'ok': "yes",
    42: "all good", 
    [1,2]: 2
} # ERR: not immutable 

# Dictionaries 
# Mutable, ordered mapping of keys -> values 
# O(1) runtime for adding, retrieving, deleting items (like JS object or Map)

chicken = {name: 'butters'} # NameError: name 'name' is not defined 

chicken = {'name': 'butters', 'age': '6 months', 'breed': 'Silkie'}

stuff = {True: 34, 100: 'AWESOME'}
stuff = {True: 34, 100: 'AWESOME', [1,2,3]: 'asd'} # TypeError: unhashable type: 'list'

# Membership & Retrieval 
# 'in' checks for membership of key ("apple" in fruit_colors)

'breed' in chicken # True 
'butters' in chicken # False because it only looks for the key

# [] retrieves item by key (fruit_colors['apple'])
# - Cannot use dot notation, though (no fruit_colors.apple)
# - Failure to find is error (can say .get(x, default))

chicken['breed'] # 'Silkie'  
chicken['age'] # '6 months'
chicken['age'] = 12 
chicken # {'name': 'butters', 'age': '12', 'breed': 'Silkie'}

chicken.get('weight', '2 lbs') 

dict() # {} is an empty dictionary
dict("hi") # ValueError: dictionary update sequence element #0 has length 1; 2 is required.
dict([[True,0], [False,1]]) # {True: 0, False: 1}

# Looping over dictionaries 

ages = {"whiskey": 6, "Fluffy": 3, "Ezra": 7}
for name in ages.keys():
    print(name)
for age in ages.values():
    print(age)
for name_and_age in ages.items():
    print(name_and_age)

chicken = {
    'name': 'Lady Gray', 
    'breed', 'Silkie', 
    'total_egg_count': 12,
    'egg_chart': {
        'M': True, 
        'T': True, 
        'W': True, 
        'TH': True, 
        'F': True, 
        'S': False, 
        'SU': True
    }, 
    'coop_mates': ['Butters', 'Stevie', 'Henry']
} 

# %run dicts.py 
chicken.keys()
dict_keys(['name', 'breed', 'total_egg_count', 'egg_chart', 'coop_mates'])

keys = chicken.keys()

for key in chicken.keys():
    print(key)

# name 
# breed 
# total_egg_count
# egg_chart
# coop_mates

chicken.values() 
# dict_values([....])

for value in chicken.values():
    print(value)

# All the values of chicken
 
chicken.items()
# dict_items([('name', 'Lady Gray'), ('breed', 'Silkie'), ('total_egg_count', 12), ('egg_chart', {'M': True, 'T': True, 'W': True, 'TH': True, 'F': True, 'S':...})])

for pair in chicken.items():
    print(pair)

# ('name', 'Lady Gray')
# ('breed', 'Silkie')
# ... 

# Can unpack name_and_age while looping: 
for(name,age) in ages.items():
    print(name, 'is', age)

for (k, v) in chicken.items():
    print(k, '--->', v)

# name ---> Lady Gray 
# breed ---> Silkie 
# total_egg_count ---> 12 
# egg_chart ---> {...}
# ... 

# Dictionary methods

chicken['sex'] # KeyError: 'sex' 
chicken.get('sex', 'unsexed') # 'unsexed'

chicken['sex'] = 'Hen'
chicken.get('sex', 'unsexed') # 'Hen'

keys = list(chickens.keys())
keys.sort() # chicken keys become alphabetically ordered.

[1,2,3].copy() # [1,2,3] 

nugget = chicken 
nugget is chicken # True 

nugget = chciken.copy() 
nugget == chicken # True 
nugget is chicken # False 

nugget['egg_chart'] # {'M': True, ...}
nuugget['egg_chart'] is chicken['egg_chart'] # True 

chicken.pop('name') # 'Lady Gray' (removes this pair completely.)

chicken.popitem() # ('sex', 'Hen')
chicken.popitem() # ('coop_mates', ['Butters', 'Stevie', 'Henry'])

# fromkeys(iterable, value=None, /) method of builtins.type instance
#     Create a new dictionary with keys from iterable and values set to value.

{}.fromkeys('MTWHF', True) # {'M': True, 'T': True, 'W': True, 'H': True, 'F': True}

chicken.fromkeys('MTWHF', True) # Creates new dictionary for us, doesn't actually affect the dict that is being called upon. 
chicken # Nothing has changed. 

chicken.clear() # Erases the contents completely. 
chicken # {}
chicken['color'] = 'gray'
chicken # {'color': 'gray'}

# Set Intros 
# Unordered, uique collection of items, like JS Set 
# O(1) runtime for adding, retrieving, deleting 

# Making Sets 
# Use {}, but with only keys, not key: value 
colors = {"red", "blue", "green"}
languages = {'ruby', 'python', 'javascript'} 
languages # {'javascript', 'python', 'ruby'}
type(languages) # set 

languages = {'ruby', 'python', 'javascript', 'ruby'}
languages # {'javascript', 'python', 'ruby'}

# JS 
new Set()

voted_languages = ['ruby', 'python', 'javascript', 'scala', 'ruby', 'python', 'python', 'scala']
set(voted_languages) # {'javascript', 'python', 'ruby', 'scala'}
# Seems like there is an order set in stone, but you can't access the contents with indices. 

set('$%#&') # {'#', '$', '%', '&'}
things = {2, 'snake', 'mario', True, [1,2,3]} # TypeError: unhashable type: 'list'
things = {2, 'snake', 'mario', True} # Works 
# All elements are unique and immutable. Cannot add mutable data structures like lists. 

########################################################
# Set Methods 

languages # {'javascript', 'python', 'ruby'}
'scala' in languages # False 

languages.add('scala') # adds 'scala' to the list. 
languages.pop() # 'scala' is removed, but returned to us. 
languages.remove('python') # 'python' is removed. 
len(languages) # 1 
languages.add('java') 
languages # {'java', 'javascript'}
copy = languages
copy == languages # True 
copy is languages # True
copy = languages.copy() 
copy # {'java', 'javascript'}
copy == languages # True 
copy is languages # False 

#######################################################

# Set Operations 
# Not in JS yet.

moods = {"happy", "sad", "grumpy"}
dwarfs = {"happy", "grumpy", "doc"}
moods | dwafs # union: {"happy", "sad", "grumpy", "doc"}
moods & dwarfs # intersection: {"happy", "grumpy"}
moods - dwarfs # difference: {"sad"}
dwarfs - moods # difference: {"doc"}
moods ^ dwarfs # symmetric difference: {"sad", "doc"}

lemon = {'sour', 'yellow', 'fruit', 'bumpy'}
banana = {'fruit', 'smooth', 'sweet', 'yellow'}

lemon | banana # {"bumpy", "fruit", "smooth", "sour", "sweet", "yellow"}
banana | lemon # Would be the same because order doesn't matter.

 all_features = lemon | banana 
 banana.union(lemon) # {"bumpy", "fruit", "smooth", "sour", "sweet", "yellow"}

banana | lemon | {'fruit', 'green', 'tart'} # A third set gets combined. 

lemon & banana # {'fruit', 'yellow'} are things they have in common.
banana.intersection(lemon) # {'fruit', 'yellow'} as well

lemon - banana # {'bumpy', 'sour'}
banana - lemon # {'smooth', 'sweet'}
lemon.difference(banana) # {'bumpy', 'sour'}
banana.difference(lemon) # {'smooth', 'sweet'}

banana ^ lemon # {'bumpy', 'smooth', 'sour', 'sweet'}
banana & lemon # {'fruit', 'yellow'}
lemon.symmetric_difference(banana) # {'bumpy', 'smooth', 'sour', 'sweet'}

orange = ['fruit', 'bumpy', 'orange', 'sweet']

lemon & orange # TypeError: unsupported operand type(s) for &: 'set' and 'list'

lemon.intersection(orange) # {'bumpy', 'fruit'} Orange is created into a set, or a set out of orange.
orange.intersection(lemon) # AttributeError: 'list' object has no attribute 'intersection'

#############################################################

# Set Speed Test 

lemon ^ banana # {'bumpy', 'smooth', 'sour', 'sweet'}

for adj in banana | lemon | set(orange): 
    print(adj)

list(lemon) # ['fruit', 'sour', 'bumpy', 'yellow']
list(lemon & banana) # ['fruit', 'yellow']

##############################################################

# Tuples 
# Kind of like lists. 
# Immutable, ordered sequence (like a list, but immutable)
# Cannot be changed (immutable)

colors = ('red', 'yellow', 'green')
type(colors) # tuple 
len(colors) # 3 
colors[0] # 'red'
colors[1] # 'yellow'
(1,True,(1,2),[])
(3) # Cannot recognize as a tuple. Just parantheses. 
tup = (3,) # Now a tuple. 
(1,1,1,1,1,1,1,1,2) # Does not have to be unique 
tuple([1,2,3,4]) # (1,2,3,4)

# What are these good for? 
# Slightly smaller, faster than lists. 
# Since they're immutable, they can be used as dict keys or put into sets. 

chicken # {'color': 'gray'}
chicken['breed'] = 'Silkie'
chicken # {'color':'gray', 'breed':'Silkie'}
chicken.items() # dict_items([('color', 'gray'), ('breed', 'Silkie')])
for (k,v) in chicken.items():
    print(k,v)
# color gray 
# breed Silkie 

board = {
    (0,0):'X',
    (0,1): None, 
    (0,2): 'O',
    (1,0): 'X', 
    (1,1): 'O'
}

(1,2,3,1,2,1).count(1) # 3 
(1,2,3,1,2,1).index(3) # 2 

##########################################################

# Comprehensions 
# No JS analog 

# List comprhensions

# Python has filter() and map(), like JS but comprehensions are even more flexible.

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
evens= []
for nums in nums:
    if num% 2 == 0:
        evens.append(num)

print(evens) # all evens 

# But instead you can say:
evens = [num for num in nums if num % 2 == 0]

# It is the act or process of comprising. 

[num * 2 for num in nums]

new_list = []
for num in nums:
    new_list.append(num * 2)

['HIII' for num in nums] # Replaces every element with 'HIII' 

# [what_to_append for thing in list]

[n**2 for n in [2,4,6,8]] # [4,16,36,64]

[char.upper() + '.' for char in 'lmfao'] # ['L.', 'M.', ...]

[num/2 for num in range(10,20)] # [5.0, 5.5, 6.0, 6.5, ...]

#################################################################

# More list comprehensions 

[for x in range(3)] # [0,1,2]
[[] for x in range(3)] # [[], [], []]
[[0 for y in range(3)] for x in range(3)] # [[0,0,0], [0,0,0], [0,0,0]]
# 0 Could be replaced with None

def gen_board(size, initial_val=None)
    return [[initial_val for x in range(size)] for y in range(size)]

gen_board(3) 
# [[None, None, None],[None, None, None],[None,None,None]]
gen_board(5) # Five lists of 5 Nones 
gen_board(5,0) # Same but with 0

[x for x in range(10) if x % 2 == 0] # [0,2,4,6,8]

chickens = [
    {'name':'Henry', 'sex':'Rooster'},
    {'name':'Lady Gray', 'sex':'Hen'},
    {'name':'Junior', 'sex':'Rooster'},
    {'name':'Stevie Chicks', 'sex':'Hen'},
    {'name':'Rocket', 'sex':'Hen'},
    {'name':'Butters', 'sex':'Rooster'}
]
hens = [bird["name"] for bird in chickens if bird["sex"] = 'Hen']

scores = [55, 89, 99, 87, 60, 70, 74, 76, 90, 82]
# grades = ['PASS' for score in scores if score >= 70]
grades = ['PASS' if score >= 70 else "FAIL" for score in scores]
[do_this if something else do this for thing in things]

#################################################################

# Dictionary Set Comparisons 

# Can make lists via comprehensions from any kind of iterable:
vowels = {'a', 'e', 'i', 'o', 'u'}
word = 'apple'
vowel_list = [ltr for ltr in word if ltr in vowels]
# Can make 'dictionary comprehensions' and 'set comprehensions':
evens_to_doubled = {n:n*2 for n in nums if n%2 == 0}
a_words = {w for w in words if w.startswith("a")}

{day for day in 'MTWRFSU'}
# {'F', 'M, 'R', 'S', 'T', 'U', 'W'}
{day:0 for day in 'MTWRFSU'}
# {'M':0, 'T':0, 'W':0, 'R':0, 'F':0, 'S':0, 'U':0}

{num: num*num for num in range(1,10) if num % 2 == 0}
# {2:4, 4:16, 6:36, 8:64}

{char for char in 'abracadabra'}
# {'a', 'b', 'c', 'd', 'r'}

{char for char in 'hello darkness my old friend'}
# All the letters in alphabetical order.

{char for char in 'hello darkness my old friend' if char not in 'aeiou'}
# Everything except 'aeiou'

