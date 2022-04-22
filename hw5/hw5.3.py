explo_dict = {}
sal_sum = 0

with open('hw5.3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        my_key = (line.split())[0]
        my_val = float((line.split())[1])
        explo_dict[my_key] = my_val

print('Меньше 20-ти тысяч получают:')
for key, value in explo_dict.items():
    if value < 200000:
        print(key)
    sal_sum += value

print(f'Средняя зарплата в фирме: {sal_sum / len(explo_dict)} тенге.')