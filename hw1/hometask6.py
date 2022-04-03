revenue=float(input("enter firm`s revenue "))
costs=float(input("enter firm`s costs "))
profit=revenue-costs
profitability= round(profit / revenue, 2)

if profit > 0:
    print("firm is profitable")
    print(f"profitability: {profitability}")
    size_staff = int(input("enter staff quantity "))
    efect = round(profit / size_staff, 2)
    print(f"profit per person: {efect}")
elif profit == 0:
    print("firm goes without profit")
else:
    print("firm is unprofitable")