import random as r

def random_number_generator():
    numList = []
    count = 0
    while count < 20:
        genNum = int(r.random()*100)
        if genNum not in numList and genNum >= 10:
            numList.append(genNum)
            count += 1
    odd_even_numbers(numList)
    
def odd_even_numbers(numList):
    oddNums = []
    evenNums = []
    for num in numList:
        if num % 2 == 0:
            evenNums.append(num)
        else:
            oddNums.append(num)
    print(f"""
          A listában a {len(evenNums)} páros szám közül a legnagyobb: {max(evenNums)}\n
          A listában a {len(oddNums)} páros szám közül a legnagyobb: {max(oddNums)}
          """)

if __name__ == "__main__":
    random_number_generator()