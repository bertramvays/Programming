def am_i_wilson(n):
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False

        import math
        wil_num = (math.factorial(n - 1) + 1) / (n * n)
        if wil_num % 1 == 0:
            return True



print(am_i_wilson(8))
print(am_i_wilson(5))
