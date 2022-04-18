# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)


my_list = ['never', 'gonna', 'give', 'you', 'up']
i = 1
for el in cycle(my_list):
    if i > 9:
        break
    print(el)
    i += 1
