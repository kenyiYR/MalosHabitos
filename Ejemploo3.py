# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):

    return base * altura

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):

    return 0.5 * base * altura



# Función principal
def main():
    # Solicitar al usuario que ingrese la base y la altura del rectángulo
    while True:
        base_rect = input("Ingrese la longitud de la base del rectángulo (entero): ")
        if base_rect.isdigit():
            base_rect = int(base_rect)
            break
        else:
            print("Error: Debe ingresar un número entero.")

    while True:
        altura_rect = input("Ingrese la altura del rectángulo (entero): ")
        if altura_rect.isdigit():
            altura_rect = int(altura_rect)
            break
        else:
            print("Error: Debe ingresar un número entero.")






    # Calcular el área del rectángulo
    area_rectangulo = calcular_area_rectangulo(base_rect, altura_rect)
    print("Área del rectángulo:", area_rectangulo)




    # Solicitar al usuario que ingrese la base y la altura del triángulo
    while True:
        base_triangulo = input("Ingrese la base del triángulo (entero): ")
        if base_triangulo.isdigit():
            base_triangulo = int(base_triangulo)
            break
        else:
            print("Error: Debe ingresar un número entero.")

    while True:
        altura_triangulo = input("Ingrese la altura del triángulo (entero): ")
        if altura_triangulo.isdigit():
            altura_triangulo = int(altura_triangulo)
            break
        else:
            print("Error: Debe ingresar un número entero.")



    # Calcular el área del triángulo
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print("Área del triángulo:", area_triangulo)

# Llamar a la función principal para ejecutar el código
main()
