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