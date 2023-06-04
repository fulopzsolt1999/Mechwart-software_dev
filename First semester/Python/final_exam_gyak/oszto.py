def oszto():
    nums = []
    num = 0
    while len(nums) != 2:
        try:
            num = int(input("Adjon meg egy 0-nál nagyobb egész számot: "))
        except:
            print("Csak számok az elfogadottak! Próbálja újra!")
        finally:
            if num > 0:
                nums.append(num)
    if nums[0] % nums[1] == 0:
        print(f"Az egyik szám: {nums[0]}\nA másik szám: {nums[1]}\n{nums[0]} : {nums[1]} = {nums[0]/nums[1]}")
    elif nums[1] % nums[0] == 0:
        print(f"Az egyik szám: {nums[1]}\nA másik szám: {nums[0]}\n{nums[1]} : {nums[0]} = {nums[1]/nums[0]}")
    else:
        print(f"Az egyik szám: {nums[0]}\nA másik szám: {nums[1]}\nA két szám nem osztója egymásnak.")

if __name__ == "__main__":
    oszto()