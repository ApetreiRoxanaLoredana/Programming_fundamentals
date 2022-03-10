def divide(lista, lista_poz):
    if len(lista_poz) == 1:
        if lista_poz[0] % 2 == 0:
            return lista[lista_poz[0]]
        return 1
    m = len(lista_poz) // 2
    return divide(lista, lista_poz[:m]) * divide(lista, lista_poz[m:])

def aplica_divide(lista):
    lista_poz = []
    for i in range(len(lista)):
        lista_poz.append(i)
    return divide(lista, lista_poz)

def divide_prime(lista):
    if len(lista) == 1:
        if lista[0] < 2:
            return 0
        if lista[0] == 2:
            return 1
        if lista[0] % 2 == 0:
            return 0
        for i in range(3, lista[0] // 2 + 1, 2):
            if lista[0] % i == 0:
                return 0
        return 1
    m = len(lista) // 2
    return divide_prime(lista[:m]) + divide_prime(lista[m:])

def divide_max(lista):
    if len(lista) == 1:
        return lista[0]
    m = len(lista) // 2
    return max(divide_max(lista[:m]), divide_max(lista[m:]))


def divide(lista):
    if len(lista) == 1:
        return [lista[0]]
    m = len(lista) // 2
    return divide(lista[m:]) + divide(lista[:m])

print(divide([1, 2, 3, 4, 5, 6]))



