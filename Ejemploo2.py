
def calcular_producto_sumar(a, b, c):

    try:
        resultado = a * b + c
        return resultado
    except TypeError:
        print("Error: Al menos uno de los argumentos no es un número válido.")
        return None  # Retornar None en caso de error

def principal():
    # Solicitar al usuario que ingrese los valores de x, y, y z
    try:
        x = float(input("Ingrese el valor de x: "))
        y = float(input("Ingrese el valor de y: "))
        z = float(input("Ingrese el valor de z: "))
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")
        return  # Salir de la función si se ingresa un valor no numérico

    # Calcular el resultado usando la función calcular_producto_sumar
    resultado = calcular_producto_sumar(x, y, z)

    # Si el resultado no es None, imprimirlo
    if resultado is not None:
        print("El resultado es:", resultado)

# Llamar a la función principal para ejecutar el código
principal()
