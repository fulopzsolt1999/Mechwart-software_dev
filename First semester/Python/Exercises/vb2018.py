def get_data_from_file():
    fileD = []
    with open("Python/files/vb2018.txt", "r", encoding="utf-8") as f:
        next(f)
        for data in f:
            fileD.append(
                {"City": data.split(";")[0],
                 "Stadium": data.split(";")[1],
                 "Alt. Stadium": data.split(";")[2],
                 "Stadium room": data.rstrip('\n').split(";")[3]
                 })
    return fileD

def count_stadiums(l):
    print(f"3. fealdat: Stadionok száma: {len(l)}")
    
def least_stadium_room(l):
    leastRI = 0
    roomN = int(l[0]["Stadium room"])
    for i in range(len(l)):
        if roomN > int(l[i]["Stadium room"]):
            roomN = int(l[i]["Stadium room"])
            leastRI = i
    print(f'''4. feladat: A legkevesebb férőhely:
          Város: {l[leastRI]["City"]}
          Stadion neve: {l[leastRI]["Stadium"]}
          Férőhely: {l[leastRI]["Stadium room"]}''')

def average_room(l):
    roomSum = 0
    for data in l:
        roomSum += int(data["Stadium room"])
    print(f"5. feladat: Átlagos férőhelyszám: {roomSum/len(l):.1f}")
    
def check_alt_names(l):
    count = 0
    for data in l:
        if data["Alt. Stadium"] != "n.a.":
            count += 1
    print(f"6. feladat: Két néven is ismert stadionok száma: {count}")
    
def city_input():
    cityInp = input("Give me a city's name: ")
    while True:
        if cityInp.isalpha() and len(cityInp) >= 3:
            break
        else:
            cityInp = input("Give me a city's name: ")
    return cityInp

def check_input_VB(l, cI):
    found = False
    for data in l:
        if cI.lower() == data["City"].lower():
            found = True
            break
    if found:
        print("8. feladat: A megadott város VB helyszín.")
    else:
        print("8. feladat: A megadott város nem VB helyszín.")
        
def check_different_cities(l):
    cities = []
    for data in l:
        cities.append(data["City"])
    print(f"9. feladat: {len(list(dict.fromkeys(cities)))} különböző városban voltak mérkőzések.")

if __name__ == "__main__":
    vbList = get_data_from_file()
    count_stadiums(vbList)
    least_stadium_room(vbList)
    average_room(vbList)
    check_alt_names(vbList)
    check_input_VB(vbList, city_input())
    check_different_cities(vbList)
    