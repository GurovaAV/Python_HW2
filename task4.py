# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся через пробел в одной строкой.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# '0 2 4'
# res -> 3

num = int(input('Введите число: '))
my_list = list((range(-num,num+1)))
print(my_list)
input_pos = input('Введите нужные позиции через пробел: ')
positions = input_pos.split(' ')            # разделяем введенные значения 
int_positions = list(map(int,positions))    # конвертируем строковые значения списка в целочисленные
multiply = 1
for i in int_positions:
    multiply *= my_list[i]
print("res ---> ",multiply)