# Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2

examples = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
for i in range(0, len(examples)):
    print('Тип результата: ', examples[i], type(examples[i]))
