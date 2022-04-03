a = float(input("1st day`s result "))
b = int(input("amount of kms wanted "))
num_day = int(1)

if a >= b:
    print("wish is granted")

while a <= b:
    a = a*1.1
    num_day = num_day + 1
    print(f"{num_day}-th day: {a}")

print(f"At {num_day}-th day you`ll get {b}")
