# Подключаем модуль времени
import time

# Выводим на экран текущее время
current_time = time.strftime("%H:%M:%S", time.localtime())
print("Текущее время:", current_time)

# Задаем перемену часа с момента начала дня
current_time_hour = time.strftime("%H", time.localtime())

# Создаем переменную минуты с момента начала часа
current_time_min = time.strftime("%M", time.localtime())

# Подсчитываем сколько прошло минут с момента начала дня И выводим на экран
S_min = int(current_time_hour) * 60 + int(current_time_min)
print('С момента начала дня прошло', S_min, 'Минут')

# Подсчитываем сколько прошло часов И минут через Сумму минуты И выводим на экран
time_h = S_min // 60
time_m = S_min % 60
print('Сначала дня прошло ', time_h, 'Часов ', 'и ', time_m, 'Минут ' )