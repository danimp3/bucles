fras = input("Introduzca la frase: ")
letr = input("Introduzca la letra a buscar: ")
numle=0

for con in fras:
    
    if con == letr:
        numle = numle+1
        
        
        
print("en la frase hay",numle, "letras", letr)
        