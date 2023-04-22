def infinite_input():
    firstNum = input_debugger()
    numList = []
    count = 0
    numList.append(firstNum)
    while True:
        otherNum = input_debugger()
        if otherNum < numList[count]:
            break
        else:
            count += 1
            numList.append(otherNum)
    print(f"\nA megadott {len(numList)} szám átlaga {round(sum(numList)/len(numList),3)}\n")

def input_debugger():
    while True:
        try:
            inpNum = float(input("Give me a number: "))
        except:
            print("\nWrong input!\nPlease try again!\n")
        else:
            return inpNum

if __name__ == "__main__":
    infinite_input()