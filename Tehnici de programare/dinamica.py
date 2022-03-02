#PROGRAMRE DINAMICA
'''PB1
Subsecvența de sumă maximăa unui șir: Se dă un șir de numere(în fișier, separate prin spații).
Să se afișeze osubsecvenţăde sumă maximăa șirului (formată cu elemente consecutive)O(n)
'''
def pb1():
    f = open('date.in')
    ls = [int(x) for x in f.read().split()]
    f.close()
    n = len(ls)
    s = [None] * (n)
    s[0] = 0
    for i in range(1,n):
        s[i] = max(ls[i], s[i-1]+ls[i])
    maxi = 0
    for i in range(n):
        if s[i]>maxi:
            maxi = s[i]
            j = i
    rez = []
    while maxi != 0 and j >= 0:
        rez.append(ls[j])
        maxi -= ls[j]
        j -= 1
    print(rez[::-1])

'''PB_Extra
Se consideră vectorul a = (a1,..., an). 
Să se determine lungimea maximă a unui subşir crescător din a şi un astfel de subşir de lungime maximă
'''
def pb_extra_v1(): #cu predecesor
    f = open("sir.in")
    v = [int(x) for x in f.read().split()]
    f.close()
    n = len(v)
    lung = [0] * n
    pred = [-1] * n
    lung[0] = 1
    pred[0] = -1
    for i in range(1,n):
        max_lung = 0
        pred[i] = -1
        for j in range(0,i):
            if v[j] < v[i] and lung[j] > max_lung:
                max_lung = lung[j]
                pred[i] = j
        lung[i] = 1 + max_lung
    print(lung)
    print(pred)
    # solutia la pb = max din vectorul lung
    i_max = 0
    for i in range(1, n):
        if lung[i] > lung[i_max]:
            i_max = i
    print("lungimea maxima ", lung[i_max])
    rez = []
    while i_max != -1:
        rez.append(v[i_max])
        i_max = pred[i_max]
    print(rez[::-1])

def pb_extra_v2(): #cu succesor
    f = open("sir.in")
    v = [int(x) for x in f.readline().split()]
    f.close()
    n = len(v)
    lung = [0 for i in range(n)]
    succ = [-1 for i in range(n)]
    # lung[i] = lung max a unui subsir cresc care incepe pe pozitia i

    lung[n - 1] = 1
    succ[n - 1] = -1

    for i in range(n - 2, -1, -1):  # lung[i]=1+max{lung[j]|j>i si vj>vi}
        max_lung = 0
        succ[i] = -1
        for j in range(i + 1, n):
            if (v[j] > v[i]) and (lung[j] > max_lung):
                max_lung = lung[j]
                succ[i] = j
        lung[i] = 1 + max_lung

    print(lung)
    print(succ)

    # solutia la pb = max din vectorul lung
    i_max = 0
    for i in range(1, n):
        if lung[i] > lung[i_max]:
            i_max = i
    print("lungimea maxima ", lung[i_max])

    while i_max != -1:
        print(v[i_max], end=" ")
        i_max = succ[i_max]

'''PB2
Se consideră o tablă de șah nxm (n,m date). 
Pe fiecare careul al tablei este plasat câte un obiect, fiecare cu o anumită valoare (cunoscută, număr natural). 
Pe tablă se deplasează un robot astfel:  pornește de pe prima linie și prima coloană (un colț al tablei) și 
se poate deplasa numai în direcțiile sud și est. La parcurgerea unei celule robotul adună obiectul din celulă. 
Să se determine un traseu al robotului până în poziția (n, m) (până în colțul opus celui din care a plecat) 
astfel încât valoarea totală a obiectelor adunate să fie maximă. Se vor afişa valoarea totală obţinută şi 
traseul optim O(nm)
'''
def pb2():
    f = open("fis.in")
    s = f.read().split("\n")
    n, m = [int(x) for x in s[0].split()]
    mat = []
    for i in range(1,len(s)):
        ls = []
        for x in s[i].split():
            y = int(x)
            ls.append(y)
        mat.append(ls)
    sol = []
    for i in range(n):
        ls = [0] * m
        sol.append(ls)
    for i in range(n-1,-1,-1):
        for j in range(m-1, -1, -1):
            if i == n - 1:
                if j == m - 1:
                    sol[i][j] = mat[i][j]
                else:
                    sol[i][j] = mat[i][j] + sol[i][j+1]
            else:
                if j == m - 1:
                    sol[i][j] = mat[i][j]+sol[i+1][j]
                else:
                    sol[i][j] = max(mat[i][j] + sol[i + 1][j], mat[i][j]+sol[i][j+1])
    print(sol[0][0])
    i = 0
    j = 0
    while i < n - 1 and j < m - 1:
        if i == 0 and j == 0:
            print(i + 1,j + 1)
            j += 1
        else:
            if sol[i+1][j] > sol[i][j+1]:
                print(i + 2,j + 1)
                i += 1
                j = 0
            else:
                print(i + 1,j + 2)
                j += 1
    print(n,m)

#PROBLEME ALEXIA:

#Problema fazan
def ex1():
    f = open("Programare dinamica/date.in")
    sir = f.readline().split()
    f.close()
    print(sir)

    n = len(sir)
    lung = [0 for i in range(n)]
    succ = [-1 for i in range(n)]

    lung[n - 1] = 1
    for i in range(n - 2, -1, -1):  # i=n-2,n-3,...,0
        lung[i] = 1
        for j in range(i + 1, n):  # cuvintele de dupa i care se potrivesc cu cuvantul i
            if sir[i][-2:] == sir[j][:2]:
                if 1 + lung[j] > lung[i]:
                    lung[i] = 1 + lung[j]
                    succ[i] = j
    print(lung)
    print(succ)

    # det poz maximului din vectorul lung
    poz_max = 0
    for i in range(1, n):
        if lung[i] > lung[poz_max]:
            poz_max = i
    print("lungimea maxima subir fazan: ", lung[poz_max])
    while poz_max != -1:
        print(sir[poz_max], end=" ")
        poz_max = succ[poz_max]

#subsirul crescator maximal
def ex2():
    f = open("Programare dinamica/sir.in")
    v = [int(x) for x in f.readline().split()]
    f.close()
    n = len(v)
    lung = [0 for i in range(n)]
    succ = [-1 for i in range(n)]
    # lung[i] = lung max a unui subsir cresc care incepe pe pozitia i

    lung[n - 1] = 1
    succ[n - 1] = -1

    for i in range(n - 2, -1, -1):  # lung[i]=1+max{lung[j]|j>i si vj>vi}
        max_lung = 0
        succ[i] = -1
        for j in range(i + 1, n):
            if (v[j] > v[i]) and (lung[j] > max_lung):
                max_lung = lung[j]
                succ[i] = j
        lung[i] = 1 + max_lung

    print(lung)
    print(succ)

    # solutia la pb = max din vectorul lung
    i_max = 0
    for i in range(1, n):
        if lung[i] > lung[i_max]:
            i_max = i
    print("lungimea maxima ", lung[i_max])

    while i_max != -1:
        print(v[i_max], end=" ")
        i_max = succ[i_max]

#suma maxima care se poate obtine intr-o matrice pe un anumit traseu
def ex3():
    f = open("Programare dinamica/traseu.in")
    t = [[int(x) for x in linie.split()] for linie in f]
    f.close()
    n = len(t)
    s = [[0 for j in range(i + 1)] for i in range(n)]
    # s[i][j]=suma max care se poate obtine pornind din (i,j)

    # stim sa calculam direct ultima linie din s = ultima linie din t
    # s[n-1][:]=t[n-1] #ls[1:2]=[3,4]
    for i in range(n):
        s[n - 1][i] = t[n - 1][i]

    # calculam s de jos in sus
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            s[i][j] = t[i][j] + max(s[i + 1][j], s[i + 1][j + 1])

    print("solutii subprobleme: ")
    for linie in s:
        print(*linie)

    print("suma maxima este ", s[0][0])

    j = 0  # coloana
    for i in range(n - 1):  # linie
        print(f"({i + 1},{j + 1}) ", end="")
        if s[i + 1][j + 1] > s[i + 1][j]:
            j += 1
    print(f"({n},{j + 1}) ", end="")

#suma minima care se poate obtine intr-o matrice pe un anumit traseu
def ex4():
    n = int(input("nr coloane: "))
    m = int(input("nr linii: "))
    mat = [[int(x) for x in input("linia: ").split()] for i in range(m)]
    sol = mat
    start_i = 3
    start_j = 1
    v_poz = []
    i = 1
    for linie in sol[i:]:
        for j in range(len(linie)):
            if j != 0 and j != n - 1:
                sol[i][j] = mat[i][j] + min(sol[i - 1][j - 1], sol[i - 1][j], sol[i - 1][j + 1])
            elif j == 0:
                sol[i][j] = mat[i][j] + min(sol[i - 1][j], sol[i - 1][j + 1])
            elif j == n - 1:
                sol[i][j] = mat[i][j] + min(sol[i - 1][j], sol[i - 1][j - 1])
        if i < m - 1:
            i += 1
    i = 0
    for linie in sol[i:m - 1]:
        minim = min(linie)
        for j in range(len(linie)):
            if sol[i][j] == minim:
                v_poz.append([i, j])
        if i < m - 2:
            i += 1
    print(sol)
    v_poz.append([start_i, start_j])
    for x in reversed(v_poz):
        print(*x)
    minim = min(mat[m - 1])
    c = 0
    for x in mat[m - 1]:
        if x == minim:
            c += 1
    if c > 1:
        print("traseul nu e unic")




