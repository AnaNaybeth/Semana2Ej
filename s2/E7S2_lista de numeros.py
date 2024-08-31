lista=input("Ingrese una lista de numeros separados por espacio:")
list=[int(x) for x in lista.split()]
suma=sum(list)
print(suma)