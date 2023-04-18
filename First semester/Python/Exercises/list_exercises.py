import random as r

def rand_numbers():
    randList = []
    for _ in range(20):
        randList.append(r.randint(-20, 25))
    return randList

def print_list(nl):
    for n in nl:
        print(n, end=" ")
    print("\n")

def negative_nums(nl):
    for n in nl:
        if n < 0:
            print(n, end=" ")
            
def positive_even_nums(nl):
    for n in nl:
        if n >= 0 and n % 2 == 0:
            print(n, end=" ")
            
def first_last_element(nl):
    print(f"First item: {nl[0]}\nLast item: {nl[-1]}")
        
def every_second_item(nl):
    for i in range(len(nl)):
        if i % 2 != 0 and i != 0:
            print(nl[i], end=" ")

def min_max_index(nl):
    print(f"""
        Minimum number index: {nl.index(min(nl))} Minimum number value: {min(nl)}\n
        Maximum number index: {nl.index(max(nl))} Maximum number value: {max(nl)}
        """)

def check_next_item(nl):
    for i in range(len(nl)):
        if i < len(nl) - 1:
            if nl[i] < nl[i+1]:
                print(nl[i], end=" ")

def check_input(nl):
    while True:
        try:
            inputNum = int(input("Give me a number (-20 - 25): "))
        except:
            print("Wront input type!\nTry again!\n")
        else:
            break
    count = 0
    indexes = []
    for i in range(len(nl)):
        if nl[i] == inputNum:
            count+=1
            indexes.append(i)
    print(f"\nI found your input number this many time: {count}\nThe indexes are: {indexes}")

def sum_avr(nl):
    print(f"\nAll element sum: {sum(nl)}\nAll element avr: {sum(nl)/len(nl)}")
    
def absolute(nl):
    for i in range(len(nl)):
        if nl[i] < 0:
            nl[i] = abs(nl[i])
        print(nl[i], end=" ")
        
def in_fixed_interval(nl):
    for n in nl:
        if -5 <= n <= 5:
            print(n, end=" ")
            
def out_fixed_interval(nl):
    for n in nl:
        if -5 >= n >= -10:
            continue
        else:
            print(n, end=" ")
            
def swap_order(nl):
    print(nl[::-1])
    
def swap_first_last(nl):
    nl[0], nl[-1] = nl[-1], nl[0]
    print(nl)
    
def neighbour_num_sum(nl):
    for i in range(len(nl)):
        if i < len(nl) - 1:
            if nl[i] + nl[i+1] == 0:
                nl[i], nl[i+1] = 0, 0
        print(nl[i], end=" ")
        
def check_same_neighbour(nl):
    count = 0
    for i in range(len(nl)):
        if i < len(nl) - 1:
            if nl[i] == nl[i+1]:
                count+=1
    print(f"I found {count} same number side by side.")
    
def check_sum_neighbours(nl):
    for i in range(len(nl)):
        if i < len(nl) - 1 and i != 0:
            if nl[i] == nl[i-1] + nl[i+1]:
                print(f"I found {nl[i]} = {nl[i-1]} + {nl[i+1]}")
        
if __name__ == "__main__":
    numList = rand_numbers()
    print_list(numList)
    #negative_nums(numList)
    #positive_even_nums(numList)
    #first_last_element(numList)
    #every_second_item(numList)
    #min_max_index(numList)
    #check_next_item(numList)
    #check_input(numList)
    #sum_avr(numList)
    #absolute(numList)
    #in_fixed_interval(numList)
    #out_fixed_interval(numList)
    #swap_order(numList)
    #swap_first_last(numList)
    #neighbour_num_sum(numList)
    #check_same_neighbour(numList)
    check_sum_neighbours(numList)