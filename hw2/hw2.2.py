my_list = []
len_my_list = int(input('enter number of elements: '))
num_my_list = 1

while num_my_list <= len_my_list :
    el_list = input(f'Enter {num_my_list} element of list: ')
    my_list.append(el_list)
    num_my_list += 1
print(my_list)

my_list[0], my_list[1] = my_list[1], my_list[0]
my_list[2], my_list[3] = my_list[3], my_list[2]

print(my_list)