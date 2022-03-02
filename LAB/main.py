import math

def interschimbare():
    x=input("Cititi x: ")
    y=input("Cititi y: ")
    x=int(x)
    y=int(y)
    x=x^y
    y=x^y
    x=x^y
    print(x)
    print(y)

def pb_2():
    x=int(input("Cititi x: "))
    if x&(x-1)==0:
        k=0
        while x!=1:
            x=x>>1
            k+=1
        print("Numarul este 2 la puterea ",k)
    else:
        print("Numarul nu este de forma 2 la puterea k")

def pb_4_shiftare():
    x = int(input("Cititi x: "))
    n = int(input("Cititi n: "))
    prima_jumatate = x%(1<<n)
    a_doua_jumatate = x>>(n+1)
    rezultat=a_doua_jumatate<<n ^ prima_jumatate
    print(rezultat)

def pb_5():
    n=int(input("Cititi n: "))
    k=0
    k=int(k)
    print(bin(n))
    while n:
        if n%2==1 :
            k+=1
        n = n // 2
    print(k)

def pb_7():
    n=int(input("Cititi n: "))
    aux=n
    invers=0
    invers=int(invers)
    while aux!=0:
        invers=invers*10 + aux%10
        aux=aux//10
    if invers==n:
        print("Numarul este palindrom")
    else:
        print("Numarul nu este palindrom")

def pb_8():
    n=int(input("Cititi n: "))
    x=float(input("x= "))#citim prima zi
    z=0
    maxi=0
    for i in range(n-1):
        y=float(input("y= "))#citim restul zilelor
        dif=y-x
        if dif>maxi:
            maxi=dif
            z=i
        x=y
    print(maxi,z+1,z+2) #+1 si +2 la zi pt ca indexarea pleaca de la 0

def pb_9_diferenta():
    L1 = int(input("Cititi L1: "))
    L2 = int(input("Cititi L2: "))
    x = L1
    y = L2
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    l = x
    AriaBucatarie = L1 * L2
    AriaGresie = l * l
    NrBuc = AriaBucatarie // AriaGresie
    print(NrBuc)

def pb_9_impartire():
    L1 = int(input("Cititi L1: "))
    L2 = int(input("Cititi L2: "))
    a=L1
    b=L2
    while b!=0:
        r=a%b
        a=b
        b=r
    l=a
    AriaBucatarie=L1*L2
    AriaGresie=l*l
    NrBuc=AriaBucatarie//AriaGresie
    print(NrBuc)

def pb_10_ecuatie_de_grad_2():
    a = int(input("Cititi a: "))
    b = int(input("Cititi b: "))
    c = int(input("Cititi c: "))
    delta = b**2 - 4*a*c
    if delta>0:
        radical = math.sqrt(delta)
        rad1 = ((-1) * b + radical)/ (2 * a)
        rad2 = ((-1) * b - radical) / (2 * a)
        print("Ecuatia are doua radacini: " ,rad1, rad2)
    else:
        if delta==0:
            radical = math.sqrt(delta)
            rad = ((-1) * b + radical) / (2 * a)
            print("Ecuatia are o singura radacina: ", rad)
        else:
            print("Ecuatia nu are solutii")

def pb_11():
    a=int(input("Cititi a: "))
    b=int(input("Cititi b: "))
    for i in range(b,a-1,-1):
        nr=0
        x=i
        for d in range (2, x//2+1):
            if x%d==0:
                nr+=1
        if nr==0:
            print (i)
            break
    else:
        print ("Nu exista niciun numar prim in intervalul [a,b]")

def pb_12(): #nu stiu daca are numar minim de comparatii(adica nu are)- trebuie gandit ceva mai eficient
    n=int(input("Cititi n: "))
    x = int(input("Cititi x: "))
    maxi=x
    mini=x
    for i in range(1,n):
        y = int(input("Cititi y: "))
        if y>maxi:
            maxi=y
        if y<mini:
            mini=y
    print("Minimul este: ", mini)
    print("Maximul este: ", maxi)

def pb_12_eficient_cu_vector():
    n = int(input("Cititi n: ")) #nr elementelor din vector
    l = [] #se declara vectorul
    lmaxmin = [0, 0] #se declara un vector de doua elem: pe prima poz va fi max pe a doua min
    for i in range(0, n, 1): #se face citirea
        a = int(input("Cititi a: ")) #se citeste cate un element
        l.append(a) #se baga in vector

    def divide(st, dr, l, lmaxmin): #se face divide et impera pentru a afla minimul si maximul
                                       #pt a folosi un numar minim de comparatii
        if (dr == st):
            lmaxmin[0] = l[st]
            lmaxmin[1] = l[dr]
            return lmaxmin
        mij = (st + dr) // 2
        l1 = [0, 0]
        l2 = [0, 0]
        l1 = divide(st, mij, l, l1)
        l2 = divide(mij + 1, dr, l, l2)
        lmaxmin[0] = max(l1[0], l2[0])
        lmaxmin[1] = min(l1[1], l2[1])
        return lmaxmin

    lmaxmin = divide(0, n - 1, l, lmaxmin) #apelam functia de divide pt tot vectorul
    print(lmaxmin) #afisam maximul si minimul

pb_12_eficient_cu_vector()