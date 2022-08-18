def number_counter(lst):
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1 
    return count

def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """ 
    counted = number_counter(nums)
    for key in counted.keys():
        if counted[key] > 1:
            return key
        
# Or: 
    # seen = set()

    # for num in nums:
    #     if num in seen:
    #         return num
    #     seen.add(num)
