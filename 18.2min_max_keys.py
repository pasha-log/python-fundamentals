def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """ 
    keys = []
    for key in d.keys():
        keys.append(key)
        keys.sort()
    return tuple([keys[0], keys[len(keys)-1]])

    # Or:
    # keys = d.keys()

    # return (min(keys), max(keys))
