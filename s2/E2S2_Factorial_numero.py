fac=1
i=1
num=int(input("Ingresa un numero entre 1 y 20:"))
if num<1 or num>20:
    print("El numero debe estar entre 1 y 20")
else:
    while i <=num:
       fac*=i
       i+=1
    print(fac)

