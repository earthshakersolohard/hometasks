num_sum = 0
while True:
    my_numbers = input('Введите числа через пробел (или введите q для выхода): \n').split()
    my_symbols = ''.join(my_numbers)
    if my_symbols.isdigit():
        num_sum += sum(map(int,my_numbers))
        print(num_sum)
    elif my_symbols == 'q':
        print('Выполнение программы завершено')
        break
    else:
        print('Подумайте ещё\n')