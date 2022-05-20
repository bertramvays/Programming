"""
Пример программы завершения программы с помощью модуля sys
"""

def later():
    import sys
    print('Bye sys world')
    sys.exit(111)
    print('Never reached')


if __name__ == '__main__': later()