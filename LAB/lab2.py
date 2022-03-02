def pb_1():
    s1=input("Cititi sirul: ")
    k=int(input("Cititi k: "))
    s2=s1[:k]+s1[k+1:]
    print(s2)

def pb_2():
    s = input("Cititi cuvantul: ")
    l=s[0]
    s2=s.replace(l,'')
    print("dupa stergerea literei ", l, " sirul obtinut este ", s2, " de lungime", len(s2))

def pb_3_v1():
    s = input("Cititi cuvantul: ")
    i=0
    j=len(s)
    while i<j:
        s1=s[i:j]
        i=i+1
        j=j-1
        print(s1.center(10))

def pb_3_v2():
    s = input("Cititi cuvantul: ")
    while s != "":
        print(s.center(10))
        s=s[1:len(s)-1]

def pb_4():
    s = input("Cititi sirul: ")
    jumatatea_sirului = (len(s) // 2) + 1
    for k in range(1, jumatatea_sirului):
        if len(s) % k == 0:
            nr_secvente = len(s) // k
            if s[:k] * nr_secvente == s:
                t = s[:k]
    print(t)

def rimeaza(cuv1, cuv2, p):
    if cuv1[-p:]==cuv2[-p:]:
        return 1
    return 0

import re

def pb_5():
    cuvant_ref =input("Cititi w: ")

    text = input("Cititi propozitia: ")
    #Promotions and demotions to and from the index occur quarterly in March, June, September, and December, The Index is calculated in real-time and published every minute
    p=int(input("Citit p: "))
    p = 3
    cuvinte = re.split(',| ',text)
    for cuvant in cuvinte:
        if rimeaza(cuvant_ref, cuvant.lower(), p):
            print(cuvant)

def pb_6_a():
    text=input("Cititi propozitia: ")
    g=input("Cititi greselile: ")
    greseli=g.split()
    c=input("Cititi corectarile: ")
    corectari=c.split()
    for i in range(0,len(greseli)):
        text=text.replace(greseli[i],corectari[i])
    print (text)

def pb_6_b():
    text=input("Cititi propozitia: ")
    g=input("Cititi greselile: ")
    greseli=g.split()
    c=input("Cititi corectarile: ")
    corectari=c.split()
    nr=0
    for i in range(0,len(greseli)):
        if(text.count(greseli[i]))>10:
            text=text.replace(greseli[i],corectari[i],10)
        elif (text.count(greseli[i])>0 and nr+text.count(greseli[i])<=10):
            text=text.replace(greseli[i],corectari[i])
            nr=nr+text.count(greseli[i])
        elif text.count(greseli[i])>0:
            aux=nr
            while aux<=10:
                aux=aux+1
                text = text.replace(greseli[i], corectari[i],1)
            nr = nr + text.count(greseli[i])
    if nr>10:
        print("textul contine prea multe greseli, doar 10 au fost corectate")
        print (text)
    else:
        print(text)

def pb_7_v1_strica_sirul():
    text = input("Cititi sirul de caractere: ")
    nou=text.split()
    for i in range(0,len(nou)):
        nou[i]=nou[i].capitalize()
    print(nou)

def pb_7_v2():
    text = input("Cititi sirul de caractere: ")
    text=text.title()
    print (text)

def pb_8():
    cod=input("Cititi codul: ")
    text=''
    for i in range (0,len(cod)):
        if(cod[i]>='0' and cod[i]<='9'):
            if (cod[i+1] >= '0' and cod[i+1] <= '9'):
                c1=int(cod[i])
                c2=int(cod[i+1])
                x=c1*10+c2
                text=text+cod[i+2]*x
            else:
                c1 = int(cod[i])
                text = text + cod[i + 1] * c1
    print(text)

def pb_9():
    text=input("Cititi propozitia: ")
    s=input("Cititi cuvantul pe care vreti sa il inlocuiti: ")
    t=input("Cititi cuvantul cu care vreti sa inlocuiti: ")
    text=text.replace(s,t)
    print(text)

def pb_10():
    text = 'Astăzi am cumpărat pâine de la piata 3 de 5 RON, pe lapte am dat 10 RON, iar de 15 RON am cumpărat niște cașcaval. De asemenea, mi-am cumpărat și niște papuci cu 50 RON!'
    suma = 0
    matches = re.findall(r'\d+ RON', text)
    # pattern unde apare cel putin o cifra, un spatiu, apoi string-ul RON
    for match in matches:
        plata,_ = match.split() # unpaching variables
        suma += int(plata)
    print(f"Suma totala de {suma} RON")

def pb_11(): #de revazut si refacut
    text = "Ionescu Ion-Andrei a fost la tara si s-a intors ieri, impreuna cu Popescu-Marin George. A venit cu masina lui Ionescu-Popescu Ion-Andrei"

    naming_pattern = r"[A-Z][a-z]{2,}(\-[A-Z][a-z]{2,}){0,}"
    naming_regex = rf"{naming_pattern}"

    matches = re.findall(naming_regex, text)
    print(matches)

    input_decide = 'Ionescu Ion-Andrei'
    decide_match = re.match(naming_regex, input_decide)

    if decide_match.start() == 0 and decide_match.end() == len(input_decide):
        print("Nume corect")
    else:
        print("Nume incorect")


pb_11()
