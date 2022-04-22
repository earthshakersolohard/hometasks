with open('hw5.2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, f'Слов в строке: {len(line.split())}', end='')
        print()