
with open("adatfile.txt","r",encoding="utf-8") as be:
    adatok = []
    for sor in be:
        adatok.append(sor.strip().split())

#print(adatok)
'''
for x in adatok:
    e = int(x[0]) * int(x[1])
    print(e)
'''
with open("eredmeny.txt","w",encoding="utf-8") as ki:
    for x in adatok:
        print("{} * {} = {}".format(x[0], x[1], int(x[0])*int(x[1])), file=ki)

print("VÉGE")
    