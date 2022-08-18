# My attempt at solution:
# import random
# class WordFinder:
#     """Word Finder: finds random words from a dictionary."""
#     def __init__(self, file):
#         """Counts the amount of words in file"""
#         self.file = file
#         f = open(self.file, 'r')
#         count = 0
#         for word in f:
#             count += 1
#         print(f"{count} words read")
#         f.close()
#     def random(self): 
#         """Selects a random word from file"""
#         f = open(self.file, 'r')
#         for x in range(0,random.randint(0,235886)):
#             word = f.readline(x).strip()
#         return word

# import re
# class SpecialWordFinder(WordFinder):
#     def __init__(self, file):
#         super().__init__(self, file)
#         self.file = file
#         with open("self.file", "r") as f:
#             for line in f:
#                 line = line.rstrip()
#                 if line:
#                     if not re.match(r'\s*#', line):
#                         file.write(line)
                        
"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]