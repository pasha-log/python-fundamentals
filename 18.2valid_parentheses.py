def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """ 
    if parens[0] == '(' and parens[len(parens)-1] == ')' and len(parens) % 2 == 0:
        return True 
    else:
        return False 

    # Or:
    # count = 0

    # for p in parens:
    #     if p == '(':
    #         count += 1
    #     elif p == ')':
    #         count -= 1

    #     # fast fail: too many right parens
    #     if count < 0:
    #         return False

    # return count == 0