p = str

while (slovo := str(input("Слово: "))) != "stop":
    if "f" in slovo:
        print("Woooow! You have a relic word")
    else:
        print("it's regular word...")