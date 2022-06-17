"""
Digital root is the recursive sum of all the digits in a number.
If that value has more than one digit, continue reducing in this way
until a single-digit number is produced.
"""
def digital_root(n):
    lst = [int(i) for i in list(str(n))]
    if len(lst) > 1:
        result = sum(lst)
        digital_root(result)
    else:
        result = lst[0]
    return result




digital_root(132189)