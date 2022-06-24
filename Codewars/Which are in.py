"""
Given two arrays of strings a1 and a2 return a sorted array r in
lexicographical order of the strings of a1 which are substrings of
strings of a2.
"""
def in_array(array1, array2):
    # your code
    l = []
    for ar1 in array1:
        for ar2 in array2:
            if ar1 in ar2:
                l.append(ar1)
                break
    return sorted(set)

"""
def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})
    
def in_array(a1, a2):
    return sorted({w for w in a1 if w in "".join(a2)})
"""
