with open("lift.txt","r",encoding="utf-8") as be:
    adatok = []
    for sor in be:
        adatok.append(sor.strip().split())

# 3. feladat
db = len(adatok)
print("3. feladat: Összes lifthasználat:",db)

# 4. feladat
mettol = adatok[0][0]
meddig = adatok[-1][0]
print("4. feladat: Időszak: {} - {}".format(mettol, meddig))

# 5. feladat
# egyik megoldás (kigyűjtés):
cellista = []
for x in adatok:
    cellista.append(x[3])
celmax1= max(cellista)
print("5. feladat: Célszint max:",celmax1)

# másik megoldás (bejárással):
celmax2 = "0"
for x in adatok:
    if x[3]>celmax2:
        celmax2 = x[3]
print("5. feladat: Célszint max:",celmax2)

# 6. feladat
print("6. feladat:")
kszam = input("\tKártya száma: ")
cszam = input("\tCélszint száma: ")
try:
    knum = int(kszam)
except:
    knum = 5
try:
    cnum = int(cszam)
except:
    cnum = 5

# 7. feladat
# for ciklussal
utaztak = False
for x in adatok:
    if int(x[1])==knum and int(x[3])==cnum:
        utaztak = True
        break
if utaztak:
    print("7. feladat: A(z) {}. kártyával utaztak a(z) {}. emeletre!".format(knum,cnum))
else:
    print("7. feladat: A(z) {}. kártyával nem utaztak a(z) {}. emeletre!".format(knum,cnum))

# while ciklussal:
utaz = False
i = 0
while not(utaz) and i<db:
    utaz = (int(adatok[i][1])==knum and int(adatok[i][3])==cnum)
    i += 1
if utaz:
    print("7. feladat: A(z) {}. kártyával utaztak a(z) {}. emeletre!".format(knum,cnum))
else:
    print("7. feladat: A(z) {}. kártyával nem utaztak a(z) {}. emeletre!".format(knum,cnum))

# 8. feladat
print("8. feladat: Statisztika:")
datumok = []
for x in adatok:
    datumok.append(x[0])
egyedi = []
for x in datumok:
    if not(x in egyedi):
        egyedi.append(x)
for x in egyedi:
    print("\t{} - {}x".format(x, datumok.count(x)))

