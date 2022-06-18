"""
Write a function that will return the count of distinct
 case-insensitive alphabetic characters and numeric digits
 that occur more than once in the input string.
 The input string can be assumed to contain only
  alphabets (both uppercase and lowercase) and numeric digits.
"""
from collections import Counter

def duplicate_count(text):
    count = 0
    s_low = text.lower()
    counts = Counter(s_low)
    for i in counts:
        if counts[i] > 1:
            count += 1
    return count

"""
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
     
"""