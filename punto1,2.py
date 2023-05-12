if __name__ == "__main__":
    # Datos que usa la funcion lambda
    P=float(input("Ingrese la cantidad de panes que te pidieron comprar:"))
    M=float(input("Ingrese la cantidad de bolsas de leche que te pidieron comprar:"))
    H=float(input("Ingrese la cantidad de huevos que te pidieron comprar:"))
    B=float(input("Ingresa la cantidad de dinero que te dieron"))
    # Funcion
    G = (lambda panes, leche, huevos, dinero: dinero - 300*panes - 3300 * leche - 350*huevos)(P, M, H, B)
    # Parametros para imprimir si debe, si le sobra o si pago exactamente
    if G>0:
        print("La cantidad que te sobra es " +str(G)+ " pesos" )
    elif G<0:
        print("la cantidad que te falta es: " +str(-G)+ " pesos") 
    else:
        print("No te sobra ni te falta nada de dinero")