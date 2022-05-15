'''
cislo = 0

for i in range(52):
    cislo += 1
    print(cislo)

slovo = 'bota'

def preved_slovo(s):
    seznam = []
    seznam[:0] = s
    print(seznam)

preved_slovo(slovo)



sifra = 'abcde'
vysledek = 'ggede'

def shodne(vysledek,odposlech):
    shodnost = 0
    
    for a, b in zip(vysledek, odposlech):
        if a == b:
            shodnost +=1
    print(shodnost)

shodne(sifra,vysledek)



final = [(1, 'BYffiqilfX'), (8, 'Helloworld'), (1, 'XuBBEMEHBt')]
final.sort()
f = final[-1]
desifra = f[1]
print(desifra)


import sys

soubor = open(sys.argv[1])
vstup = soubor.read().splitlines()
sifra = vstup[0]
odposlech = vstup[1]

with open('output.txt','w') as f:
    f.write(sifra)

'''

povoleno ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

test = 'krtek15'

for i in test:
    if not i in povoleno:
        print('Error: Chybny vstup!')
    else:
        print('deez what?')