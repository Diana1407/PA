#Exercitii setul 1 - numere
def pb_1():
    a = float(input("Cititi a: "))
    b = float(input("Cititi b: "))
    c = float(input("Cititi c: "))

    if (a*b==c*c or a*c==b*b or b*c==a*a):
        print("Numerle pot fi laturile unui triunghi.")
    else:
        print("Numerle nu pot fi laturile unui triunghi.")

def pb_2():
    x = int(input("Cititi numarul: "))
    i=1
    while (i*i*i<x):
        i+=1
    if(i*i*i==x):
        print("Numarul este cub perfect")
    else:
        print("Numarul nu este cub perfect")

def pb_3():
    n = int(input("Cititi n: "))
    if n%2==1:
        print("Weird")
    else:
        if(n>=2 and n<=5):
            print("Not Weird")
        elif (n>=6 and n<=20):
            print("Weird")
        elif n>20:
            print("Not Weird")

def prim(x):
    if (x<=1 or (x>2 and x%2==0)):
        return 0
    for i in range(3,x//2,2):
        if x%i==0:
            return 0
    else:
        return 1

def pb_4():
    a = int(input("Cititi a: "))
    b = int(input("Cititi b: "))
    for i in range (a,b+1):
        if prim(i)==1:
            print(i)
            break
    else:
        print("Nu exista un numar prin in interval")

def nr_div(x):
    nr=0
    for i in range(1,x+1):
        if (x%i==0 and prim(i)==1):
            nr+=1
    return nr

def pb_5():
    a = int(input("Cititi a: "))
    b = int(input("Cititi b: "))
    maxi=-1
    for i in range(a,b+1):
        if(nr_div(i)>maxi):
            maxi=nr_div(i)
    for i in range(a,b+1):
        if(nr_div(i)==maxi):
            print(i)

def pb_6_citire1():
    n = int(input("Cititi n: "))
    v=[]
    for i in range(0,n):
        x=int(input("Cititi elem: "))
        v.append(x)
    min1=v[0]
    min2=v[1]
    if min1>min2:
        aux=min1
        min1=min2
        min2=aux
    #min1 retine cel mai mic numar
    #min2 retine al doilea cel mai mic numar
    for i in range(2,n):
        if v[i]<min1:
            min2=min1
            min1=v[i]
        elif v[i]<min2:
            min2=v[i]
    if min1!=min2:
        print(min1,min2)
    else:
        print("Nu se poate")

def pb_6_citire2():
    n = int(input("Cititi n: "))
    v = input("dati vectorul: ").split() #citesc pe o linie ca sir de carc si despart
    v = [int(x) for x in v] #fac conversie la tipul int
    min1 = v[0]
    min2 = v[1]
    if min1 > min2:
        aux = min1
        min1 = min2
        min2 = aux
    # min1 retine cel mai mic numar
    # min2 retine al doilea cel mai mic numar
    for i in range(2, n):
        if v[i] < min1:
            min2 = min1
            min1 = v[i]
        elif v[i] < min2:
            min2 = v[i]
    if min1 != min2:
        print(min1, min2)
    else:
        print("Nu se poate")

import math
def pb_7():
    x = int(input("Cititi x: "))
    if x<=-9:
        print(x*(-1))
    elif (x>-9 and x<0):
        print(math.sqrt(x+9))
    elif (x>=0 and x<=10):
        print(x*x)

#Exercitii setul 2 - siruri de caractere
def pb1():
    s1 = input("Cititi s1: ")
    s2 = input("Cititi s2: ")
    l1=len(s1)
    l2=len(s2)
    if(l1<l2):
        mini=l1
    else:
        mini=l2
    s3=""
    for i in range(0,mini):
        s3=s3+s1[i]
        s3=s3+s2[(-1)*i-1]
    if(mini!=l1):
        for i in range(mini,l1):
            s3=s3+s1[i]
    elif (mini != l2):
        for i in range(mini, l2):
            s3 = s3 + s2[i]
    print(s3)

def pb2():
    s1 = input("Cititi s1: ")
    s2 = input("Cititi s2: ")
    print(s1.count(s2))

def pb3():
    s=input("Cititi sirul: ")
    suma=0
    prod=1
    nr=0
    for i in range(0,len(s)):
        if (s[i]>='0' and s[i]<='9'):
            suma=suma+int(s[i])
            prod=prod*int(s[i])
            nr+=1
    print(f"suma este {suma}, produsul este {prod} iar media aritmetica este {suma//nr}")

import string
def pb4():
    sir = "/*Is it an #$% important @ day ?!"
    print(sir)
    sir_aux = string.punctuation #genereaza un sir cu toate semnele de punctuatie
    print(sir_aux)
    for char in sir_aux: #ne plimbam prin semenele de punctuatie si daca apar in sirul
                        #nostru, le inlocuim cu *
        sir = sir.replace(char, '*')
    print(sir)

def pb5():
    sir = input("Cititi sirul: ")
    s = "Care"
    l = len(s)
    s = s[:(l//2)] + sir + s[(l//2):]
    print(s)

def pb6_v1(): #face toate literele din sir mici(daca ar fi litere mari la mijloc nu mai
    # merge pt problema data pt ca le modifica si pe alea)
    s = input("Cititi sirul: ")
    s = s.lower()
    print(s)

def pb6_v2():
    s = input("Cititi sirul: ")
    sir=""
    sir = sir + s[0].lower()
    for i in range(1,len(s)):
        if s[i-1]==" " and s[i].isupper():
            sir = sir + s[i].lower()
        else:
            sir = sir + s[i]
    print(sir)

def pb7():
    s = input("Cititi sirul: ")
    rez = ""
    for i in range(len(s)):
        if i%2==0:
            rez = rez + s[i]
    print(rez)

def pb8_v1():
    a = 3.1415987
    b = 14.99999
    print(round(a,2))
    print(round(b,2))

def pb8_v2():
    a = 3.1415987
    b = 14.99999
    print(f"{a:.2f}")
    print(f"{b:.2f}")

def pb10():
    s1 = input("Cititi primul sir: ")
    s2 = input("Cititi al doilea sir: ")
    s = ""
    if s1[len(s1)-1] == s2[0]: # sau s1[len(s1)-1] == s1[-1]
        s = s1[0:len(s1) - 1]
        s = s + s2
    else:
        s = s + s1 + s2
    print(s)

#Exercitii setul 3 - liste
def p_1_v1():
    n = int(input("Cititi n: "))
    ls = [int(i) for i in input("Cititi nr: ").split()]
    x = int(input("Cititi x: "))
    nr = 0
    if ls.count(x)>0:
        nr = 1
        while(ls.count(x)>0):
            ls.remove(x)
        print(ls)
    if nr==0:
        print(f"Nu exista valoarea {x} in lisa")

def p_1_v2():
    n = int(input("n= "))
    lista = []
    for i in range(n):
        lista.append(int(input("elem=")))
    print(lista)
    y = int(input("y = "))
    ls = [x for x in lista if x != y]
    print(ls)

def p_2():
    l_original = [1, 2, [3, [4, 5, [6, 7], 11], 12], 13, 14]
    l_add = [8, 9, 10]
    l_original[2][1][2].extend(l_add)
    print(l_original)

def p_3_a():
    ls=[int(x) for x in range(2,25,2)]
    print(ls)

def p_3_b():
    n = int(input("Cititi n: "))
    ls = [int(x) if x % 2 == 0 else -x for x in range(1, n + 1)]
    print(ls)

def p_3_c():
    ls1 = [int(x) for x in input("Cititi lista: ").split()]
    l=len(ls1)
    ls2=[]
    for i in range(0,l,2):
        ls2.append(ls1[i])
    print(ls2)

def p_3_d():
    lista = [2, 4, 5, 8, 10, 15]
    lista_rez = [lista[x] for x in range(len(lista)) if x % 2 != lista[x] % 2]
    print(lista_rez)

def p_3_e():
    n = int(input("Cititi n: "))
    ls = [[] if l == 0 else [l] * l for l in range(n)]
    print(ls)

def sum_cif(x):
    s = 0
    while x>0:
        s += x%10
        x = x//10
    return s

def p_4():
    n = int(input("Cititi n: "))
    ls = [int(x) for x in input("Cititi lista: ").split()]
    par = []
    impar = []
    for x in ls:
        if sum_cif(x)%2==0:
            par.append(x)
        else:
            impar.append(x)
    par.sort(reverse = True)
    impar.sort(reverse=False)
    par = par + impar
    print(par)

def p_5():
    m = int(input("Cititi m: "))
    n = int(input("Cititi n: "))
    x = int(input("Cititi x: "))
    a=[]
    for i in range(m):
        a.append([x*j for j in range(i*n,(i+1)*n)])

    for linie in a:
        for y in linie:
            print(f"{y:4}", end="")
        print()

    smax = -1
    for j in range(n):
        s = 0
        for i in range(m):
           s += a[i][j]
        if s>smax:
            smax = s
            jmax = j
    print(f"Suma maxima este {smax} pe coloana {jmax}")

def p_5_c():
    #Matrice nxn
    n = int(input("Cititi n: "))
    a=[]
    for i in range(n):
        a.append([int(x) for x in input().split()])
    sprinc = 0
    for i in range(n):
        sprinc += a[i][i]
    print(f"Suma de pe diag princ este {sprinc}")

    psec = 1
    for i in range(n):
        psec *= a[i][n-1-i]
    print(f"Produsul de pe diag secundara este {psec}")

    simp = 0
    for i in range(1,n):
        for j in range(0,i):
            if a[i][j]%2==1:
                simp += a[i][j]
    for i in range(n-1):
        for j in range(i+1,n):
            simp += a[i][j]
    print(f"Suma elem impare de sub si deasupra diag princ este {simp}")

p_5_c()
