# Muscalu Diana, 144
#Se dă fișierul "matrice.in" cu următoarea structură: pe linia 𝑖 se află separate prin câte un spațiu
#𝑛 numere naturale reprezentând elementele de pe linia 𝑖 a unei matrice, ca în exemplul de mai
#jos. Este cunoscut faptul că în fișier se află 𝑛 ∗ 𝑛 elemente numere naturale, unde 𝑛 este un
#număr natural impar > 2.
#a) [0,25p] Să se scrie o funcție citire_matrice care citește datele din fișierul "matrice.in" și
#returnează o matrice de dimensiune 𝑛 × 𝑛 formată din aceste numere

def citire_matrice():
    f = open("matrice.in")
    s = f.read()
    s = s.split("\n")
    mat = []
    for x in s:
        ls = [int(y) for y in x.split()]
        mat.append(ls)
    f.close()
    return mat

#b) [1,5p] Să se scrie o funcție care primește ca parametru matricea și returnează matricea bordată
#după următoarele reguli:
#● se va adăuga o coloană nouă la final (pe poziția 𝑛) care va avea pe poziția 𝑘 suma
#valorilor de pe linia 𝑘
#● se va adăuga o linie nouă la final (poziția 𝑛) care va avea pe poziția 𝑘 suma valorilor
#de pe coloana 𝑘

def fct(mat):
    n = len(mat)
    for x in mat:
        s = sum(x)
        x.append(s)
    vs = [0 for i in range(n+1)]
    n += 1
    for i in range(n-1):
        for j in range(n):
            if i == 0:
                vs[j] = mat[i][j]
            else:
                vs[j] += mat[i][j]
    mat.append(vs)
    return mat

#c) [1,25p] Se consideră matricea citită la punctul a), peste care se aplică funcția de la punctul b).
#Să se parcurgă matricea mai întâi pe diagonala principală, apoi pe diagonala secundară și, în final,
#restul elementelor care nu aparțin diagonalelor (parcurgerea se face pe linii de sus în jos și de la
#stânga la dreapta) și se afișează elementele în fișierul ”matrice.out”.

mat = citire_matrice()
m = fct(mat)
g = open("matrice.out", "w")
n = len(m)
for i in range(n):
    c = m[i][i]
    a=''
    while c:
        cif = c % 10
        cifs = cif + ord('0')
        a = a + chr(cifs)
        c = c // 10
    g.write(a)
    g.write(" ")
for i in range(n):
    c = m[i][n-i-1]
    a = ''
    while c:
        cif = c % 10
        cifs = cif + ord('0')
        a = a + chr(cifs)
        c = c // 10
    g.write(a)
    g.write(" ")
for i in range(n):
    for j in range(n):
        if i != j and j != n-i-1:
            c = m[i][j]
            a = ''
            while c:
                cif = c % 10
                cifs = cif + ord('0')
                a = a + chr(cifs)
                c = c // 10
            g.write(a)
            g.write(" ")
g.close()