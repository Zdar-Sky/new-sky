#Присваивание переменной значение строки
s1 = 'hello'
number = 741
s2 = str(number)
print(type(s2))

#Склейка строк
s1 = 'hello'
s2 = 'world'
s3 = s1 + ' ' + s2 #Можно так вклеивать и пробел, любой символ
print(s3)

s3 = s1 * 10 #Дублирование строки то есть выведется 10 раз
print(s3)

if s1 in s3: #Оператор in проверяет входит ли данная строка в эту подстроку
    print(True)
else:
    print(False)

s1 = 'a'
if s1 == 'a' or s1 == 'b' or s1 == 'c' or s1 == '1': #Поиск символа в строке
    print(True)
else:
    print(False)

s1 = 'a'
if s1 in 'adcdegf1': #Упрощаем код с помощью оператора in
    print(True)
else:
    print(False)

s1 = 'inform'
print(s1[2], s1[-2]) #Поиск символа с помощью индекса

s1 = 'inform'
print(s1[2:5:1]) #Срез строки от 2 индекса до 5 с шагом 1 -for-

s1 = 'inform'
print(s1[:5:1]) #Срез строки от 0 индекса до 5 с шагом 1 -infor-

s1 = 'inform'
print(s1[:]) #Срез строки от 0 индекса до Последнего с шагом 1 -inform-