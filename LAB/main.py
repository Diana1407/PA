#SORTARI
def pb_1_v1():
    s = input("Cititi propozitia: ")
    cuv=s.split()
    print(cuv)
    cuv.sort(key=len,reverse=True)
    for x in cuv:
        if len(x)>=2:
            print(x,end=" ")

def pb_1_v2():
    prop = "Ana are 3 mere si 2 banane"
    pct_a = " ".join(sorted([cuv for cuv in prop.split() if len(cuv) >= 2], reverse=True))
    pct_b = " ".join(sorted([cuv for cuv in prop.split() if len(cuv) >= 2], key=lambda x: -len(x)))
    print(pct_a, pct_b, sep='\n')

def cheie_a(x):
    return int(x[0]),x[1]

def cheie_b(x):
    return x[1],int(x[0])

def cheie_c(x):
    return int(x[3])

def pb_2():
    n = int(input("Cititi n: "))
    ls = []
    for i in range(n):
        ti = tuple(j for j in input().split())
        ls.append(ti)
    ls_a = sorted(ls, key=cheie_a)
    print(ls_a)
    ls_b = sorted(ls,key=cheie_b)
    print(ls_b)
    #var_1 pt varsta
    rez_1 = max(ls,key=cheie_c)
    print(f"Varsta maxima este {rez_1[3]}")

    #var_2 pt varsta
    rez_2 = max(ls, key=lambda x: int(x[3]))
    print(f"Varsta maxima este {rez_2[3]}")

#MATRICE, VECTORI
def pb1():
    n,m = [int(x) for x in input("Cititi n si m: ").split()]
    a=[]
    for i in range(n):
       a.append([int(x) for x in input().split()])
    a.sort()
    for linie in a:
        for x in linie:
            print(f"{x:4}", end=" ")
        print()

#def pb2(): #TRIUNGHIUL LUI PASCAL

def pb4(): #Transpusa
    m,n = [int(x) for x in input("Cititi m si n: ").split()]
    a=[]
    for i in range(m):
        a.append([int(x) for x in input().split()])

    b=[]
    for j in range(n):
        linie=[]
        for i in range(m):
            linie.append(a[i][j])
        b.append(linie)
    for linie in b:
        for x in linie:
            print(f"{x:4}",end=" ")
        print()

def pb5_a():
    n = int(input("Cititi n: "))
    a = []
    for i in range(n):
        a.append([int(x) for x in range(i*n+1,(i+1)*n+1)])

    for linie in a:
        for x in linie:
            print(f"{x:4}", end=" ")
        print()


def spiralPrint(m, n, a):
    k = 0
    l = 0

    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''

    while (k < m and l < n):

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            #print(a[k][i], end=" ")
            print(k,i)

        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            #print(a[i][n - 1], end=" ")
            print(i,n-1)

        n -= 1

        # Print the last row from
        # the remaining rows
        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                #print(a[m - 1][i], end=" ")
                print(m-1,i)

            m -= 1

        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                #print(a[i][l], end=" ")
                print(i,l)

            l += 1

def pb5_bc(): #Parcurgere in spirala
    n = int(input("Cititi n: "))
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])

    spiralPrint(n,n,a)


def pb7():
    m1 = {int(x) for x in input().split()}
    m2 = {int(x) for x in input().split()}
    reuniune = m1|m2
    intersectie = m1&m2
    print(reuniune)
    print(intersectie)

def pb8():
    n = int(input("Cititi n: "))
    v = [int(x) for x in input("Cititi n elemente: ").split()]
    for i in range(n-1):
        for j in range(i+1,n):
            if(v[i]+v[j]==0 and v[i]!=v[j]):
                print(v[i],v[j])

#SIRURI DE CARACTERE
def vocala(x):
    voc="aeiouAEIOU"
    if(voc.count(x)!=0):
        return 1
    return 0
def pbb4():
    text = input("Cititi textul: ")
    l = len(text)
    rez=""
    for i in range(l):
        if(vocala(text[i])==1):
            rez = rez + text[i]
            rez = rez + "p"
            rez = rez + text[i].lower()
        else:
            rez = rez + text[i]
    print(rez)

pbb4()
















