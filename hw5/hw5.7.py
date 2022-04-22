import json

l_dict2 = []

with open('hw5.7.txt', 'r', encoding='utf-8') as my_f:
    prof_dict = []
    for line in my_f:

        sp_line = line.split()
        profit = int(sp_line[2]) - int(sp_line[3])
        if profit > 0:
            prof = 'прибыль'
            prof_dict.append(profit)
        else:
            prof = 'убыток'
        print(f'{sp_line[1]} {sp_line[0]} - выручка: {sp_line[2]}, издержки: {sp_line[3]}, {prof}: {profit}')
    print(f'Средняя прибыль фирм: {sum(prof_dict) / len(prof_dict)}')

with open('hw5.7.txt', 'r', encoding='utf-8') as my_f:
    for line in my_f:
        sp_line = line.split()
        l_dict2.append({sp_line[0]: int(sp_line[2]) - int(sp_line[3])})
    l_dict2.append({'avg_prof': sum(prof_dict) / len(prof_dict)})
    print(l_dict2)

with open('my_file.json', 'w', encoding='utf-8') as f_json:
    json.dump(l_dict2, f_json)