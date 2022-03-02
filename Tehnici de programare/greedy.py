#GREEDY
#PDF Suport Tehnici De Programare Moodle - Exmeple

'''Exemplu_1:
Se consideră mulţimea de valori reale A={a1,...,an}. Să se determine o
submulţime a lui A a cărei sumă a elementelor este maximă.
'''
#ideea e sa ordonam a-ul descrescator si sa punem elemente in vectorul de suma (s) cat timp sunt mai mari decat 0
#deoarece astfel vom avea suma maxima, daca nu exista elem pozitive atunci suma maxima este elementul cel mai mare.
def ex1():
    a = [int(x) for x in input().split()]
    s = []
    a.sort(reverse = True)
    s.append(a[0])
    for i in range(1, len(a)):
        if a[i]>0:
            s.append(a[i])
    print(s)

'''Exemplu_2
Se consideră mulțimea de valori reale A={a1,...,an} și k<n. Să se determine o
submulțime a lui A de cardinal k a cărei sumă a elementelor este maximă.
'''
#ideea e sa sortam vecorul descrescator si sa alegem dupa din el primele k elemente
def ex2():
    a = [int(x) for x in input().split()]
    k = int(input())
    n = len(a)
    a.sort(reverse = True)
    s = []
    for x in a:
        if k > 0:
            s.append(x)
        else:
            break
        k -= 1
    print(s)

'''A. Planificarea activităților cu minimizarea timpului mediu de așteptare
Avem n activități (comenzi date simultan de n clienți la un restaurant) care se desfășoară
utilizând o resursă comună (un bucătar care trebuie să execute comenzile, pe rând, câte una
sau un evaluator de proiecte care evaluează pe rând proiecte depuse, un procesor etc)
Știind durata fiecărei activități t1, t2,..., tn (cât îi ia bucătarului să facă fiecare comandă sau
evaluatorului să evalueze fiecare proiect), să se determine ordinea în care trebuie executate
activitățile astfel încât timpul mediu de așteptare să fie minim
'''
#ideea e sa sortam timpii si la fiecare pas sa luam activitatea care are cel mai scurt timp de desf, pt ca
#la ea se vor adauga toate celelalte mai departe
def exA():
    t = [int(x) for x in input().split()]
    aux = t.copy()
    n = len(t)
    ordine = []
    timp = 0
    aux.sort()
    for x in aux:
        timp += x
        ordine.append(t.index(x)+1)
    print(ordine)
    print(timp)

'''B. Planificarea unui număr maxim posibil de activități – Problema spectacolelor [2]
Variantă de enunț: Ştiind intervalele de desfăşurare a unor conferinţe la care dorim să asistăm
în timpul unei zile (sau emisiuni pe care dorim sa le vizionăm), să se determine numărul maxim
de conferințe la care putem participa (= cu intervale de desfășurare disjuncte).
6
Variantă de enunț cu intervale: Se consideră o mulțime A de intervale închise. Să se
determine o submulțime de cardinal maxim de intervale disjuncte din A
'''
#ideea e sa sortam crescator dupa timpul de finalizare, iar la fiecare pas este aleasa activitatea care
#se termina cel mai repede si este compatibilia cu celelalte activitati deja adaugate, adica mai exact
#activitatea care are timpul de de sfarsit cel mai mic si cel de inceput mai mare decat timpul de sfarsit
#al ultimei activitati adaugate
def exB():
    a = [int(x) for x in input().split()]
    n = len(a)
    intervale = []
    for i in range(0,n-1,2):
        t = (a[i],a[i+1])
        intervale.append(t)
    n = n // 2
    intervale.sort(key = lambda t:(t[1]))
    sol = [intervale[0]]
    us = intervale[0][1]
    for i in range(1, n):
        if intervale[i][0] > us:
            sol.append(intervale[i])
            us = intervale[i][1]
    print(sol)

'''C. Determinarea numărului minim de resurse necesare pentru a putea desfășura
toate activitățile – Problema partiționării intervalelor [2]
Să presupunem că avem n activităţi (spectacole) care pentru a se desfășura au nevoie de o
resursă (sală de spectacole). Această resursă poate fi folosită de o singură activitate la un
moment dat. Fiecare activitate i are un timp de start si şi un timp de terminare ti, deci se poate
desfășura doar în intervalul [si, ti). Astfel, pe o resursă se pot planifica doar activități cu
intervalele de desfășurare disjuncte. Să se determine numărul minim k de resurse (săli de
spectacole) de care este nevoie pentru a efectua toate activitățile (spectacolele) și o planificare
a acestor activități pe cele k resurse.
Exemplu: pentru n=3 spectacole, care trebuie să se desfășoare în intervalele: [10, 14), [12, 16),
respectiv [17, 18), sunt necesare 2 săli, o programare optimă fiind:
o Sala 1: [10, 14) – spectacolul 1, [17, 18) – spectacolul 3
o Sala 2: [12, 16) – spectacolul 2
Variantă de enunț cu intervale – Problema partiționării intervalelor: Se consideră o
mulțime A de intervale închise. Să se împartă (partiţioneze) această mulţime de intervale întrun număr 
minim de submulţimi cu proprietatea că oricare două intervale dintr-o submulţime nu se intersectează şi să 
se afişeze aceste submulţimi
'''
def exC():
    a = [int(x) for x in input().split()]
    n = len(a)
    intervale = []
    for i in range(0,n-1,2):
        t = (a[i], a[i+1])
        intervale.append(t)
    intervale.sort(key = lambda t: (t[0]))
    n = n // 2
    print(intervale)

#DARIA - TUTORIAT 7
'''Exemplul 1(Problema numerelor naturale prime și neprime)
Se dă un set de numere naturale și se cere alegerea a cel mult k (dat) numere prime și oricâte neprime, 
astfel încât suma celor prime să depășească suma celor neprime, iar numărul elementelor 
alese(prime și neprime) să fie maxim.
'''
def prim(x):
    if x <= 1 or x > 2 and x % 2 == 0:
        return 0
    for d in range(3, x, 2):
        if x % d == 0:
            return 0
    return 1

def d_ex1():
    nr = [int(x) for x in input().split()]
    k = int(input())
    prime = []
    neprime = []
    for x in nr:
        if prim(x) == 1:
            prime.append(x)
        else:
            neprime.append(x)
    prime.sort(reverse = True)
    neprime.sort()
    sol = []
    sp = 0
    for i in range(0,len(prime)):
        if k > 0:
            sol.append(prime[i])
            sp += prime[i]
            k -= 1
        else:
            break
    i = 0
    sn = 0
    while i < len(neprime) and sn < sp:
        if sn + neprime[i] < sp:
            sn += neprime[i]
            sol.append(neprime[i])
        i += 1
    print(sol)

'''Exemplul 2 (Medici)
O asociație caritabilă asigură consultații medicale gratuite pentru cei fără posibilități materiale. 
Există un singur cabinet dotat cu aparatură medicală, din acest motiv la un moment dat un singur medic 
poate face consultații. Asociația apelează la n medici de diverse specialități, care își oferă benevol 
serviciile.Fiecare prezintă un singur interval [si, fi] de-a lungul aceleiași zile, în care este disponibil. 
Ajutați asociația să realizeze o programare a consultațiilor în cabinet, astfel încât numărul demedici să fie maxim.
'''
def d_ex2():
    s = [int(x) for x in input().split()]
    intervale = []
    n = len(s)
    for i in range(0,n-1,2):
        j = i // 2 + 1
        t = (j, s[i], s[i+1])
        intervale.append(t)
    intervale.sort(key = lambda t : (t[2]))
    print(intervale)
    sol = {1}
    f = intervale[0][2]
    n = n // 2
    for i in range(1,n):
        s = intervale[i][1]
        if s > f:
            f = intervale[i][2]
            m = {intervale[i][0]}
            sol = sol | m
    print(sol)

#DARIA - TUTORIAT 8
'''Problemă (Stații)
Patronul unei companii private de transport în comun a primit de la primăria orașului aprobarea 
de a putea folosi o parte dintre stațiile Regiei Locale de Transport în comun. Stațiile disponibile
sunt plasate de-a lungul arterei principale a orașului.El hotărăște să introducăocursă rapidă care să
străbată orașul, de la un capăt la altul, pe artera principală. Pentru început se ocupă de stațiile 
situate de aceeași parte a drumului.Patronul are o dilemă: dacăopririle vor fi prea dese, atunci 
străbaterea orașului va dura prea mult și va plictisi călătorii, iar dacă stațiile sunt prea rare, 
călătorii vor fi prea puțini. De aceea, criteriile dupăcare patronul stabilește stațiile în care va opri 
cursa rapidă sunt:
între doua stații alăturate să fie cel puțin x metrii;
numărul total de stații săfie maxim.
'''
def statii():
    n, m = [int(y) for y in input().split()]
    s = [int(y) for y in input().split()]
    sol = []
    sum = 0
    sol.append(1)
    for i in range(n-1):
        sum += s[i]
        if sum > m:
            sum = 0
            sol.append(i+2)
    print(sol)


#DARIA EXAMEN PA GITHUB

#SUBIECTUL I
#a)
def litere(*cuv):
    dmare = {}
    for x in cuv:
        d = {}
        m = set(x)
        for lit in m:
            nr = x.count(lit)
            d[lit] = nr
        dmare[x] = d
    return dmare
#print(litere("teste", "programare"))

#b)
numere = [int(x) for x in range(10,100) if x % 6 != 0]
#print(numere)

#c) Complexitate

#SUBIECTUL II
def greedy():
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    apoz = [x for x in a if x > 0]
    aneg = [x for x in a if x < 0]
    bpoz = [x for x in b if x > 0]
    bneg = [x for x in b if x < 0]
    apoz.sort(reverse = True)
    bpoz.sort(reverse = True)
    aneg.sort()
    bneg.sort()
    s = 0
    m = len(a)
    na = len(apoz)
    nb = len(bpoz)
    i = 0
    j = 0
    while m and i < na and j < nb:
        s = s + apoz[i]*bpoz[j]
        i += 1
        j += 1
        m -= 1
    na = len(aneg)
    nb = len(bneg)
    i = 0
    j = 0
    while m and i < na and j < nb:
        s = s + aneg[i] * bneg[j]
        i += 1
        j += 1
        m -=1
    print(s)
greedy()



















