if __name__ == "__main__":
    # Datos que usa la funcion
    C = float(input("Ingresa el dinero incial prestado:"))
    I = float(input("Ingresa el interes:"))
    N = float(input("Ingresa la cantidad de meses:"))
    # Funcion lambda
    D = (lambda dineroinicial, interes, meses:dineroinicial * (1+ interes/100)**meses )(C,I,N)
    print("El dinero final es: " + str(D))