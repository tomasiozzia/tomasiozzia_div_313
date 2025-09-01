# 1)Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
#  En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
#  Si es invierno: solo se viaja a Bariloche.
#  Si es verano: se viaja a Mar del plata y Cataratas.
#  Si es otoño: se viaja a todos los lugares.
#  Si es primavera: se viaja a todos los lugares menos Bariloche.

destino = input("Ingrese su destino: ")
estacion = input("Ingrese la estacion del año: ")

match estacion:
    case "invierno":
        match destino:
            case "bariloche":
                print("Se viaja")
            case _:
                print("No se viaja")

    case "verano":
        match destino:
            case "mar del plata" | "cataratas":
                print("Se viaja")
            case _:
                print("No se viaja")

    case "otoño":
        print("Se viaja")

    case "primavera":
        match destino:
            case "bariloche":
                print("No se viaja")
            case _:
                print("Se viaja")