def get_input():
    x = int(input("Give me a number: "))
    positive_or_negative(x)

def positive_or_negative(x):
    print("The number is 0." if x==0 else "The number is positive." if x>0 else "The number is negative.")   
    print(x==0 and "The number is 0." or x>0 and "The number is positive." or "The number is negative.")
    
if __name__ == "__main__":
    get_input()