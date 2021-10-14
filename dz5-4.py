### 4. Представлен список чисел. Необходимо вывести те его элементы, значения
# которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#это классика, код тоже рабочий.
# result = []
# b = src[0]
#
# for i in range(1, len(src)):
#     if src[i] > b:
#         result.append(src[i])
#     b = src[i]
#
# print(result)
# end of classic

# try with comprehensions
result = [src[n] for n in range(1, len(src)) if src[n] > src[n-1]]
print(result)




