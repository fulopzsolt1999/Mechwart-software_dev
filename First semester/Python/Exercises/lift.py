def get_file_data():
    data = []
    with open("Python/files/lift.txt", "r") as f:
        for line in f:
            data.append(
                {"Date": line.rstrip('\n').split(" ")[0],
                 "Card number": line.rstrip('\n').split(" ")[1],
                 "Start level": line.rstrip('\n').split(" ")[2],
                 "Target level": line.rstrip('\n').split(" ")[3]
                 }
                )
    return data
    
def count_usage(fData):
    print(f"3. feladat: {len(fData)}")
    
def start_finish_date(fData):
    print("4. feladat:",(fData[0])["Date"],"-",fData[-1]["Date"])
    
def max_level(fData):
    result = 0
    for data in fData:
        if result < int(data["Target level"]):
            result = int(data["Target level"])
    print(f"5. feladat: Célszint max: {result}")
    
def get_input(fData):
    try:
        cardNum = int(input("\nGive me a card number: "))
    except:
        cardNum = 5
    try:
        targetLvl = int(input("Give me the target level: "))
    except:
        targetLvl = 5
    print(f"6.feladat:\n\tKártya száma: {cardNum}\n\tCélszint száma: {targetLvl}")
    return {"Card number": cardNum, "Target level": targetLvl}
    
def check_moving(fData, l):
    moved = False
    for data in fData:
        if int(data["Card number"]) == l["Card number"] and int(data["Target level"]) == l["Target level"]:
            moved = True
    if moved:
        print("A(z)", str(l["Card number"])+".", "kártyával utaztak a(z)",str(l["Target level"])+".", "emeletre!")
    else:
        print("A(z)", str(l["Card number"])+".","kártyával nem utaztak a(z)", str(l["Target level"])+".", "emeletre!")
        
def count_dates(fData):
    datesList = []
    for d in fData:
        datesList.append(d["Date"])
    dates = list(dict.fromkeys(datesList))
    d = 0
    count = 0
    countDates = []
    for i in range(len(fData)):
        if dates[d] == fData[i]["Date"]:
            count += 1
        else:
            countDates.append({"Date": dates[d],
                               "Number": count})
            count = 1
            d += 1
    print("8. feladat: Statisztika",
          "\n".join(["\t"+str(date["Date"])+" - "+str(date["Number"])+"x" for date in countDates]), sep="\n")
    
if __name__ == "__main__":
    fileData = get_file_data()
    count_usage(fileData)
    start_finish_date(fileData)
    max_level(fileData)
    inpList = get_input(fileData)
    check_moving(fileData, inpList)
    count_dates(fileData)
