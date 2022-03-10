def Cautare_Secventiala(element, lista):
    """
    Cauta un element in lista
    Returneaza elementul sau -1
    daca nu gaseste elementul
    """
    poz = -1
    for i in range(len(lista)):
        if element == lista[i]:
            poz = i
    return poz


def Cautare_Succesiva(element, lista):
    i = 0
    while i < len(lista) and element != lista[i]:
        i += 1
    if i < len(lista):
        return i
    return -1


def Cautare_Binara(element, lista, left, right):
    if left >= right - 1:
        return right
    m = (left + right) // 2
    if element <= lista[m]:
        return Cautare_Binara(element, lista, left, m)
    else:
        return Cautare_Binara(element, lista, m, right)

def Cautare_Binara_Recursiva(element, lista):
    if len(lista) == 0:
        return 0
    if element < lista[0]:
        return 0
    if element > lista[len(lista)-1]:
        return len(lista)
    return Cautare_Binara(element, lista, 0, len(lista))

def Cautare_Binara_Iterativa(element, lista):
    if len(lista) == 0:
        return 0
    if element <= lista[0]:
        return 0
    if element >= lista[len(lista) - 1]:
        return len(lista)
    right = len(lista)
    left = 0
    while right - left > 1:
        m = (left+right)//2
        if element <= lista[m]:
            right = m
        else:
            left = m
    return right
            