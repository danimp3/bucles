num = int(input("Dime un numero positivo"))
i = 1
l = []
while i <= num:
    impar = i % 2
    if impar != 0:
        l.append(i)    
    i= i+1
    
print(l)