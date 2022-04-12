def int_func(*args):
    args = str(args)
    if args.islower() and args.isascii():
        print (args.title())
    else:
        print('Введите слово только из латинских букв в нижнем регистре')


if __name__ == "__main__":
    int_func('google', 'helicopter', 'newspaper')

words = input('Введите слова через пробел состоящие из латинских букв в нижнем регистре: ')

int_func(words)