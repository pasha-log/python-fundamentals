def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}

        get(self, key, default=None, /)
    Return the value for key if key is in the dictionary, else default.
    """
    result = {}
    for ltr in phrase:
        result[ltr] = result.get(ltr, 0) + 1 

    return result
