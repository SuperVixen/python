#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
#duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
#* в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Введите продолжительность в секундах: '))

day = duration // 86400
duration = duration % 86400
hour = duration//3600
duration = duration % 3600
minutes = duration //60
duration = duration % 60

print('Продолжителность: ', day, 'дней', hour, 'часов', minutes, 'минут', duration, 'секунд')