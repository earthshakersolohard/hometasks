revenue=float(input("enter firm`s revenue "))
costs=float(input("enter firm`s costs "))
profit=revenue-costs
if profit > 0:
    print("firm is profitable")
elif profit == 0:
    print("firm goes without profit")
else:
    print("firm is unprofitable")