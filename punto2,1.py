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