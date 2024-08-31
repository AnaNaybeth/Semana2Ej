n = int(input("Ingresa un número entre 1 y 50: "))

if n>1 or n>50:
    print("Debes ingresar un numero entre 1 y 50")
fibo=[0, 1]
for i in range(2, n):
    fibo.append(fibo[-1] + fibo[-2])
print(fibo)
