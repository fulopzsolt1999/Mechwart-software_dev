def get_data_from_file():
    vasData = []
    with open("Python/szemszam/vas.txt", "r") as f:
        for birth in f.readlines():
            vasData.append(birth.strip())
    print(f"2. feladat: Adatok beolvasása, tárolása")
    return vasData

def check_last_digit(vD):
    count = 0
    mathNum = 0
    result = []
    for birth in vD:
        for i in range(len(birth)-1):
            if birth[i].isdigit():
                count += int(birth[i])*(len(birth)-3-mathNum)
                mathNum += 1
        if int(birth[-1]) != count % 11:
            result.append(birth)
        count = 0
        mathNum = 0
    print("4. feladat: Ellenőrzés")
    for res in result:
        print(f"\tHibás a {res} személyi azonosító!")
    return result
        
def count_birth(vD, fB):
    print(f"5.feladat: Vas megyében a vizsgált évek alatt {len(vD)-len(fB)} csecsemő született.")
    
def count_boys(vD, fB):
    count = 0
    for birth in vD:
        if int(birth[0]) % 2 != 0 and birth not in fB:
            count += 1
    print(f"6. feladat: Fiúk száma: {count}")
    
def date(vD):
    dateYear = []
    for birth in vD:
        if int(birth[2]) == 9:
            dateYear.append("19"+str(birth[2:4]))
        else:
            dateYear.append("20"+str(birth[2:4]))
    print(f"7. feladat: Vizsgált időszak: {min(dateYear)} - {max(dateYear)}")
    return dateYear
    
def leap_day(vD):
    leapDay = '0224'
    for birth in vD:
        if birth[4:8] == leapDay:
            print("8. feladat: Szökőnapon született baba!")
            break
        
def statistics(vD, aY, fB):
    birthYears = []
    for year in list(dict.fromkeys(aY)):
        birthYears.append({'year': year, 'born': 0})
    for birth in vD:
        for i in range(len(birthYears)):
            if birth[2:4] == birthYears[i]['year'][2:4] and birth not in fB:
                birthYears[i]['born'] += 1
    print("9. feladat: Statisztika")
    for date in birthYears:
        print(f"\t{date['year']} - {date['born']}")

if __name__ == "__main__":
    vasData = get_data_from_file()
    falseBirth = check_last_digit(vasData)
    count_birth(vasData, falseBirth)
    count_boys(vasData, falseBirth)
    allYears = date(vasData)
    leap_day(vasData)
    statistics(vasData, allYears, falseBirth)