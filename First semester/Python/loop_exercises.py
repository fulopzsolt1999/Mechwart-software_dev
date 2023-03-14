import random as r

def first():
    getnum = int(input("Give me a number: "))
    for i in range(getnum+1):
        print(i)

def second():
    getnum1 = int(input("Give me a number: "))
    getnum2 = int(input("Give me a number: "))
    for i in range(getnum1, getnum2+1):
        print(i)

def third():
    for i in range(10, 20+1):
        print(i, i*i)

def fourth():
    for i in range(0, 100+1):
        if i%7==0:
            print(i)

def fifth():
    for i in range(0, 100+1):
        if i % 7 == 0:
            if 100 - i < 7:
                print(i)
            else:
                print(i, end=", ")
        
def sixth():
    for i in range(10, 100+1):
        if i**0.5*10%10 == 0:
            print(i)

def seventh():
    getnum1 = int(input("Give me a number: "))
    getnum2 = int(input("Give me a number: "))
    for i in range(getnum1, getnum2+1):
        if i%6 == 0:
            print(i)
            
def eighth():
    getnum1 = int(input("Give me a number: "))
    getnum2 = int(input("Give me a number: "))
    if getnum1 < getnum2:
        for i in range(getnum1, getnum2+1):
            if i % 6 == 0:
                print(i)
    else:
        for i in range(getnum2, getnum1+1):
            if i % 6 == 0:
                print(i)
                
def ninth():
    result = 0
    for _ in range(5):
        getnum = int(input("Give me a number: "))
        result+=getnum
    print(result)
    
def tenth():
    result = 0
    for _ in range(5):
        getnum = int(input("Give me a number: "))
        if result < getnum:
            result = getnum
    print(result)
    
def eleventh():
    getnum = int(input("Give me a number: "))
    for i in range(1, getnum+1):
        if getnum%i == 0:
            print(i)    

def twelveth():
    getnum = int(input("Give me a number: "))
    if getnum > 1:
        for i in range(2, getnum):
            if getnum%i == 0:
                print(f"{getnum} is not prime")
                break
        else:
            print(f"{getnum} is prime")

def thirteenth():
    getnum = int(input("Give me a number: "))
    result = 0
    for i in range(1, getnum+1):
        if getnum % i == 0:
            result+=i
    print(result)

def fourteenth():
    getnum1 = int(input("Give me a number: "))
    getnum2 = int(input("Give me a number: "))
    result = 0
    if getnum1 < getnum2:
        for i in range(getnum1, getnum2+1):
            result+=i
    else:
        for i in range(getnum2, getnum1+1):
            result+=i
    print(result)
    
def fifteenth():
    getnum1 = int(input("Give me a number: "))
    dice = []
    for i in range(getnum1):
        dice.append(r.randint(1, 6))
        print(dice[i])
    print(f"Avg.: {sum(dice)/len(dice)}")
    
def sixteenth():
    getnum1 = int(input("Give me the start number: "))
    getnum2 = int(input("Give me the difference: "))
    getnum3 = int(input("Give me how many element you want: "))
    for i in range(getnum3):
        if i == getnum3-1:
            print(getnum1)
        else:
            print(getnum1, end=", ")
        getnum1+=getnum2

def seventeenth():
    getnum1 = int(input("Give me how many times you want to play: "))
    lst = ["head", "tail"]
    headc = 0
    tailc = 0
    for _ in range(getnum1):
        if r.choice(lst) == "head":
            headc+=1
        else:
            tailc+=1
    print(f"Heads: {headc}\tTails: {tailc}")

def eighteenth():
    getnum1 = int(input("Give me how many times you want to play: "))
    lst = ["head", "tail"]
    for _ in range(getnum1):
        getans = input("Give me a guess (h-head, t-tail): ")
        if r.choice(lst) == "head" and getans == "h":
            print("You guessed head and it was correct!")
        elif r.choice(lst) == "tail" and getans == "t":
            print("You guessed tail and it was correct!")
        else:
            print("Your guess was incorrect!")

def nineteenth():
    getnum = int(input("Give me a number: "))
    for i in range(2, getnum+1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
        if prime:
            print(i)

def twentyth():
    getnum = int(input("Give me a number: "))
    lst = []
    for i in range(getnum, 101):
        if i % getnum == 0:
            lst.append(i)
    lst.sort(reverse=True)
    print(lst)
    
def twentyfirst():
    getnum = int(input("Give me a number (0-10): "))
    result = 0
    while True:
        if 0 < getnum <= 10:
            result += getnum
            getnum = int(input("Give me a number: "))
        else:
            break
    print(f"All 0-10 numbers sum is: {result}")
    
def twentysecond():
    getnum = int(input("Give me a number: "))
    n = getnum
    dev2 = ""
    while n % 2 == 0:
        n /= 2
        dev2 += "2*"
        rem = n
    print(f"{getnum} = {dev2}{int(rem)}")

def twentythird():
    getnum = int(input("Give me a number: "))
    result = getnum
    count = 0
    while result >= 3:
        result-=3
        count+=1
    if getnum%3 != 0:
        print(f"{getnum} = {count}*3+{getnum%3}")
    else:
        print(f"{getnum} = {count}*3")
    
def twentyfourth():
    rnum = r.randint(1,100)
    gnum = int(input("Guess a number (0 if you want to quit): "))
    count = 1
    while gnum != rnum:
        if gnum < rnum:
            print("The number to be guessed is higher!")
        elif gnum == 0:
            print("You quited!")
        else:
            print("The number to be guessed is lower!")
        gnum = int(input("Guess a number (0 if you want to quit): "))
        count += 1
    print(count)
    
def twentyfifth():
    lst = ["r", "p", "s"]
    mypoints = 0
    mpoints = 0
    while True:
        relement = r.choice(lst)
        gword = input("Give me rock(r)/paper(p)/scissors(s): ")
        if gword == relement:
            print(f"Draw this round! Mypoints: {mypoints} Enemy points: {mpoints}")
        elif (gword == "r" and relement == "s") or (gword == "s" and relement == "p") or (gword == "p" and relement == "r"):
            mypoints += 1
            if mypoints < 5:
                print(f"Win this round! Mypoints: {mypoints} Enemy points: {mpoints}")
            elif mypoints == 5:
                print(f"Congratulations you won! Mypoints: {mypoints} Enemy points: {mpoints}")
                break
        else:
            mpoints += 1
            if mpoints < 5:
                print(f"Lose this round! Mypoints: {mypoints} Enemy points: {mpoints}")
            elif mpoints == 5:
                print(f"Poor you, you lost! Mypoints: {mypoints} Enemy points: {mpoints}")
                break
        
if __name__ == "__main__":
    #first()
    #second()
    #third()
    #fourth()
    #fifth()
    #sixth()
    #seventh()
    #eighth()
    #ninth()
    #tenth()
    #eleventh()
    #twelveth()
    #thirteenth()
    #fourteenth()
    #fifteenth()
    #sixteenth()
    #seventeenth()
    #eighteenth()
    #nineteenth()
    #twentyth()
    #twentyfirst()
    #twentysecond()
    #twentythird()
    #twentyfourth()
    twentyfifth()