def max(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)

max(1,33,3)

def vocale(a):
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
        print(str(a) + " è una vocale")
    else:
        print(str(a) + " è una consonante")

vocale("a")

list = list()
def sommatrice(list):
    sum = 0
    for i in list:
        sum +=i
    print("la somma è ",sum)

list = [1,2,3]
sommatrice(list)


def moltiplicatrice(list):
    moltip = 1
    for i in list:
        if i !=0:
            moltip *=i
    print("la moltip è ",moltip)

list = [2,2,2]
moltiplicatrice(list)

parola= ""
def reverser(parola):
    print(parola[::-1])

reverser("ciao")

stringa = ""
def palindromo(stringa):
    if stringa == stringa[::-1]:
        print(str(stringa) + " è un palindromo")
    else:
        print(str(stringa) + " non è un palindromo")

palindromo("alna")

lista = []
def lunghezza(lista):
    counter = 0
    for i in lista:
        if counter <= i:
            counter = counter + 1
    print(counter)

lista = [1,3,4,88,55,302]
lunghezza(lista)

ist = []
def istogrammi(ist):
    for i in ist:
        i = i * '*'
        print(i)

ist = [2,7,5]
istogrammi(ist)


listaA = []
listaB = []
def lunghezzaAB(listaA):
    for i in listaA:
            listaB.append(len(i))
    print(listaB)

lista = ["uno", "due", "tre"]
lunghezzaAB(lista)

