# EJERCICIO 1

# 1)A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

altura = int(input("Ingrese su altura en centimetros: "))

if altura < 160:
    posicion = "Base"
elif altura <= 179:
    posicion = "Escolta"
elif altura >= 180 and altura <= 199:
    posicion = "Alero"
else:
    posicion = "Ala Pivot o Pivot"

print(f"El jugador con {altura} cm juega de: {posicion}")

# ============================================================

# EJERCICIO 2

#2)Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota
#  es ...

# ============================================================

nota = int(input("Ingrese una nota aleatoria entre 1 y 10: "))

if nota >= 6:
    print(f"Promocion directa, la nota es {nota}")
elif nota == 4 or nota == 5:
    print(f"Aprobado, la nota es {nota}")
elif nota >= 1 and nota <=3:
    print(f"Desaprobrado, la nota es {nota}")