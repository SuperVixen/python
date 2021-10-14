# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

def odd_generator_with_yield(n):
    for i in range(1, n + 1, 2):
        yield i
    # return 'exaust'

n = int(input('Введите число n: '))
odd_numbers = odd_generator_with_yield(n)
print(*odd_numbers)

print(odd_generator_with_yield(n))#показываю что это генератор
next(odd_numbers)# и что он закончился




