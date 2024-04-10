# Función para solicitar al usuario un valor entero
def solicitar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debe ingresar un valor entero.")

# Solicitar al usuario que ingrese los valores de x e y
x = solicitar_entero("Ingrese el valor de x (entero): ")
y = solicitar_entero("Ingrese el valor de y (entero): ")

# Calcular el valor de z sumando x e y
z = x + y

# Mostrar el valor de z
print("El valor de z es:", z)

# Definir una función para calcular el producto de dos números
def calcular_producto(num1, num2):
    producto = num1 * num2
    return producto

# Llamar a la función y asignar el resultado a la variable resultado
resultado = calcular_producto(x, z)

# Imprimir el resultado
print("El resultado es:", resultado)
