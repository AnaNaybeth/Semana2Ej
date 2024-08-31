
let=input("Ingresa una cadena de texto:")
vocales="aeiouAEIOU"
sum=0
for car in let:
    if car in vocales:
        sum+=1
print(sum) 
