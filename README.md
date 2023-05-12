# Reto 9

### 1. De los retos anteriores seleciones 3 funciones y escribalas en forma de lambdas.
 ##### El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.


<details><summary>codigo</summary><p>

``` python
if __name__ == "__main__":
    # Datos que usa la funcion
    C = int(input("ingrese la cantidad inicial de contagiados")) 
    D = float(input("ingrese la cantidad de dias a evaluar"))
    # Funcion lambda
    T = (lambda personas, dias: int(personas * (2 ** dias)))(C,D)
    print("La cantidad de contagiados en Nuncalandia despues de " + str(D) + " dias es: " + str(T)) #Se imprime
```
</p></details></br>

 ##### Mi mamá me manda a comprar `P` panes a 300 cada uno, `M` bolsas de leche a 3300 cada una y `H` huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de `B` pesos.


<details><summary>codigo</summary><p>

``` python
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
```
</p></details></br>

 ##### Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

<details><summary>codigo</summary><p>

``` python
if __name__ == "__main__":
    # Datos que usa la funcion
    C = float(input("Ingresa el dinero incial prestado:"))
    I = float(input("Ingresa el interes:"))
    N = float(input("Ingresa la cantidad de meses:"))
    # Funcion lambda
    D = (lambda dineroinicial, interes, meses:dineroinicial * (1+ interes/100)**meses )(C,I,N)
    print("El dinero final es: " + str(D))
```
</p></details></br>

### 2. De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).
 ##### Dada la figura desarolle: Una función matemática para calcular el área y el perimetro, funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
 
<details><summary>codigo</summary><p>

``` python
import math
#Para el rectangulo
def calcular_area_rectangulo(*args) -> float:
  # args[0] y args[1] son el primer y segundo valor ingresado en la tupla con args respectivamente
  # En este caso son base y altura
  area_rectangulo = args[0]*args[1] 
  return area_rectangulo

def calcular_perimetro_rectangulo(*args) -> float:
  # args[0] y args[1] son el primer y segundo valor ingresado en la tupla con args respectivamente
  # En este caso son base y altura
  perimetro_rectangulo = 2*args[0]+2*args[1]
  return perimetro_rectangulo

#Para los circulos
def calcular_area_circulos(*args) -> float:
  # args[0] es el primer valor ingresado en la tupla con args 
  # # En este caso es el radio
  area_circulos = math.pi*args[0]**2
  return area_circulos

def calcular_perimetro_circulos(*args) -> float:
  # args[0] es el primer valor ingresado en la tupla con args 
  # # En este caso es el radio
  perimetro_circulos = 2*math.pi*args[0]
  return perimetro_circulos

def area_total():
  arearectangulo = calcular_area_rectangulo(base,altura)
  areacirculos = calcular_area_circulos(radio)
  areatotal = arearectangulo + areacirculos
  return areatotal

def perimetro_total():
  perimetrorectangulo = calcular_perimetro_rectangulo(base,altura)
  perimetrocirculos = calcular_perimetro_circulos(radio)
  perimetrototal = perimetrorectangulo + perimetrocirculos
  return perimetrototal

if __name__ == "__main__":
  #rectangulo
  base = float(input("Ingrese la base del rectangulo:"))
  altura = float(input("Ingrese la altura del rectangulo:"))
  # Se define con cuales variables se usaran las funciones
  arearectangulo = calcular_area_rectangulo(base,altura)
  perimetrorectangulo = calcular_perimetro_rectangulo(base,altura)
  #circulos
  radio = float(input("Ingrese un radio para los circulos:"))
  # Se define con cuales variables se usaran las funciones
  areacirculos = calcular_area_circulos(radio)
  perimetrocirculos = calcular_perimetro_circulos(radio)
 
  #total
  areatotal =  area_total()
  perimetrototal = perimetro_total()
  
  print("El area del rectangulo es " + str(arearectangulo))
  print("El perimetro del rectangulo es " + str(perimetrorectangulo))
  print("El area de los circulos " + str(areacirculos))
  print("El perimetro de los circulos es " + str(perimetrocirculos))
  print("El area total de la figura es " + str(areatotal))
  print("El perimetro total de la figura es " + str(perimetrototal))
```
</p></details></br>

 ##### Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.
 
<details><summary>codigo</summary><p>

``` python
# Función para calcular el factorial de un número
def calcularfactorial(*args):
    # Inicializar la variable factorial en 1
    factorial = 1
    # Bucle para multiplicar los números del 1 al valor indicado y calcular el factorial
    for i in range(1,(args[0]+1)): # Se escribe args[0] para poder operarlo, ya que se coge el primer primer valor ingresado de la tupla, el cual es "n" 
        factorial = i * factorial
        print(i, "! =", factorial)
    # Devolver el factorial del número dado
    return factorial

# Pedir al usuario un número y calcular los factoriales de los números del 1 al n
if __name__ == "__main__":
    # Pedir al usuario que ingrese un número natural
    n = int(input("Ingrese un número natural: "))
    # Llamar a la función para calcular los factoriales y guardar el resultado en la variable "fact"
    fact = calcularfactorial(n) # Se define que la funcion usara el valor n ingresado
```
</p></details></br>

 ##### El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

<details><summary>codigo</summary><p>

``` python
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
    print("La cantidad de contagiados en Nuncala
```
</p></details></br>

### 3. Escriba una función recursiva para calcular la operación de la potencia.

<details><summary>codigo</summary><p>

``` python
def potenciarecursiva(n : int,p : int)-> int:
  """
  Calcula la potencia de un número utilizando recursión.

  Args:
  n (int): La base de la potencia.
  p (int): El exponente de la potencia.

  Returns:
  int: El resultado de elevar la base a la potencia indicada.
  """
  if p == 0: 
    return 1
  elif p == 1:
    return n
  else:
    return n*potenciarecursiva(n,p-1) 

if __name__ == "__main__":
  # Los valorres que se piden son enteros
  base = int(input("Ingrese la base: ")) 
  exponente = int(input("Ingrese el exponente: "))
  potencia = potenciarecursiva(base,exponente) # Se llama a la funcion
  print(str(base) + " elevado a " + str(exponente) + " es "+ str(potencia)) # Se imprime el resultado
```
</p></details></br>


### 4. Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
<details><summary>codigo</summary><p>

``` python
import time

def fiboiterativo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo

def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2)  
  
if __name__ == "__main__":
  # Fibo iterativo
  numeroiterativo = int(input("Ingrese numero: "))
  start_time1 = time.time()
  serieFibo = fiboiterativo(numeroiterativo)
  end_time1 = time.time()
  timer1 = end_time1 - start_time1
  print("La serie de Fibonacci hasta " + str(numeroiterativo) + " es " + str(serieFibo)+ " (Se calculo de forma iterativa)")
  print("Fibonacci calculado de forma iterativa tardo: " + str(timer1))

if __name__ == "__main__":
  # Fibo recursivo
  numerorecursivo = int(input("Ingrese numero: "))
  start_time2 = time.time()
  serieFibo = fiboRecursivo(numerorecursivo)
  end_time2 = time.time()
  timer2 = end_time2 - start_time2
  print("La serie de Fibonacci hasta " + str(numerorecursivo) + " es " + str(serieFibo)+ " (Se calculo de forma recurisva)")
  print("Fibonacci calculado de forma recursiva tardo: " + str(timer2))
  # Comparación de tiempos
  
  tiempo = timer2 - timer1  # segundos
  if tiempo <= 0.1:
    print("La versión recursiva tardó demasiado, considere usar la versión iterativa") 
```
</p></details></br>

+ Luego de comparar los tiempos se evidencio que la iterativa era mucho mas eficiente que la recursiva, ya que mientras que en la iterativa podia calcular facilmente entradas mayores a 1000, en la recursiva se nota como se tarda significativamente algo mas que la iterativa desde la entrada 16.
+ En este codigo se muestran los tiempos que se tarda cada funcion en dar el resultado requerido, ademas muestra que si la diferencia de tiempo entre la iterativa y recursiva es menor a 0.1, recomienda calcular fibonacci por medio de la funcion iterativa (ya que la recursiva siempre es la que mas tarda) 

### 5. Crear cuenta en stackoverflow y adjuntar imagen en el repo
[![Captura-de-pantalla-2023-05-11-203225.png](https://i.postimg.cc/9XYzqbzZ/Captura-de-pantalla-2023-05-11-203225.png)](https://postimg.cc/6TTBkdrp)

### 6. Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalon. Dejar enlace en el repo.

enlace: https://www.linkedin.com/in/andr%C3%A9s-felipe-vega-bermeo-b51670276/

## Gracias por leer. 
