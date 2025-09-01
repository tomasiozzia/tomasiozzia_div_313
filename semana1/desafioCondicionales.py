# DESAFIO CONDICIONALES

# Facturación del Servicio de Agua Potable

# El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.

# Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.

# A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.

# Tarifa base:

# Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
# El costo por metro cúbico (m³) de agua es de $200/m³.

# Bonificaciones y Recargos según tipo de cliente:

# Cliente Residencial:
# Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
# Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.

# Cliente Comercial:
# Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
# Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
# Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

# Cliente Industrial:
# Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
# consumo.
# Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
# Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

# Casos especiales:
# Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
# En todos los casos, se aplica el IVA del 21% sobre el total.

# Requerimientos del programa:

# 1) Solicitar al usuario:
    # Cantidad de metros consumidos
    # Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.

# 2) Calcular:
    # Subtotal de consumo.
    # Bonificaciones, si corresponde
    # Recargos, si corresponde
    # Subtotal, con recargos y bonificaciones.
    # IVA aplicado (21%), si corresponde.
    # Total final a pagar.

# 3) Mostrar en pantalla el desglose de los cálculos.

metros_consumidos = int(input("Ingrese los metros consumidos: "))
cliente = input("Ingrese su tipo de cliente (Residencial, Comercial o Industrial): ").lower()

cargo_fijo = 7000
metro_cubico = 200 * metros_consumidos 

bonificacion = 0
recargos = 0
iva = 0.21

# Bonificaciones y Recargos según tipo de cliente:

match cliente:
    case "residencial":
        if metros_consumidos > 80:
            recargos = 0.15
        elif metros_consumidos < 30:
            bonificacion = 0.10

    case "comercial":
        if metros_consumidos > 300:
            bonificacion = 0.12
        elif metros_consumidos > 150:
            bonificacion = 0.08
        elif metros_consumidos < 50:
            recargos = 0.05

    case "industrial":
        if metros_consumidos > 1000:
            bonificacion = 0.30
        elif metros_consumidos > 500:
            bonificacion = 0.20
        elif metros_consumidos < 200:
            recargos = 0.10


if cliente == "residencial" and (cargo_fijo + metro_cubico) < 35000:
    bonificacion += 0.05

# VARIABLES NUEVAS

# subtotal de consumo es METRO CUBICO
bonificacion_total = metro_cubico * bonificacion
recargo_total = metro_cubico * recargos
subtotal_entero = metro_cubico - bonificacion_total + recargo_total + cargo_fijo
iva_aplicado = subtotal_entero * iva
total_final = subtotal_entero + iva_aplicado

print(f"Su subtotal es {metro_cubico}")
print(f"Su bonificacion es: ${bonificacion_total} ")
print(f"Su rescargo es: ${recargo_total}")
print(f"Su subtotal con bonificaciones y recargos es: ${subtotal_entero}")
print(f"Su IVA aplicado es: ${iva_aplicado}")
print(f"El total a pagar es: ${total_final}")