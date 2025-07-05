from alumnos import alumnos
from funciones import busqueda_lineal, insertion_sort

def main():
    nombre = input("Ingrese el nombre del alumno: ")

    nombres = list(alumnos.keys())
    indice = busqueda_lineal(nombres, nombre)

    if indice != -1:
        notas = alumnos[nombres[indice]]
        notas_ordenadas = insertion_sort(notas.copy())
        print(f"Notas de {nombres[indice]} ordenadas de menor a mayor:")
        for nota in notas_ordenadas:
            print(nota)
    else:
        print(f"No se encontraron notas para el alumno: {nombre}.")

if __name__ == "__main__":
    main()