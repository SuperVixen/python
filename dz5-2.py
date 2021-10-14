# Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield

n = int(input('Введите число n: '))
odd_generator = (n for n in range(1, n + 1, 2))
# m = odd_generator
print(*odd_generator) #нечетные
print(odd_generator) #сам генератор
next(odd_generator) #сам генератор закончился
