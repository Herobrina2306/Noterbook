import datetime
from datetime import date
import pathlib
import os , fnmatch
import operator

# Время
def time_file():
    today = date.today()
    day = str(today.day)
    month = str(today.month)
    year = str (today.year)
    now = datetime.datetime.now(datetime.timezone.utc).astimezone()
    time_format = "%H:%M:%S"
    str_time = str(f"{now:{time_format}}")
    time_format = str(day + '.' + month + '.' + year + ' ' + str_time)
    return time_format

# Новая заметка
def new_fail():
    heading0 = str(input("Введите текст заголовка: "))
    heading1 = str(heading0 + ".json")
    pyt = str("notes/" + heading1)
    text = str(input("Введите текст заметки: "))
    with open(heading1, 'w', encoding="utf-8") as f:
        f.write(time_file() + '\n \n' + heading0 + '\n \n' + text)
    os.replace(heading1, pyt) 

# Чтение
def conclusion():
    heading0 = str(input("Введите заголовок заметки, который вы хотите открыть: "))
    heading1 = str("notes/" +heading0 + ".json")
    with open(heading1, encoding="utf-8") as f:
        for line in f:
            print(line.strip())

# Добавление в заметку
def add():
    heading0 = str(input("Введите заголовок заметки, который вы хотите редактировать: "))
    heading1 = str("notes/" + heading0 + ".json")
    with open(heading1, '+a', encoding="utf-8") as f:
        new_zap = str(input("Что вы хотите добавить(добавиться в конец файла на новой строке): "))
        f.write("\n" + new_zap)
    with open(heading1, encoding="utf-8") as f:
        for line in f:
            print(line.strip())

# Удаление заметки
def delete ():
    heading0 = str(input("Введите заголовок заметки, который вы хотите удалить: "))
    heading1 = str("notes/" +heading0 + ".json")
    file = pathlib.Path(heading1) 
    file.unlink()

# Вывод каталога
def catalog ():
    l = []

    def custom_key1(l):
        return l[1]
    
    listOfFiles = os.listdir('notes')  
    pattern = "*.json"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            heading = str("notes/" + entry)    
            with open(heading) as f:
                lines = f.readlines()
            y = []
            y.append(entry)
            y.append(lines[0])
            l.append(y)
    l.sort(key = custom_key1, reverse=True)   

    res = [x[0] for x in l]
    print(*res, sep = '\n \n')



