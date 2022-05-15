'''Program precte soubor ktery musi mit 2 radky. Prvni radek je zasifrovane slovo,
druhy odposlechnute, castecne desifrovane slovo. Cilem programu je zjistit,
jake slovo je zasifrovane.
'''

import sys

'''
znaky = 2*26 = 52 pismen (26 malych[abc...xyz], 26 velkych[ABC...XYZ])

ASCII:
A = 65-90
a = 97-122

'''
#r urcuje pocet posunuti(ve funkci dochazi k rekurenci)
#seznam final vytridi vysledek s nejvetsim poctem shodnych znaku

final = []
r = 0

'''
sifra = 'mnoXYhnJLJ'
odposlech = 'JCudvgtXRi'
'''
try:
    soubor = open(sys.argv[1])
    vstup = soubor.read().splitlines()
    sifra = vstup[0]
    odposlech = vstup[1]
except IndexError:
    print('Chyba! Chybejici argumenty!')
    exit()

povoleno ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in sifra:
    if not i in povoleno:
        print('Error: Chybny vstup!')
        exit()

for i in odposlech:
    if not i in povoleno:
        print('Error: Chybny vstup!')
        exit()
    

def shodne(vysledek,odposlech):
    shodnost = 0
    
    for a, b in zip(vysledek, odposlech):
        if a == b:
            shodnost +=1
    
    return shodnost
            

def cccc(r):
    if 0<= r <=9:
        c = '0'+str(r)
    elif r>9:
        c = str(r)
    return c

def jeshodne(shodnost):
    if shodnost>0:
        shodn = 'shodnost = {}'.format(shodnost)
        return shodn
    else:
        return ''

def jeshodne_int_vys(shodnost,vysledek):
    if shodnost>0:
        return shodnost, vysledek
    else:
        return None

def posun(string,r):    
    s = []

    for pismeno in string:
        
        o = ord(pismeno)
        
        for i in range(r):
            if o == 90:
                o += 7
            elif o == 122:
                o += -57
            else:
                o +=1
        
        s.append(chr(o))
        
    vysledek = ''.join(s)
    
    shodnost = shodne(vysledek,odposlech)

    c = cccc(r)

    shod = jeshodne(shodnost)

    shod_int = jeshodne_int_vys(shodnost,vysledek)

    if shod_int != None:
        final.append(shod_int)

    #print('|{}|'.format(c), vysledek, '~', odposlech,shod)
    '''
    Libila se mi predstava tabulky, ktera vyhazuje jednotlive posuny,
    tak sem si ji vytvoril. Odkomentovanim radku nad timto komentarem
    se tabulka vytiskne. Dokonce tiskne pocet shodnych pismen pouze v
    pripade, pokud nejaka shodna pismena jsou.
    '''



def desifruj(sifra,odposlech,r):
    
    if not len(sifra) == len(odposlech):
        print('Error: Chybna delka vstupu!')
        exit()

    else:
        if r !=52:
            posun(sifra,r)
            r +=1
            desifruj(sifra,odposlech,r)

        elif r ==52:
            posun(sifra,r)
            final.sort()
            f = final[-1]
            desifra = f[1]
            with open('output.txt','w') as f:
                f.write(desifra)

desifruj(sifra,odposlech,r)