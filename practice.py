

with open("list.txt") as f:
    lines = f.readlines

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter the amount: \n"))
print("Enter the name of the currency you want to convert: ")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of thse values: \n")
print(
    f"{amount} USD is equal to {amount*float(currencyDict[currency])} {currency} ")
