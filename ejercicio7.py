valor = str(input("Introduzca la contraseña: "))
contr = 'contraseña'

while True:
    if valor == contr:
        print("Accediendo al sistema...")
        break
    else:
        print("Contraseña incorrecta")
        valor = str(input("Introduzca la contraseña: "))