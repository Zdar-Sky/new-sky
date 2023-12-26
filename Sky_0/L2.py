# Подключаем модуль текущей даты
import datetime
today = datetime.date.today()
current_year = today.year

# Вводим основные данные имя год рождения
my_name = input('Введите свое имя: ')
year_of_birth = input('Введите свой год рождения: ')

# Вычисляем возраст
age = current_year - int(year_of_birth)

# Выводим на экран переменный имя и год рождения И возраст
print(my_name)
print(year_of_birth)
print(age)

# Выводим на экран надпись с именем и возрастом да
print('Привет, меня зовут ', my_name, 'я родился в', year_of_birth, 'и мне', age, 'лет.')