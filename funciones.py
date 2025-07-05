def busqueda_lineal(lista, objetivo):
    objetivo = objetivo.lower()
    for i in range(len(lista)):
        if lista[i].lower() == objetivo:
            return i
    return -1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


