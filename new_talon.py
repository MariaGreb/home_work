from random import randint

print ('Добрый день! Оформление записи к врачу:')
first_name = input('Введите свое имя: ')
last_name = input('Введите вашу фамилию: ')
age = input('Введите возраст: ')
wt = input('Введите вес: ')
comment = input('Комментарии: ')

number = randint(0, 100)
print(last_name,' ', first_name, ', вы назначены к врачу.\nВаш талон № ', number, sep='')
print(last_name + ' ' + first_name + ', вы назначены к врачу.\nВаш талон № ' + str(number))
print(f'{last_name} {first_name}, вы назначены к врачу.\nВаш талон № {number}')





