def calcularcontagiados(*args)-> int:
    # args[0] y args[1] es el elemento 1 y 2 de la tupla que en este caso seria:
    # C (cantidad inicial de contagiados) y D (Dias a evaluar) respectivamente
    contagiados =int(args[0] * (2 ** args[1]))
    return contagiados

if __name__ == "__main__":
    C = int(input("ingrese la cantidad inicial de contagiados"))
    D = float(input("ingrese la cantidad de dias a evaluar"))
    # Se asignan los valores a usar a la funcion
    T = calcularcontagiados(C,D)
    print("La cantidad de contagiados en Nuncalandia")