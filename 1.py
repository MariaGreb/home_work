str_var = "hello, how are you!?"
char_count = 0
char_index_list = []
char_find = input('Введите букву: ')
for index, char in enumerate(str_var):
    if char == char_find:
        char_index_list.append(index)
        char_count += 1
print(f"На {char_index_list} месте стоит {char_find} символ")



# str_var = "hello, how are you!?"
# char_count = 0
# char_find = input('Введите букву: ')
# for char in str_var:
#   if char == char_find:
#     char_count += 1
# print(f'Количество = {char_count}')
#
#
# str_var = "hello, how are you!?"
# char_count = 0
# for char in str_var:
#     if char == 'o':
#         char_count += 1
# print(f"Количество = {char_count}")
#
#
#
# str_var = "hello, how are you!?"
# char_count = 0
# check = int(input('Введите букву: '))
# for char in str_var:
#     if char == check:
#         char_count += 1
# print(f"Количество = {char_count}")