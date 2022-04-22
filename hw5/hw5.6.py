subject = {}
with open("hw5.6.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.replace("-", "0").replace(":", "").replace("(l)", "").replace("(pr)", "").replace("(sem)", "")
        subject[line.split()[0]] = sum(map(int, line.split()[1:]))
        print(f"total hours: \n{subject}")
