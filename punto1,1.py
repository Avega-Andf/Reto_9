if __name__ == "__main__":
    # Datos que usa la funcion
    C = int(input("ingrese la cantidad inicial de contagiados")) 
    D = float(input("ingrese la cantidad de dias a evaluar"))
    # Funcion lambda
    T = (lambda personas, dias: int(personas * (2 ** dias)))(C,D)
    print("La cantidad de contagiados en Nuncalandia despues de " + str(D) + " dias es: " + str(T)) #Se imprime