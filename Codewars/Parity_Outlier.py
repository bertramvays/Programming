"""
You are given an array (which will have a length of at least 3,
 but could be very large) containing integers. The array is either
 entirely comprised of odd integers or entirely comprised of even
 integers except for a single integer N. Write a method that takes
 the array as an argument and returns this "outlier" N
"""

def find_outlier(integers):
    l = [integers[0] % 2, integers[1] % 2, integers[2] % 2]
    if (not l[0] and not l[1]) or (not l[0] and not l[2]) or (not l[1] and not l[2]):
        for i in integers:
            if i % 2  != 0:
                return i
    else:
        for i in integers:
            if not i % 2:
                return i

"""
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
"""
