with open("szemelyek.txt","r",encoding="utf-8") as be:
    adatok=[]
    for sor in be:
        adatok.append(sor.strip().split(";"))

#print(adatok)

# Nevek kiírása, ha azonos a vezetéknév és a keresztnév első karaktere
for x in adatok:
    if x[0][0] == x[1][0]:
        print(x[0], x[1])

# Keresztnév bekérése és ennek megszámolása az adatok között
knev = input("Kérem a keresztnevet: ")
db = 0
for x in adatok:
    if x[1].lower() == knev.lower():
        db +=1
if db>0:
    print(db)
else:
    print("nincs ilyen...")

# A legidősebb személy neve
datum = []
for x in adatok:
    datum.append(x[2])
idos = min(datum)
idoshely = datum.index(idos)
print(adatok[idoshely][0], adatok[idoshely][1])

# születési évek statisztikája (pl: 1982 - 11 fő)
evek = []
for x in adatok:
    evek.append(x[2][:4])
egyedi = []
for x in evek:
    if not(x in egyedi):
        egyedi.append(x)
egyedi.sort()

for x in egyedi:
    print("{} - {} fő".format(x, evek.count(x)))




