def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista)//2]
        menores = [x for x in lista if x < pivot]
        iguais = [x for x in lista if x == pivot]
        maiores = [x for x in lista if x > pivot]
        return quicksort(menores) + iguais + quicksort(maiores)

lista = [65, 5, 2, 7, 28, 9, 15, 3, 98]
lista_ordenada = quicksort(lista)
print(lista_ordenada)