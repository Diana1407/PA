#PROBLEMA 1
def min_max(ls):
    return min(ls), max(ls)
def pb1_a():
    ls = [3, -3, 1, 7, 3, 2]
    print(*min_max(ls)) #afiseaza ca un tuplu

#def pb1_b():
def incarca_fisier(fis):
    ls = []
    with open(fis, 'r') as f:
        for linie in f:
            ls.append(linie.split())
    return ls

def pb1_c():
    fis = input("Citit numele fisierului: ")
    ls = []
    ls = incarca_fisier(fis)
    i = 0
    f = open('fis.out',"w")
    mini = 0
    maxi= 0
    for linie in ls:
        t = min_max(linie)
        if t[0] == t[1]:
            f.write(str(i) + "\n")
        if i == 0:
            mini = int(t[0])
            maxi = int(t[1])
        else:
            if int(t[0]) < mini:
                mini=int(t[0])
            if int(t[1]) > maxi:
                maxi=int(t[1])
        i += 1
    f.close()
    print(mini,maxi)

#PROBLEMA 2
def deviruseaza(prop):
    rez = ''
    ls = prop.split()
    n = len(ls)
    for i in range(n-1,-1,-1):
        l = len(ls[i])
        if l == 1:
            rez += ls[i] + " "
        else:
            cuv = ''
            p = ls[i][0]
            u = ls[i][l-1]
            cuv += u
            cuv += ls[i][1:l-1]
            cuv += p
            rez += cuv + " "
    return rez
def pb2_a():
    prop = input("Cititi prop: ")
    print(deviruseaza(prop))
def prime(n, numar_maxim=0):
    ls = []
    for i in range(n,1,-1):
        ok = 1
        if i<=1 or i>2 and i%2==0:
            ok = 0
        for d in range (3, i, 2):
            if (ok == 1 and i%d == 0):
                ok = 0
        if ok == 1:
            ls.append(i)
    if numar_maxim==0:
            return ls
    else:
        ls1=[]
        l = len(ls)
        for i in range(0,l):
            if numar_maxim == 0:
                break
            else:
                ls1.append(ls[i])
            numar_maxim -= 1
        return ls1
def pb_2b():
    n = int(input("Cititi n: "))
    print(prime(n))
def pb2_c():
    #f = open("intrare.in")
    g = open("intrare_devirusata.out", "w")
    i = 1
    with open("intrare.in", 'r') as f:
        for linie in f:
            if i>1:
                ls = prime(i,1)
                if ls[0]==i:
                    linie = deviruseaza(linie) + "\n"
            g.write(linie)
            i += 1
    g.close()

#PROBLEMA 3
#def pb3_a():
def cifra_control(n):
    while(n>9):
        s = 0
        while n>0:
            s += n % 10
            n = n // 10
        n = s
    return n
def insereaza_cifra_control(ls):
    l = len(ls)
    i = 0
    while l>0:
        l -= 1
        ls.insert(i+1,cifra_control(ls[i]))
        i += 2
def pb3_b():
    ls=[11,12,13,14,15]
    insereaza_cifra_control(ls)
    print(ls)
def egale(*liste):
    for i in range(1,len(liste)):
        if liste[i] != liste[i-1]:
            return False
    return True
def pb3_c():
    ls1 = [1,2]
    ls2 = [1,2]
    ls3 = [1,3]
    print(egale(ls1,ls2,ls3))
def pb3_d():
    with open("numere.in", 'r' )as f:
        for linie in f:
            for x in linie.split():
                print(x,cifra_control(int(x)))
def pb3_e():
    ls1 = []
    ls2 = []
    with open("numere.in", 'r') as f1:
        for linie in f1:
            ls1 = linie.split()
    with open("numere2.in", 'r') as f2:
        for linie in f2:
            ls2 = linie.split()
    s1 = set(ls1)
    s2 = set(ls2)
    lf1 = []
    lf2 = []
    for x in s1:
        lf1.append(cifra_control(int(x)))
    for x in s2:
        lf2.append(cifra_control(int(x)))
    lf1.sort()
    lf2.sort()
    if lf1 == lf2:
        print("DA")
    else:
        print("NU")

#PROBLEMA 4
#def pb4_b():
def despre_spiridus(d, cod):
    ls = d.get(cod)
    l = []
    for x in ls:
        t = tuple(x)
        l.append(t)
    print(l)

#def pb4_c():
def jucarii_v1(d):
    j = []
    i = 0
    for x in d:
        ls = d.get(x)
        for y in ls:
            if j.count(y[0])==0:
                j.append(y[0])
    l = len(j)
    for i in range(l-1):
        print(j[i], end="")
        print(',', end=" ")
    print(j[l-1])

def jucarii_v2(d): #bag toate jucariile in lista si dupa fac o multime cu set (adica o sa raman doar cu o jucarie de fiecare tip)
    ls=[]
    for x in d:
        lv = d[x]
        for y in lv:
            ls.append(y[0])
    s = set(ls)
    afisare=", ".join(s)
    print(afisare)

def spiridusi(d):
    ls = []
    for x in d:
        lt = []
        lt.append(x)
        val = d[x]
        lt.append(len(val))
        sum = 0
        for y in val:
            sum = sum + y[1]
        lt.append(sum)
        ls.append(lt)
    ls.sort(key = lambda t:(-t[1],-t[2], t[0]))
    lp = []
    for x in ls:
        lp.append((x[0], x[1], x[2]))
    for x in lp:
        print(x)

def actualizare(d, cod, jucarie):
    spir = d.get(cod)
    print(spir)
    l = len(spir)
    if(l>2):
        for x in spir:
            if x[0] == jucarie:
                spir.remove(x)
        return True
    else:
        return False

def pb4():
    #datele sunt salvate intr-un dictionar de forma
    # {S:[[jucarie, numar]]}
    with open("date.in", "r") as f:
        s = f.read()
        lt = [x for x in s.split("\n")] #imi adaug in lista pe fiecare pozitie o linie din fisier
    dictionar = {}
    for x in lt:
        spiridus, numar, jucarie = [y for y in x.split()] #despachetez linia
        numar = int(numar)
        m = len(jucarie)
        ls = dictionar.get(spiridus) #cheama spiridusul curent
        lv = []
        if (ls == None): #daca e NONE ins ca inca nu am nimic pus la spiridusul actual si adaug normal jucaria si numarul
            lv.append([jucarie, numar])
            dictionar[spiridus] = lv
        else: #altfel il scot din dictionar si fie updatez numarul daca exista jucaria, fie ii aduag inca o jucarie cu numarul ei
            ok = 0
            lf = dictionar.pop(spiridus)
            n = len(ls)
            ok = 1
            for i in range(n):
                string = lf[i][0]
                if (string == jucarie):
                    nr = lf[i][1] + numar
                    lf[i][1] = nr
                    ok = 0
            if (ok == 1):
                lf.append([jucarie, numar])
            dictionar[spiridus] = lf
    print(dictionar)
    despre_spiridus(dictionar, "S1")
    jucarii_v2(dictionar)
    spiridusi(dictionar)
    actualizare(dictionar,"S1","trenulet")
    despre_spiridus(dictionar,"S1")
pb4()

#DARIA GITHUB
#SORTARI

'''
1.a) Se cite??te o propozi??ie cu cuvinte separate prin spa??iu. S?? se formeze o nou?? propozi??ie cu
cuvintele din prima propozi??ie care au lungime cel pu??in 2 ordonate descresc??to'''
def pb1a():
    prop = input("Cititi propozitia: ")
    cuv = [x for x in prop.split() if len(x)>2]
    cuv.sort(reverse = True)
    print(cuv)

def pb1b():
    prop = input("Cititi propozitia: ")
    cuv = [x for x in prop.split() if len(x) > 2]
    cuv.sort(key = len, reverse = False)
    print(cuv)

'''
2. a) Se citesc un num??r natural n ??i urm??toarele informa??ii despre n persoane: cod de cel
mult 3 cifre, nume (un singur nume), prenume (un singur prenume), v??rsta (informa??ia despre
o persoana este dat?? pe o linie). S?? se creeze o list?? de tupluri cu 3 elemente cu informa??iile
despre cele n persoane ??i s?? se afi??eze lista cu print.'''
def pb2a():
    n = int(input(""))
    l = []
    for i in range(n):
        s = input()
        cod, nume, prenume, varsta = s.split()
        nume = nume + " " + prenume
        t = (int(cod), nume, int(varsta))
        l.append(t)
    print(l)

'''
b) S?? se afi??eze persoanele ordonate dup?? cod ??i, ??n caz de egalitate, dup?? nume (pentru o
persoan?? se va afi??a codul pe 4 caractere ??i numele)'''
def pb2b():
    n = int(input(""))
    l = []
    for i in range(n):
        s = input()
        cod, nume, prenume, varsta = s.split()
        nume = nume + " " + prenume
        t = (int(cod), nume, int(varsta))
        l.append(t)
    l.sort(key = lambda t:(t[0],t[1]))
    for x in l:
        print(x[0],x[1])

'''
c) S?? se afi??eze persoanele ordonate dup?? nume ??i, ??n caz de egalitate, dup?? cod (pentru o
persoan?? se va afi??a codul pe 4 caractere ??i numele)'''
def pb2c():
    n = int(input(""))
    l = []
    for i in range(n):
        s = input()
        cod, nume, prenume, varsta = s.split()
        nume = nume + " " + prenume
        t = (int(cod), nume, int(varsta))
        l.append(t)
    l.sort(key = lambda t:(t[1],t[0]))
    for x in l:
        print(x[0], x[1])

'''
d) S?? se afi??eze v??rsta maxim?? a unei persoane din list?? (folosind max(lista,key))'''
def pb2d():
    n = int(input(""))
    l = []
    for i in range(n):
        s = input()
        cod, nume, prenume, varsta = s.split()
        nume = nume + " " + prenume
        t = (int(cod), nume, int(varsta))
        l.append(t)
    vm = max(l, key = lambda t:(t[2]))
    print(vm[2])

#MATRICE SI VECTORI
'''
1. Se citesc n, m ??i o matrice cu n linii si m coloane (numerele sunt date c??te unul pe linie).
S?? se ordoneze cresc??tor elementele de pe prima coloana prin interschimb??ri de linii ??i s?? se
afi??eze matricea ob??inut?? (fiecare element se va afi??a pe 5 caractere)'''
def pb_1_met1():
    n,m = (int(x) for x in input().split())
    a = []
    for i in range (n):
        a.append([int(x) for x in input().split()])

    for i in range(n-1):
        for j in range(i+1, n):
            if a[i][0]>a[j][0]:
                ls = []
                ls = a[i]
                a[i] = a[j]
                a[j] = ls
    for linie in a:
        for x in linie:
            print(f"{x:4}",end="")
        print()
def pb_1_met2():
    n, m = (int(x) for x in input().split())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    a.sort(key = lambda t:(t[0]))
    for linie in a:
        for x in linie:
            print(f"{x:4}", end="")
        print()

'''
2. Se da un num??r natural n>2. S?? se afi??eze primele n linii din triunghiul lui Pascal (daca c
este num??rul maxim de cifre ale unui num??r din triunghi, toate numerele se vor afi??a pe c+1
caractere)'''
def pb_2_met1():
    n = int(input("Cititi n: "))
    p = 1
    for j in range(0, n + 1):
        print(1, end=" ")
        for i in range(1, j + 1):
            p = p * (j - i + 1) // i
            print(p, end=" ")
        print()

def pb_2_met2():
    n = int(input("Cititi n: "))
    a = []
    for i in range(n):
        a.append([0 for j in range (n)])
    for i in range(n):
        if i==0:
            a[0][0] = 1
        else:
            for j in range(0, i+1):
                if j==0 or j==i:
                    a[i][j] = 1
                else:
                    a[i][j] = a[i-1][j]+a[i-1][j-1]
    for i in range(n):
        for j in range(0, i+1):
            print(f"{a[i][j]:4}", end=" ")
        print()

'''
4. Se citesc m, n ??i o matrice cu m linii ??i n coloane, elementele unei linii fiind date pe o linie
(elementele unei linii date pe o linie separate cu spa??iu). S?? se construiasc?? ??n memorie ??i s??
se afi??eze matricea transpus??.'''
def pb_4_met1():
    m,n = [int (x) for x in input().split()]
    a = []
    for i in range(m):
        a.append([int(x) for x in input().split()])
    at = []
    for i in range(n):
        at.append([0 for j in range(m)])
    for i in range(m):
        for j in range(n):
            at[j][i] = a[i][j]
    for linie in at:
        for x in linie:
            print(f"{x:4}", end= " ")
        print()

def pb_4_met2():
    m,n = [int (x) for x in input().split()]
    a = []
    for i in range(m):
        a.append([int(x) for x in input().split()])
    at = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(a[j][i])
        at.append(b)
    for linie in at:
        for x in linie:
            print(f"{x:4}", end=" ")
        print()

'''
5. Se cite??te un num??r natural N.
a) S?? se genereze ??i afi??eze o matrice de dimensiune NxN, cu elementele de la 1 la N*N - ??n
ordine cresc??toare, de la st??nga la dreapta ??i de sus ??n jos.'''
def pb_5a_met1():
    n = int(input())
    k = 1
    a = []
    for i in range(n):
        ls = []
        for j in range(n):
            ls.append(k)
            k +=1
        a.append(ls)
    for linie in a:
        for x in linie:
            print(f"{x:4}", end = " ")
        print()

def pb_5a_met2():
    n = int(input())
    a = [[int(k) for k in range(1*i*n+1,n*i+n+1)] for i in range(n)]
    for linie in a:
        for x in linie:
            print(f"{x:4}", end = " ")
        print()
'''
b) Pentru a parcurge elementele matricei ??n spiral??, pornind din col??ul din st??nga-sus (spre
dreapta, ??n jos, spre st??nga, ??n sus, ???), s?? se ob??in?? ??nt??i o list?? av??nd elemente de tip tuplu
(linie, coloan??) care s?? reprezinte pozi??iile care trebuie parcurse ??n aceast?? spiral??.
c) Folosind lista de tupluri de mai sus, s?? se afi??eze elementele din matrice aflate la acele
pozi??ii.'''
def pb_5bc():
    n = int(input())
    a = [[int(k) for k in range(1 * i * n + 1, n * i + n + 1)] for i in range(n)]
    l=[]
    m=n-1
    k=0
    while k<m:
        i=k
        while i<m:
            t=(k,i)
            l.append(t)
            i=i+1
        i=k
        while i<m:
            t = (i, m)
            l.append(t)
            i = i + 1
        i=m
        while i>k:
            t = (m, i)
            l.append(t)
            i = i-1
        i=m
        while i>k:
            t = (i, k)
            l.append(t)
            i = i-1
        k=k+1
        m=m-1
    if m==k:
        t=(k,k)
        l.append(t)
    print(l)
    for x in l:
        i=x[0]
        j=x[1]
        print(a[i][j],end=" ")

'''
6. Ciurul lui Eratostene. Se d?? un numar natural n. S?? se creeze o list?? cu numerele prime
mai mici sau egale cu n.'''
def pb_6():
    n = int(input())
    ls = []
    for x in range(n,1,-1):
        ok = 1
        if x<=1 or x>2 and x%2==0:
           ok = 0
        for d in range(3,x,2):
            if x % d == 0:
                ok = 0
        if ok == 1:
            ls.append(x)
    ls.sort()
    print(ls)

'''
7. Se dau dou?? mul??imi cu elementele ordonate cresc??tor (c??te una pe linie). S?? se determine
eficient reuniunea ??i intersec??ia celor dou?? mul??imi (f??r?? a folosi set).'''
def pb_7_cu_set():
    a = {x for x in input().split()}
    b = {x for x in input().split()}
    reuniune = a | b
    print(reuniune)
    intersectie = a & b
    print(intersectie)

def pb_7_fara_set(): #interclasare modificata
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    reuniune = []
    intersectie = []
    l1 = len(a)
    l2 = len(b)
    #reuniune
    i = 0
    j = 0
    while i<l1 and j<l2:
        if a[i]<b[j]:
            reuniune.append(a[i])
            i += 1
        elif b[j]<a[i]:
            reuniune.append(b[j])
            j += 1
        elif a[i]==b[j]:
            reuniune.append(a[i])
            i += 1
            j += 1
    while i<l1:
        reuniune.append(a[i])
        i += 1
    while j<l2:
        reuniune.append(b[j])
        j += 1

    #intersectie
    i = 0
    j = 0
    while i < l1 and j < l2:
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        elif a[i] == b[j]:
            intersectie.append(a[i])
            i += 1
            j += 1
    print(reuniune)
    print(intersectie)

'''
8. Se citesc: un num??r natural n ??i un ??ir de n numere naturale.
a) S?? se afi??eze toate perechile distincte de elemente din ??ir cu suma 0 (2-SUM)'''
def pb_8a():
    n = int(input())
    ls = [int(x) for x in input().split()]
    print(ls)
    for i in range(n-1):
        for j in range(i+1,n):
            if ls[i]+ls[j]==0:
                print(ls[i],ls[j])

''' b) S?? se afi??eze toate tripletele de elemente din ??ir cu suma 0'''
def pb_8b():
    n = int(input())
    ls = [int(x) for x in input().split()]
    print(ls)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if ls[i]+ls[j]+ls[k]==0:
                    print(ls[i],ls[j],ls[k])
