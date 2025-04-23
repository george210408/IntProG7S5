rango_inicial = int(input("escribe el inicio del rango: "))
rango_final = int(input("escriba el fin del rango: "))

if(rango_inicial < rango_final):
    numero = int(input("dime un numero: "))
    if(numero >= rango_inicial and numero <= rango_final):
        print("el numero esta dentro del rango")
    else:
        print("el numero esta fuera del rango")
else:
    print("el rango inicial debe ser menor que el rango final")