#BACKTRACKING

'''PERMUTARI
    Reprezentare solutie: x = (x1, x2,..., xn),  unde xk apartine {1,2,...,n}  (pk=1, uk=n)
    Conditii finale: cand indicele curent k ajunge sa fie egal cu n, inseamna ca avem solutie si o afisam
                        + toate elem sa fie diferite
    Conditii de continuare pt xk: xk sa nu se regaseasca printre termenii deja pusi in solutie adica in x[:k]

def back1(k):
    #cond de oprire:
    if k == n:
        print(*x)
    else:
        for i in range(1,n+1):
            if i not in x:
                x[k] = i
                back(k+1)
                x[k] = 0

def back2(k):
    #cond de oprire:
    if k == n:
        if x[0] == p:
            print(*x)
    else:
        for i in range(1,n+1):
            if i not in x:
                x[k] = i
                back2(k+1)
                x[k] = 0

n = 4
p = 1
x = [0 for i in range(n)]
v = [0 for i in range(n + 1)]
back2(0)
'''

'''ARANJAMENTE
    Reprezentare solutie: x = (x1, x2,..., xm),  unde xk apartine {1,2,...,n} 
    Conditii finale: cand indicele curent k ajunge sa fie egal cu m, inseamna ca avem solutie si o afisam
                        + toate elem sa fie distincte
    Conditii de continuare pt xk: xk sa nu se regaseasca printre termenii deja pusi in solutie adica in x[:k]

def back(k):
    if k == m:
        print(*x)
    else:
        for i in range(1, n + 1):
            if i not in x:
                x[k] = i
                back(k+1)
                x[k] = 0
n = 4
m = 3
x = [0 for i in range(m)]
back(0)
'''

'''COMBINARI
    Reprezentare solutie: x = (x1, x2,..., xm),  unde xk apartine {1,2,...,n} 
    Conditii finale: cand indicele curent k ajunge sa fie egal cu m, inseamna ca avem solutie si o afisam
                        + toate elem sa fie distincte si in ordine crescatoare
    Conditii de continuare pt xk: xk sa nu se regaseasca printre termenii deja pusi in solutie adica in x[:k] 
                        si xk sa fie mai mare decat toti termenii precedenti

def back(k):
    if k == m:
        print(*x)
    else:
        for i in range(1,n+1):
            if i not in x and i > x[k - 1]:
                x[k] = i
                back(k+1)
                x[k] = 0

n = 4
m = 3
x = [0 for i in range(m)]
back(0)
'''

'''SUBMULTIMI
    Pb se reduce la generarea tutoror sirulior binare de lungime n unde 1 inseamna ca punem numarul in sir,
iar 0 ca nu il punem 
    Reprezentare solutie: x = (x1, x2,..., xn),  unde xk apartine {0,1} 
    Conditii finale: nu avem
    Conditii de continuare pt xk: nu avem

def back(k):
    if k == n:
        for i in range(n):
            if x[i] == 1:
                print(a[i], end = " ")
        print()
    else:
        for i in range(0,2):
            x[k] = i
            back(k+1)


a = [3, 1, 7, 9]
n = len(a)
x = [0 for i in range(n)]
back(0)
'''

'''PARTITII
n - toate modalitatile de a scrie n ca suma de numere naturale nenule
(cu obs ca ordinea termenilor in descompunere conteaza)
n=4:
1+1+1+1
1+1+2 = 1+2+1
1+3
2+2
4
    Reprezentare solutie: x = (x1, x2,..., xk),  unde xk apartine {1,2,....,n} 
    Conditii finale: suma din x sa fie egala cu n
    Conditii de continuare pt xk: suma din x[:k] la care adunam elementul curent xk pe care vrem sa 
                                    il punem in solutie sa nu depaseasca suma ceruta n

def back(k):
    if sum(x[:k]) == n:
        print(*x[:k])
    else:
        for i in range(1,n+1):
            if sum(x[:k]) + i <= n:
                x[k] = i
                back(k+1)
                x[k] = 0

n = 4
x = [0 for i in range(n)]
back(0)
'''

'''PB1_LAB
Se d?? o sum?? S ??i n tipuri de monede av??nd valorile v1, v2, ..., vnlei(un num??r nelimitat de valori de fiecare tip). 
Se cer toate modalit????ile de plat?? a sumei S utiliz??nd aceste monede.
Exemplu: Pentru S=20 ??i n=3 tipuri de monede, cu valorile v1=1,v2=5, v3=10 putem avea urm??toarele modalit????i de plat?? 
(pentru fiecare moned?? de la 1 la n se afi??eaz?? num??rul de monezi de acest tip care se pl??tesc):
0, 2, 1 (0 monede de 1 leu, 2 de 5 lei ??i 1 de 10 lei)
0, 0, 2
5, 1, 1
5, 3, 0
10, 0, 1
10, 2, 0
15, 1, 0
20, 0, 0
    Reprezentare solutie: x = (x1, x2,..., xk),  unde xk apartine {1,2,....,s} 
    Conditii finale: k sa fie egal cu n si suma monedelor sa fie egala cu s
    Conditii de continuare pt xk: nu avem

def back(k,suma):
    if k == n:
        if suma == s:
            print(*x)
    else:
        for i in range(mini+1):
            x[k] = i
            suma += x[k] * v[k]
            back(k+1, suma)
            suma -= x[k] * v[k]
            x[k] = 0

s = 20
n = 3
x = [0 for i in range(n)]
v = [1,5,10]
mini = s // min(v)
back(0,0)
'''

'''PB2_LAB
Se dau n mul??imi (elementele fiec??rei mul??imi se dau pe o linie, separate prin spa??iu). 
S?? se afi??eze elementele produsului cartezian al celor n mul??imi
    Reprezentare solutie: x = (x1, x2,..., xk),  unde xk apartine multimilor date x1 in m1, x2 in m2.... xk in mk
    Conditii finale: k sa fie egal cu n 
    Conditii de continuare pt xk: nu avem

def back(k):
    if k == n:
        print(*x)
    else:
        for y in mat[k]:
            x[k] = y
            back(k+1)
            x[k] = 0


f = open("date.in")
s = f.read().split("\n")
f.close()
mat = []
for linie in s:
    ls = [int(x) for x in linie.split()]
    mat.append(ls)
n = len(mat)
x = [0 for i in range(n)]
back(0)
'''

'''PB3_LAB
Pentru elaborarea unui test de aptitudini avem un set de n ??ntreb??ri, fiecare fiind 
cotat?? cu un num??r de puncte dat. S?? se elaboreze toate chestionarele av??nd a ??ntreb??ri distincte, 
fiecare chestionar totaliz??nd p puncte. ??ntreb??rile sunt date prin num??r ??i punctaj. Nu se ??ine cont 
de ordinea ??ntreb??rilor ??n chestionar (de exemplu chestionarul cu ??ntreb??rile 1 ??i 2 este acela??i cu 
chestionarul cu ??ntreb??rile 2 ??i 1).
    Reprezentare solutie: x = (x1, x2,..., xk),  unde xk apartine {1,2,....,n} 
    Conditii finale: k sa fie egal cu a si suma elementelor din pct cu indicii salvati in x sa aibe suma p
    Conditii de continuare pt xk: sa nu se mai regaseasca pana atunci in solutie si elem sa fie in ordine
                                    crescatoare
def back(k):
    if k == a:
        sum = 0
        for i in x[:a]:
            sum+= pct[i-1]
        if sum == p:
            print(*x[:a])
    for i in range(1,n+1):
        if i not in x:
            if i > x[k-1]:
                x[k] = i
                back(k+1)
                x[k] = 0
n = 6
a = 3
p = 10
x = [0 for x in range(n)]
pct = [1,4,2,3,5,4]
back(0)
'''

'''PB4_LAB
S?? se descompun?? un num??r natural n ??n toate modurile posibile distincte ca sum?? de numere prime
(de  exemplu,  pentru  n  =  10  descompunerile  sunt  2+2+2+2+2,  2+2+3+3,  2+3+5,  5+5, 3+7).
    Reprezentare solutie: x = (x1, x2,..., xk),  unde xk apartine multimii nr prime mai mici egale cu n 
    Conditii finale: suma din s[:k] sa fie egala cu n
    Conditii de continuare pt xk: suma elem din x[:k] la care se aduna elementul curent sa nu depaseasca n si elemntul
                        curent x[k] sa fie mai mare sau egal cu predecesorii sai

def back(k):
    if sum(x[:k]) == n:
        print(*x[:k], sep = "+")
    else:
        for y in prime:
            if sum(x[:k]) + y <= n and x[k-1] <= y:
                x[k] = y
                back(k + 1)
                x[k] = 0

n = 10
x = [0 for i in range(n // 2 + 2)]
primeList = lambda M: [y for y in range(2,n) if all(y%d for d in range(2,y))]
prime = primeList(n)
back(0)
'''

'''
VARIANTA 2
def prim(numar):
    for i in range (2,numar-1):
        if numar%i==0:
            return 0
    return 1
def back(k):
    if sum(x[1:k])==n:
        print(*x[1:k], sep="+")
    elif k<=n//2:
        for i in range(x[k-1], n+1):
            x[k]=i
            if prim(x[k])==1:
                back(k+1)

n=10
x=[2]*(n//2+1)
back(1)
'''

#TEMA CURS PROBLEME BACKTRACKING

'''PB1
Se d?? un cuv??nt s. S?? se afi??eze toate anagramele sale.
Problema se reduce la o problema de permutari.
    Reprezentare solutie: x = (x1, x2,..., xn),  unde xk apartine {1,2,...,n}  
    Conditii finale: cand indicele curent k ajunge sa fie egal cu n, inseamna ca avem solutie si o afisam
                        + toate elem sa fie diferite
    Conditii de continuare pt xk: xk sa nu se regaseasca printre termenii deja pusi in solutie adica in x[:k]

def afis(x):
    cuv = ''
    for i in x:
        cuv += ls[i-1]
    print(cuv)

def back(k):
    if k == n:
        afis(x)
    else:
        for i in range(1,n+1):
            if i not in x:
                x[k] = i
                back(k+1)
                x[k] = 0
s = 'rac'
ls = list(s)
n = len(s)
x = [0 for i in range(n)]
back(0)
'''

'''PB2
Se d?? o mul??ime de numere naturale ??i un num??r natural M. 
S?? se afi??eze toate submul??imile de sum?? M ale mul??imii date.
    Reprezentare solutie: x = (x1, x2,..., xk),  unde xk apartine {1,2,...,n} = multimea data
    Conditii finale: suma din x[:k] sa fie egala cu M
    Conditii de continuare pt xk: xk sa nu se regaseasca printre termenii deja pusi in solutie adica in x[:k],
                                    daca il adaugam pe xk in solutie noua suma sa nu depaseasca M si termenii
                                        sa fie in ordine crescatori 

def back(k):
    if sum(x[:k]) == M:
        print(*x[:k])
    else:
        for i in a:
            if i not in x and sum(x[:k]) + i <=M and x[k-1] <= i:
                x[k] = i
                back(k+1)
                x[k] = 0

a = [1,2,3,4,5,6]
n = 6
M = 7
x = [0 for i in range(n)]
back(0)
'''

'''PB3 = PB4
??ntr-o clas?? sunt n fete identificate prin numerele naturale de la 1 la n ??i m b??ie??i identifica??i
prin numerele naturale de la n+1 la n+m. S?? se afi??eze toate modalit????ile de a forma echipe de c??te 
t elevi din clas?? astfel ??nc??t ??n fiecare echip?? s?? fie cel pu??in o fat?? ??i cel pu??in un b??iat  
(n,m,t>2  se  citesc  de  la  tastatur??).??n  cadrul  unei  echipe  nu  conteaz??  ordinea membrilor.
    Reprezentare solutie: x = (x1, x2,..., xk),  unde xk apartine {1,2,...,n+m} 
    Conditii finale: k sa fie egal cu t, iar in solutie sa am cel putin un baiat si cel putin o fata
    Conditii de continuare pt xk: xk sa nu se regaseasca printre termenii deja pusi in solutie adica in x[:k],
                                    si termenii sa fie in ordine crescatori 

def back(k):
    if k == t:
        nrb = 0
        nrf = 0
        for i in x:
            if i in f:
                nrf += 1
            else:
                nrb += 1
        if nrb != 0 and nrf != 0:
            print(*x)
    else:
        for i in range(1, nm + 1):
            if x[k-1] < i:
                x[k] = i
                back(k+1)
                x[k] = 0


n = 5
m = 3
t = 3
nm = n + m
f = [1,2,3,4,5]
b = [6,7,8]
x = [0 for i in range(t)]
back(0)
'''

'''PB5
S?? se afi??eze toate numerele naturale cu n cifre av??ndsuma cifrelor s (n ??i s se citesc de la tastatur??). 
    Reprezentare solutie: x = (x1, x2,..., xn),  unde xk apartine {1,2,...,9} 
    Conditii finale: k sa fie egal cu n, iar suma din x[:k] sa fie s
    Conditii de continuare pt xk: xk se adauga in solutie daca adunarea lui la suma curenta din x[:k] 
                                    nu depaseste s
'''
def back(k):
    if k == n:
        if sum(x[:k]) == s:
            print(*x, sep = "")
    else:
        for i in range(1,10):
            if sum(x[:k]) + i <= s:
                x[k] = i
                back(k+1)
                x[k] = 0

n = 3
s = 6
x = [0 for i in range(n)]
back(0)
