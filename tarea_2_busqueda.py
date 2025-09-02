def localizar(lista, buscado):
    contador = 0
    for elemento in lista:
        contador += 1
        if elemento == buscado:
            break  # Se detiene al encontrar el número :3
    return contador


def main():
    tamaño = int(input("Tamaño del arreglo: "))
    numeros = []

    print(f"Ingrese {tamaño} números:")
    for _ in range(tamaño):
        numeros.append(int(input()))

    objetivo = int(input("Ingresa el número a localizar: "))

    intentos = localizar(numeros, objetivo)
    print("Comparaciones realizadas:", intentos)


if __name__ == "__main__":
    main()
