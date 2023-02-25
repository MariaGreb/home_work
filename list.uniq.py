numbers_list = [1, 5, 4, 3, 5, 6, 7, 4, 5, 6, 7, 5, 4, 3, 5, 4, 3, 2, 5, 4, 5, 9, 0, 4, 3, 7, 0, 9, 5, 0, 3, 5, 4, 3, 6, 4]
numbers_set = set(numbers_list)
print(numbers_set)

numbers_2 = range(10)
numbers_2_set = set(numbers_2)
set_1 = numbers_2_set - numbers_set

print(set_1)


list_1 = list(range(400))
print(list_1)
print(list_1[100:300:7])

list_2 = list_1[100:300:7]
print(list_2[-1:-6:-1])