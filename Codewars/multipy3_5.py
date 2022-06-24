"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5
below the number passed in. Additionally, if the number is negative, return 0

Note: If the number is a multiple of both 3 and 5, only count it once.
"""
"""
def solution(number):
    if number < 0:
        return 0
    else:
       return sum([i for i in range(0, number) if i % 3 == 0 or i % 5 == 0])

    """
    #итересное с кодварс но у меня не работает
"""        
def solution(number):
    threes = range(3, number, 3)
    fives = range(5, number, 5)
    return sum(list(set(threes + fives)))


solution(10)
"""