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