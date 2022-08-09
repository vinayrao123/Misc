"""
1. Variables
2. Loops
3. Conditions
4. Functions
5. Classes and objects
6. Dictionaries and lists
7. Generic data structures (int, char)
"""
valueDict = {"vinay": 36, "Meenakshi": 18, "Amaan": 17, "Kaushal": 12}

inputDict = [{"operator": "sum", "values": [1,2,3,4,5,6]},{"operator": "multiply", "values": [1,2,3,4,5,6]},{"operator": "sum-2,multiply-2,sum-2", "values": [1,2,3,4,5,6]}]


#[1,2,3,4,5,6], [1,2], [3,4,5]

def addition(values):
    sum = 0
    for item in values:
        sum += item
    return sum

def multiply(values):
    product = 1
    for item in values:
        product *= item
    return product

for i in range(len(inputDict)):
    if inputDict[i]["operator"] == "sum":
        print(addition(inputDict[i]["values"]))
    elif inputDict[i]["operator"] == "multiply":
        print(multiply(inputDict[i]["values"]))
    else: #"sum-2,multiply-3,sum-2,multiply-1"
        outs = inputDict[i]["operator"].split(",")
        print(outs)
        min = 0
        max = 0
        for j in range(len(outs)):
            data = outs[j].split("-")
            if data[0] == "sum":
                min = max
                max = int(data[1]) + min
                print(addition(inputDict[i]["values"][min:max]))
            elif data[0] == "multiply":
                min = max
                max = int(data[1]) + min
                print(multiply(inputDict[i]["values"][min:max]))

