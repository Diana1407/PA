def pareimpare(*ls):
    n = len(ls)
    d = {}
    for i in range(n):
        pare = [x for x in ls[i] if x % 2 == 0]
        impare = [x for x in ls[i] if x % 2 == 1]
        l = []
        l.append(impare)
        l.append(pare)
        d[i] = l
    print(d)
#pareimpare([1, 1, 2, 3, 4], [0, 2], [1, 2, 3])

#numere = [x for x in range(100,1000) if x % 5 != 0 and x % 10 == x // 100]
#print(numere)

#SUBIECTUL II
'''La ora de sport, profesorul vrea să execute exerciții de gimnastică cu grupe de câte 2 elevi,
dar pentru a putea realiza acest lucru trebuie ca valoarea absolută a diferenței dintre
înălțimile celor 2 elevi dintr-o grupă să fie strict mai mică decât un număr natural h.
Scrieți un program Python care citește de la tastatură numele și înălțimile a n elevi și
afișează pe ecran, în forma indicată în exemplu, numărul maxim de grupe formate din
câte 2 elevi care se pot forma respectând condiția indicată anterior, precum și numele
elevilor din grupele respective. Evident, un elev poate să facă parte din cel mult o grupă!
Înălțimile tuturor elevilor și diferența h sunt exprimate în centimetri. Nu contează
ordinea în care se vor afișa grupele de elevi și nici ordinea numelor elevilor dintr-o grupă.
Dacă nu se poate forma nicio grupă de 2 elevi cu proprietatea cerută se va afișa un mesaj
corespunzător.
8
10
Popescu Ion 172
Mihai Ana 162
Popescu Dana 190
Ionescu Ion 181
Georgescu Ioana 170
Dumitrescu George 188
Constantinescu Radu 165
Georgescu Anca 210'''
def greedy():
    n = int(input())
    h = int(input())
    ls = []
    for i in range(n):
        s = input().split()
        nume = s[0] + " " + s[1]
        inaltime = int(s[2])
        l = [nume,inaltime]
        ls.append(l)
    ls.sort(key = lambda t : (t[1]))
    rez = []
    for i in range(n-1):
        if ls[i+1][1] - ls[i][1] < h:
            if ls[i][0] not in rez and ls[i+1][0] not in rez:
                rez.append(ls[i][0])
                rez.append(ls[i+1][0])
    print(len(rez) // 2)
    for i in range(0,len(rez),2):
        print(rez[i],rez[i+1],sep = ", ")

#SUBIECTUL IV
'''
6
lslsll
a b c D
@ .
'''
def back(k):
    global nr
    if k == n :
        if x[0] in "aeiouAEIOU":
            print(*x, sep = "")
            nr += 1
    else:
        if T[k] == 'l':
            for i in range(len(L)):
                if L[i] not in x:
                    x[k] = L[i]
                    back(k+1)
                    x[k] = 0
        else:
            for i in range(len(S)):
                if S[i] not in x:
                    x[k] = S[i]
                    back(k+1)
                    x[k] = 0

nr = 0
#n = int(input())
#T = input()
#L = [i for i in input().split()]
#S = [i for i in input().split()]
#x = [0 for i in range(n)]
#back(0)
#print(nr)


p=int(input("p="))
contor = 0
st = [0 for _ in range(p)]


def divizor(i):
    if p % i == 0:
        return True
    return False


def valid(k):
    for i in range(k):
        if st[i] > st[k]:
            return False

    if sum(st[:k + 1]) <= p:
        return True
    return True


def afisare(k):
    global contor
    if st[0] != st[len(st) - 1] and st.count(st[0]) + st.count(st[len(st) - 1] == len(st)):
        rez = '+'.join([str(x) for x in st[:k + 1]])
        contor += 1
        print(rez)


def back(k):
    for i in range(1, p):
        if divizor(i):
            st[k] = i
            if valid(k):
                if sum(st[:k + 1]) == p:
                    afisare(k)
                elif sum(st[:k + 1]) < p:
                    back(k + 1)


back(0)
print('nr modalitati')
print(contor)
