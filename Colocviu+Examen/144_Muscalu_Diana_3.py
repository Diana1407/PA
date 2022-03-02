# Muscalu Diana, 144
#Fișierul text drumuri.in conține informații despre drumurile dintre orașele unei țări. O linie din
#fișier are următoarea structură:
#Nume_Oras_1 - Nume_Oras_2 distanta stare_drum
#unde Nume_Oras_1 și Nume_Oras_2 sunt numele a două orașe (un nume este un șir de
#cuvinte separate prin câte un spațiu), distanta este lungimea drumului dintre cele două orașe,
#iar stare_drum (număr natural) este un număr natural între 0 și 5 reprezentând calitatea
#drumului între cele două orașe. Pe un drum se poate circula doar într-un sens, respectiv de la
#Nume_Oras_1 la Nume_Oras_2.

f = open("drumuri.in")
s = f.read()
s = s.split("\n")
d = {}
for x in s:
    inf = x.split(" -")
    f = d.get(inf[0])
    if f == None:
        ls = inf[1].split()
        for y in ls:
            nume = ''
            l = len(ls)
            if l == 4:
                nume = nume + ls[0] + " " + ls[1]
                dist = int(ls[2])
                stare_drum = int(ls[3])
            else:
                nume = nume + ls[0]
                dist = int(ls[1])
                stare_drum = int(ls[2])
        lf = []
        lf.append(nume)
        lf.append(dist)
        lf.append(stare_drum)
        d[inf[0]] = lf

        d[inf[0]] = inf[1]
    else:
        ls = f.split()
        nume=''
        l = len(ls)
        if l == 4:
            nume = nume + ls[0] + " " + ls[1]
            dist = int(ls[2])
            stare_drum = int(ls[3])
        else:
            nume = nume + ls[0]
            dist = int(ls[1])
            stare_drum = int(ls[2])
        lf = []
        lf.append(nume)
        lf.append(dist)
        lf.append(stare_drum)
        ls = inf[1].split()
        for y in ls:
            nume = ''
            l = len(ls)
            if l == 4:
                nume = nume + ls[0] + " " + ls[1]
                dist = int(ls[2])
                stare_drum = int(ls[3])
            else:
                nume = nume + ls[0]
                dist = int(ls[1])
                stare_drum = int(ls[2])
        lf.append(nume)
        lf.append(dist)
        lf.append(stare_drum)
        d[inf[0]] = lf

print(d)

#b) [1 p.] Scrieți o funcție modifica_stare care are următorii parametri (în această ordine):
#• structura în care s-au memorat datele la cerința a)
#• un număr natural s între 0 și 5 reprezentând starea unui drum
#• două șiruri de caractere o1 și o2; ultimul parametru o2 are valoarea implicită șirul vid.
#Dacă o2 este un șir nevid, funcția va modifica starea drumului de la orașul cu numele o1
#la orașul o2 cu valoarea s, dacă acest drum există. Dacă o2 este șirul vid funcția va modifica
#starea tuturor drumurilor de la orașul o1 la celelalte orașe în s. Funcția va returna numărul
#de drumuri a căror stare a fost modificată.

def modifica_stare(d, s, o1, o2=None):
    if o2 == None:
        for x in d:
            if x == o1:
                nume = d[x][0]
                dist = d[x][1]
                stare_drum = d[x][2]
                stare_drum = s
                lf = []
                lf.append(nume)
                lf.append(dist)
                lf.append(stare_drum)
                del d[x]
                d[x] = lf

    else:
        for x in d:
            if x == o1:
                nume = d[x][0]
                dist = d[x][1]
                stare_drum = d[x][2]
                stare_drum = s
                lf = []
                lf.append(nume)
                lf.append(dist)
                lf.append(stare_drum)
                del d[x]
                d[x] = lf
    print(d)
modifica_stare(d, 3, "Oraselul Mic")
