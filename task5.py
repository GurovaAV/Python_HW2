# Реализуйте алгоритм перемешивания списка.

import random

num = int(input('Введите число: '))
my_list = list((range(-num,num+1)))
print(my_list)
random.shuffle(my_list)
print(my_list)