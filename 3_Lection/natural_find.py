try:
    value = float(input('Введите до какого числа: '))
except Exception as e:
    print('Не удалось преобразить в число')
    exit ()

max_value = int(input('Введите до какого числа: '))
values_sum = 0
for value in range  (max_value):
    if value % 3 ==0 or value % 5 ==0:
        values_sum += value

    if value % 3 ==0 and value % 5 ==0:
        values_sum += value

print(values_sum)

