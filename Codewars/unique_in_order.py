"""
Implement the function unique_in_order which takes as argument
a sequence and returns a list of items without any elements
with the same value next to each other and preserving the
original order of elements.
"""

def unique_in_order(iterable):
    if iterable:
        lst = [iterable[0]]
        for i in iterable:
            if i != lst[-1]:
                lst.append(i)
        return lst
    else:
        return list(iterable)


