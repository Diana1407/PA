#LABORATOR 4

#Problema_9
def numar(*lista):
    ls = [int(x) for x in lista]
    nr = 0
    for x in ls:
        maxi = -1
        while(x != 0):
            if(x%10 > maxi):
                maxi = x%10
            x = x // 10
        nr = nr * 10 + maxi
    return nr

def pb_9a():
    print(pb_9a(4251, 73, 8, 133))

def pb_9b(a, b, c):
    b2 = numar(a,b,c)
    if b2 == 111:
        print("True")
    else:
        print("False")
pb_9b(1001, 17, 100)

#Problema_10

