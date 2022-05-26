"""
Отыскивает наибольший файл с исходным кодом на языке Пайтон в дереве каталогов.
Поиск выполняется в каталоге стандартной библиотеке, отображение результатов выполняется с
с помощью модуля pprint.
"""
import sys, os, pprint
trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Python31\Lib'  # Windows
else:
    dirname = '/lib/python3/'  # Unix

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
