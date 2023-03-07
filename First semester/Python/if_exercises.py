def get_input():
    num1 = float(input("Give me a number: "))
    num2 = float(input("Give me a number: "))
    first_ex(num1, num2)
    second_ex(num1, num2)

def first_ex(n1, n2):
    if n1==0 or n2==0:
        print("Can not devide with 0.")
    else:
        print(n1/n2)
    
def second_ex(n1, n2):
    print(n1>n2 and f"{n1/n2:.2f}" or f"{n2/n1:.2f}")

def third_ex():
    num = float(input("Give me the water's temperature: "))
    print(num>=100 and "The water is in steam state" or num>0 and "The water is in liquid state" or "The water is in solid state")

def fourth_ex():
    num = int(input("Give me the result: "))
    result = num/150*100
    print(result>=80 and "5" or result>=60 and "4" or result>=40 and "3" or result>=25 and "2" or "1")

def fifth_ex():
    price = float(input("Give me the product's price: "))
    sale = int(input("Give me the sale(%): "))
    print(f"The product's new price is: {price*(sale/100):.2f}")
    print(sale>=50 and "It is worth to buy!" or "It is not worth to buy")

def sixth_ex():
    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me a number: "))
    num3 = int(input("Give me a number: "))
    
    if num1>num2 and num1>num3:
        print(f"The max num is: {num1}")
    elif num2>num1 and num2>num3:
        print(f"The max num is: {num2}")
    else:
        print(f"The max num is: {num3}")

def seventh_ex():
    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me a number: "))
    num3 = int(input("Give me a number: "))
    
    if num2<=num1>=num3:
        if num2>=num3:
            return num1, num2, num3
        else:
            return num1, num3, num2
    elif num1<=num2>=num3:
        if num1>=num3:
            return num2, num1, num3
        else:
            return num2, num3, num1
    elif num2<=num3>=num1:
        if num1>=num2:
            return num3, num1, num2
        else:
            return num3, num2, num1

def eighth_ex(nums):
    if nums[1]+nums[2] > nums[0]:
        K = nums[0]+nums[1]+nums[2]
        T = (K*(K-nums[0])*(K-nums[1])*(K-nums[2]))**0.5
        right_angle = nums[0]^2==nums[1]^2*nums[2]^2
        print(f"District: {K}, Area: {T:.2f}, \nIs this right triangle? {right_angle}")
    else:
        print("Can not make a triangle!")

def ninth_ex():
    year = int(input("Give me the year: "))
    
    if year%4==0 and year%100!=0 or year%400==0:
        print("The year is leap year.")
    else:
        print("The year is not leap year.")

def tenth_ex():
    num = input("Give me the code: ")
    if int(num[0])%2==0:
        if int(num[1])%2==0:
            print("You can enter to the first room.")
        else:
            print("You can enter to the second room.")
    elif int(num[1])%2 == 0:
            print("You can enter to the third room.")
    else:
        print("You can enter to the forth room.")

if __name__ == "__main__":
    #get_input()
    #third_ex()
    #fourth_ex()
    #fifth_ex()
    #sixth_ex()
    #three_num = seventh_ex()
    #print(three_num)
    #eighth_ex(three_num)
    #ninth_ex()
    tenth_ex()