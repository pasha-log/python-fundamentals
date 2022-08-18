# 1. For a list of words, print out each word on a separate line, 
# but in all uppercase. How can you change a word to uppercase? 
# Ask Python for help on what you can do with strings!

greetings = ["hello", "hey", "goodbye", "yo", "yes"]

for greet in greetings:
    print(greet.upper())

# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

def print_upper_words(array):
    """Accepts an array of words, and converts all of them to uppercase.
    For example:
    ["hello", "hey", "goodbye", "yo", "yes"] becomes

    HELLO
    HEY
    GOODBYE
    YO
    YES

    """
    for greet in greetings:
        print(greet.upper())

# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

words = ["sup", "existential", "exactly", "wow"]

def print_upper_words_starting_with_e(array):
    for word in array:
        if word.startswith("e"):
            print(word.upper())

print_upper_words_starting_with_e(words) 

# Make your function more general: you should be able to pass in a set of letters, 
# and it only prints words that start with one of those letters.
# For example:

# this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})

def print_upper_words_more_generally(array, must_start_with={}):
    for word in array:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

print_upper_words_more_generally(greetings, must_start_with={"h", "y"})
