cant= int(input("Dime la cantidad a invertir: "))
interes = int(input("Dime el interes anual: "))
años = int(input("Dime los años a los que quieres aplazar: "))
i = 1

while i <= años:
    cap = cant * (interes / 100)
    print(años,cap)
    cant = cant+cap
    i= i+1