be = open("mondas.txt","r",encoding="utf-8")
szoveg = []
for sor in be:
    szoveg.append(sor.strip())
be.close()

'''print(szoveg)

for x in szoveg:
    print(x)
'''

hely = 0
for i in range(len(szoveg)):
    if len(szoveg[i])>len(szoveg[hely]):
        hely = i
print(szoveg[hely])

# vagy:
hosszu = szoveg[0]
for x in szoveg:
    if len(x)>len(hosszu):
        hosszu = x
print(hosszu)
