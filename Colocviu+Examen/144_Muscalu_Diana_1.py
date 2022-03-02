# Muscalu Diana, 144

#Fișierul text text.in conține pe prima linie un cuvânt w nevid format din litere mici ale
#alfabetului englez, iar pe următoarele linii un text în care cuvintele sunt despărțite prin spații
#și semnele de punctuație uzuale. Să se scrie în fișierul text 𝑡𝑒𝑥𝑡. 𝑜𝑢𝑡 toate cuvintele din fișierul
#𝑡𝑒𝑥𝑡. 𝑖𝑛 care au mulțimea literelor inclusă în mulțimea literelor cuvântului 𝑤 sau mesajul
#"𝐼𝑚𝑝𝑜𝑠𝑖𝑏𝑖𝑙" dacă în fișierul de intrare nu există nici un cuvânt cu proprietatea cerută,
#conform modelului din exemplul de mai jos. Cuvintele vor fi scrise grupat, în funcție de
#mulțimile literelor. Grupele vor fi scrise în ordine lexicografică, iar în cadrul fiecărui grup
#cuvintele vor fi scrise în ordinea descrescătoare a lungimilor lor. Fiecare cuvânt va fi scris o
#singură dată și nu se va face distincție între litere mici și litere mari.

f = open("text.in")
s = f.read()
s = s.split("\n")
print(s)
cuv = s[0]
dict = {}
for i in range (1, len(s)):
    ls = s[i].split()
    for x in ls: #x este cuvantul pe care trebuie sa il verific
        xx = x.lower()
        m = set(xx)
        ok = 1
        for y in m:
            if y not in cuv:
                ok = 0
                break
        if ok == 1:
            d = dict.get(xx)
            if d == None:
                dict[xx] = x
            else:
                l= []
                for y in d:
                    l += y
                print(l)
                dict[xx] = l
print(dict)


