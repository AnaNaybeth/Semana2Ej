lista=input("ingresa una lista de numeros separados:")
lista2=[int(x) for x in lista.split()]
lista2.sort(reverse=False)
print(lista2)