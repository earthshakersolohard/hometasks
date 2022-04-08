num = int(input('enter month`s number '))
if num < 1 or num > 12:
    print('Error')
    num = int(input('enter month`s number '))

season = {12: 'winter', 1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer',
          7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn'}

print(season.get(num))
