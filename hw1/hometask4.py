digit = 0

while digit <= 0:
    digit = int(input("enter your number: "))
max_digit = digit % 10
digit = digit // 10

while digit > 0:
    next_digit = digit % 10
    digit = digit // 10
    if max_digit < next_digit:
        max_digit = next_digit

print(max_digit)