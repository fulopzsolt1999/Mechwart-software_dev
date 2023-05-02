import random as r

def open_file():
    with open("Exercises/file.txt", "r") as f:
        f.seek(0)
        text = f.read()
    return text

def text_input():
    txt = input("Write some words: ")
    return txt
        
def case_sensitive(text):
    inpChar = input("Give me a character: ")
    count = 0
    for word in text:
        if inpChar == word:
            count += 1
    print(f"A bekért karakterből ({inpChar}) találtam {count} a szövegben.")
    
def not_case_sensitive(text):
    inpChar = input("Give me a character: ")
    count = 0
    for word in text:
        if inpChar.lower() == word.lower():
            count += 1
    print(f"A bekért karakterből ({inpChar}) találtam {count} a szövegben.")

def space_remover():
    textInp = text_input()
    print(textInp.replace(" ", ""))

def palindrome():
    textInp = text_input()
    text = ""
    for word in textInp:
        if word.isalpha():
            text += word
    if text.lower() == text[::-1].lower():
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")
        
def space_to_hashtag():
    textInp = text_input()
    print(textInp.replace(" ", "#"))

def num_in_input():
    textInp = text_input()
    for c in textInp:
        if c.isdigit():
            print("I found a number in the input.")
            break

def every_other_character():
    textInp = text_input()
    for i in range(len(textInp)):
        if i % 2 != 0:
            print(textInp[i], end="")

def print_one_ch_one_line():
    textInp = text_input()
    for c in textInp:
        print(c, end="\n")
        
def print_only_upperc():
    textInp = text_input()
    for c in textInp:
        if c.isalpha() and c == c.upper():
            print(c)
            
def stars_to_ch():
    textInp = text_input()
    for _ in range(len(textInp)):
        print("*", end="")
        
def ch_space():
    textInp = text_input()
    for c in textInp:
        if c == textInp[-1]:
            print(c)
        else:
            print(c, end=" ")

def island():
    numList = []
    for _ in range(23):
        numList.append(r.randint(0,3))
    landLen = 0
    landSum = 0
    landHigh = 0
    landDiff = 0
    landDist = 0
    n = 0
    while n != 0:
        if numList[n] != 0:
            break
            
        

if __name__ == "__main__":
    text = open_file()
    #case_sensitive(text)
    #not_case_sensitive(text)
    #space_remover()
    #palindrome()
    #space_to_hashtag()
    #num_in_input()
    #every_other_character()
    #print_one_ch_one_line()
    #print_only_upperc()
    #stars_to_ch()
    #ch_space()
    island()
