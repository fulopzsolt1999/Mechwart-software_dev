def get_input():
    data1 = input("Give me a number: ")
    data2 = input("\nGive me a number: ")
    operator = input("\nGive me an operator: ")
    
    odds_even(int(data1), int(data2))
    take_actions(float(data1), float(data2), operator)

def odds_even(d1, d2):
    if d1 % 2 == 0:
        print("Num1 is even")
    else:
        print("Num1 is odds")
    if d2 % 2 == 0:
        print("Num2 is even")
    else:
        print("Num2 is odds")

def take_actions(d1, d2, o):
    if o == "+":
        print(f"Addiction: {d1 + d1}")
    elif o == "-":
        print(f"Subtraction: {d1 - d1}")
    elif o == "*":
        print(f"Multiplication: {(d1 * d2):.3f}")
    elif o == "/":
        print(f"Division: {d1 / d1}")
    elif o == "%":
        print(f"Modulus: {d1 % d1}")
    elif o == "**":
        print(f"Exponentiation: {(d1 ** d1):.3f}")
    elif o == "//":
        print(f"Floor division: {d1 // d1}")
    else:
        print("Wrong o! Try again!\n")        
    
if __name__ == "__main__":
    get_input()