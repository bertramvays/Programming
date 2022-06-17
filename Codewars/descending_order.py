"""
task is to make a function that can take any non-negative integer
as an argument and return it with its digits in descending order.
 Essentially, rearrange the digits to create the highest possible number.
"""
def descending_order(num):
    l = sorted(list(str(num)), reverse=True)  # преобразовую число в строку, строку в список
    print(l)                            # сортирую список
    st = l[0]                   # создаю переменную с первой цифрой
    for i in l[1:]:
        st += i
    return int(st)

"""
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
"""