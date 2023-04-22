def mid_input():
    inpList = []
    for _ in range(3):
        while True:
            try:
                inpNum = int(input("Give me an positive integer number: "))
            except:
                print("\nWrong input!\nPlease try again!\n")
            else:
                inpList.append(inpNum)
                break
    inpList.sort()
    print(f"\nA 2. legnagyobb megadott szám: {inpList[1]}\n")

if __name__ == "__main__":
    mid_input()