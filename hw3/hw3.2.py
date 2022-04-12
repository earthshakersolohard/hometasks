def my_func2(*args):
    b = list(args)
    b.sort()
    b.reverse()
    return print(sum([b[0], b[1]]))