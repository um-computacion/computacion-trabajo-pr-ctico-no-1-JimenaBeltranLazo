#FASE 2: Implementación de la Solución (Verde)

def decimal_to_roman(decimal):
    roman_values = [
        #Orden de mayor a menor
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    resultado = ""

    for value, symbol in roman_values:
        while decimal >= value:
            resultado = resultado + symbol
            decimal = decimal - value
    return resultado

#Interacción Usuario
my_decimal = int(input("Bienvenido al Convertor Romano. Por favor ingrese un número del 1 al 3999: "))
my_roman = decimal_to_roman(my_decimal)
if 0 < my_decimal < 4000:
    print(f"El número {my_decimal} en romano es: {my_roman}")
else:
    print("El número que ingresaste está fuera del rango.")