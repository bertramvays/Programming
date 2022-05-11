#!/bin/python3
"""
Реализует веб-интерфейс для просмотра и изменения экземпляров классов в хранилище;
хранилище нахидиться на сервере (или на том же компьютере, если используется имя
localhost)
"""
import cgi, shelve, sys, os  # cgi.test() выведет поля ввода


shelvename = 'class-shelve'  # файлы хранилища находятся в текущем катологе
fieldnames = ('name', 'age', 'job', 'pay')
form = cgi.FieldStorage()  # парсинг данных формы
print('Content-type: text/html')  # заголовок + пустая строка для ответа
sys.path.insert(0, os.getcwd())  # благодаря этому модуль picle и сам сценарий будут
                                 # способны импортировать модуль person

# главный шаблон разметки html
replyhtml = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>People Input Form</title>
</head>
<body>
<form method="post" action="peoplecgi.py">
    <table>
        <tr><th>Key <td><input type="text" name="key" value="%(key)s"></td></th></tr>
        $ROWS$
    </table>
    <p>
        <input type="submit" value="Fetch", name="action">
        <input type="submit" value="Update", name="action">
    </p>
</form>
</body>
</html>
"""

# вставить разметку html  данными в позицию $ROWS$
rowhtml = '<tr><th>%s<td><input type="text" name=%s value="%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))
replyhtml = replyhtml.replace('$ROWS', rowshtml)

def htmlize(adict):
    new = adict.copy()  # значения могут содержать &, > и другие специальные символы,
    for field in fieldnames:   # отображаемые особым образом; их необходимо экранировать
        value = new[field]
        new[field] = cgi.escape(repr(value))
    return new


def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__  # для заполнения строки ответов использовать
        fields['key'] = key  # словарь атрибутов
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields


def updateRecord(db, form):
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]  # изменить существующую запись
        else:
            from person import Person
            record = Person(name='?', age='?')

        for field in fieldnames:
            setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields


db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fields = fetchRecord(db, form)
elif action == 'Update':
    fields = updateRecord(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')  # недопустимое значение кнопки отправки
    fields['key'] = 'Missing or invalid action!'  # формы. Заполнить форму ответа из
                                                  # словаря


db.close()
print(replyhtml % htmlize(fields))
