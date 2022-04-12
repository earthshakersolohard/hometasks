def my_func(x, y):
    try:
        if y > 0:
            y = y * -1
        return print(abs(x) ** y)
    except ZeroDivisionError:
        return


my_func(2, 3)