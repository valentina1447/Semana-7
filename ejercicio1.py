x=(int(input("Ingresa el numero de personas")))

for i in range(x):

    nombres = input("Ingrese sus nombres: ")
    apellidos = input("Ingrese sus apellidos: ")
    estatura = float(input("Ingrese su estatura en metros: "))
    peso = float(input("Ingrese su peso en kilogramos: "))


    id_masa = peso / (estatura ** 2)

    print ("tu indice de masa corporal es: ", id_masa)

    if id_masa < 18.5:
        print("Tu IMC es bajo/naranja")
    elif 18.5 <= id_masa <= 24.9:
        print("Tu IMC es saludable/verde")
    elif 25.0 <= id_masa <= 29.9:
        print("Tu IMC es sobrepeso/rojo ")
    else:
        print("Tu IMC es obeso")

