
num=(int(input("Ingresa un numero:")))

if num<=1:
    print("No es un numero primo")
elif num==2 or num==3:
    print("Es un numero primo")
elif num%2==0 or num%3==0:
    print("No es un numero primo")
else:
    primo=True
    i=5
    while i*i<=num:
        if num%i==0 or num%(i + 2)==0:
            primo=False
            break
        i+=6
    
    if primo:
        print("Es un numero primo")
    else:
        print("No es un numero primo")
