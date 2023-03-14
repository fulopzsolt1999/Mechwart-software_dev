import random as r

def random_number():
    rnum = []
    getnum = int(input("How many numbers do you want? "))
    minnum = int(input("Give me a minimum number: "))
    maxnum = int(input("Give me a minimum number: "))
    for _ in range(getnum):
        rnum.append(r.randint(minnum, maxnum))
    print(f"All number: {rnum}\nAvr: {sum(rnum)/getnum}")

def game():
    lst = ["rock", "paper", "scissors"]
    relement = r.choice(lst)
    print(f"\n{relement}\n")

if __name__ == "__main__":
    #random_number()
    game()
