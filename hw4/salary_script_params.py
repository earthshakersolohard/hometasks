from sys import argv
script_name, first_par, second_par, third_par = argv

print('script name', script_name)
print('work hours', first_par)
print('rate per hour', second_par)
print('bonus', third_par)
first_par = int(first_par)
second_par = int(second_par)
third_par = int(third_par)
salary = (first_par*second_par) + third_par
print(salary)