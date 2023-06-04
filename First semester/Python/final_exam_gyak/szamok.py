def szamok():
    pozNums = []
    negNums = []
    while True:
        try:
            inp = int(input("A szám: "))
        except:
            print("Csak számok az elfogadottak! Próbálja újra!")
        finally:
            if inp > 0:
                pozNums.append(inp)
            elif inp < 0:
                negNums.append(inp)
            else:
                break
    print("Pozitív számok:", *pozNums, sep="\t")
    print("Negatív számok:", *negNums, sep="\t")
    print(f"A számok összege: {sum(pozNums)+sum(negNums)}")
    print(f"A számok átlaga: {(sum(pozNums)+sum(negNums)/len(pozNums)+len(negNums)):.2f}")
    
if __name__ == "__main__":
    szamok()