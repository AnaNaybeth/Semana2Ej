lista=input("Ingrese una lista de numeros separados por espacio:")
list=[int(x) for x in lista.split()]
mayor=max(list)
minimo=min(list)
print("El numero mayor es:",mayor," El numero menor es:",minimo)