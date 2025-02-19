# Suma
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")

# División
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for division: "))
if num4 == 0:
    print("Error: Division by zero is not allowed.")
else:
    div_result = num3 / num4
    print(f"Division: {num3} / {num4} = {div_result}")


"""
input() obtiene valores ingresados por el usuario.
float() convierte la entrada en número decimal.
f"Texto {variable}" es una f-string para formatear cadenas.
Se verifica si el divisor es 0 para evitar errores matemáticos.


"""

# Pedir al usuario la base y la altura
base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calcular el área del triángulo
area = 0.5 * base * height

# Mostrar el resultado
print(f"The area of the triangle is: {area}")

"""

input() solicita los valores de base y altura al usuario.
float() convierte la entrada en un número decimal.
area = 0.5 * base * height usa la fórmula matemática del área de un triángulo:


"""

# Entrada de datos
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")

# Mostrar valores originales
print(f"Original values: a = {a}, b = {b}")

# Intercambiar valores usando una variable temporal
temp = a
a = b
b = temp

# Mostrar valores intercambiados
print(f"Swapped values: a = {a}, b = {b}")


import random

# Generar un número aleatorio entre 1 y 100
print(f"Random number: {random.randint(1, 100)}")

# Pedir al usuario la distancia en kilómetros
kilometers = float(input("Enter distance in kilometers: "))

# Factor de conversión
conversion_factor = 0.621371

# Convertir a millas
miles = kilometers * conversion_factor

# Mostrar resultado
print(f"{kilometers} kilometers is equal to {miles} miles")


# Pedir al usuario la temperatura en Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Fórmula de conversión
fahrenheit = (celsius * 9/5) + 32

# Mostrar resultado
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")



import calendar

# Solicitar año y mes al usuario
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Mostrar el calendario del mes y año especificados
cal = calendar.month(year, month)
print(cal)


import math

# Solicitar los coeficientes de la ecuación cuadrática
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calcular el discriminante
discriminant = b**2 - 4*a*c

# Verificar el valor del discriminante
if discriminant > 0:
    # Dos raíces reales y distintas
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant == 0:
    # Una raíz real (repetida)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    # Raíces complejas
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")

"""

Entrada de datos: Se solicitan los coeficientes a, b y c de la ecuación cuadrática.

Discriminante: Se calcula el discriminante usando la fórmula discriminant = b**2 - 4*a*c.

Condiciones:

Si el discriminante es positivo, hay dos raíces reales distintas.

Si el discriminante es cero, hay una raíz real repetida.

Si el discriminante es negativo, las raíces son complejas.

Salida: Se imprimen las raíces según el caso.

"""


# Inicializar dos variables
a = 5
b = 10

# Intercambiar valores sin usar una variable temporal
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

"""
Inicialización: Se inicializan dos variables a y b con valores 5 y 10 respectivamente.

Intercambio: Se intercambian los valores de a y b usando la asignación múltiple en Python: a, b = b, a.

Salida: Se imprimen los valores de a y b después del intercambio.


"""

# Solicitar un número al usuario
num = float(input("Enter a number: "))

# Verificar si el número es positivo, negativo o cero
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# Solicitar un número al usuario
num = int(input("Enter a number: "))

# Verificar si el número es par o impar
if num % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")


# Definir el intervalo
lower = 1
upper = 10

print("Prime numbers between", lower, "and", upper, "are:")

# Iterar a través del intervalo y verificar si cada número es primo
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

"""

Intervalo: Se define el intervalo de números desde lower (1) hasta upper (10).

Iteración: Se itera a través de cada número en el intervalo.

Verificación de primalidad: Para cada número mayor que 1, se verifica si es divisible por algún número entre 2 y num-1.

Si no es divisible por ningún número, es primo.

Salida: Se imprimen los números primos en el intervalo.


"""

# Solicitar un número al usuario
num = int(input("Enter a number: "))

factorial = 1

# Verificar si el número es negativo, cero o positivo
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")

"""
Entrada de datos: Se solicita al usuario que ingrese un número.

Condiciones:

Si el número es negativo, no existe factorial.

Si el número es 0, el factorial es 1.

Si el número es positivo, se calcula el factorial multiplicando todos los números desde 1 hasta num.

Salida: Se imprime el factorial del número.
"""

# Solicitar el número de términos al usuario
nterms = int(input("How many terms? "))

# Primeros dos términos de la secuencia de Fibonacci
n1, n2 = 0, 1
count = 0

# Verificar si el número de términos es válido
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # Actualizar valores
        n1 = n2
        n2 = nth
        count += 1


# Solicitar el límite al usuario
limit = int(input("Enter the limit: "))

# Inicializar la suma
sum = 0

# Calcular la suma de los números naturales hasta el límite
for i in range(1, limit + 1):
    sum += i

# Imprimir la suma
print("The sum of natural numbers up to", limit, "is:", sum)

"""
Entrada de datos: Se solicita al usuario que ingrese un límite.

Inicialización: Se inicializa la variable sum en 0.

Iteración: Se itera desde 1 hasta el límite, sumando cada número a sum.

Salida: Se imprime la suma de los números naturales hasta el límite.

"""
# Función para calcular el LCM de dos números
def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

# Solicitar dos números al usuario
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Calcular y mostrar el LCM
print("The L.C.M. is", compute_lcm(num1, num2))


"""
Función compute_lcm: Esta función calcula el LCM de dos números.

Se encuentra el mayor de los dos números.

Se incrementa el mayor número hasta que sea divisible por ambos números.

Entrada de datos: Se solicitan dos números al usuario.

Cálculo del LCM: Se llama a la función compute_lcm para calcular el LCM.

Salida: Se imprime el LCM de los dos números.

"""
# Función para calcular el BMI
def bodymassindex(height, weight):
    return round((weight / height**2), 2)

# Solicitar la altura y el peso al usuario
h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))

# Calcular y mostrar el BMI
print("Welcome to the BMI calculator.")
bmi = bodymassindex(h, w)
print("Your BMI is: ", bmi)

# Interpretar el resultado del BMI
if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")


"""
Función bodymassindex(height, weight): Esta función calcula el BMI usando la fórmula BMI = weight / height^2.

Entrada de datos: Se solicita al usuario que ingrese su altura en metros y su peso en kilogramos.

Cálculo del BMI: Se llama a la función bodymassindex para calcular el BMI.

Interpretación del BMI: Se interpreta el resultado del BMI y se imprime el estado de peso correspondiente.

"""
# Encontrar la suma de los elementos de un arreglo usando la función sum()
arr = [1, 2, 3]
ans = sum(arr)
print('Sum of the array is ', ans)

"""
Arreglo: Se define un arreglo de números.

Función sum(arr): Esta función calcula la suma de los elementos del arreglo.

Salida: Se imprime la suma de los elementos del arreglo.

"""

# Función para encontrar el elemento más grande en un arreglo
def find_largest_element(arr):
    if not arr:
        return "Array is empty"

    # Inicializar el primer elemento como el más grande
    largest_element = arr[0]

    # Iterar a través del arreglo para encontrar el elemento más grande
    for element in arr:
        if element > largest_element:
            largest_element = element

    return largest_element

# Ejemplo de uso
my_array = [10, 20, 30, 99]
result = find_largest_element(my_array)
print(f"The largest element in the array is: {result}")

"""
Función find_largest_element(arr): Esta función encuentra el elemento más grande en un arreglo.

Si el arreglo está vacío, devuelve un mensaje indicando que el arreglo está vacío.

De lo contrario, inicializa el primer elemento como el más grande y luego itera a través del arreglo para encontrar el elemento más grande.

Ejemplo de uso: Se define un arreglo y se llama a la función para encontrar el elemento más grande.

Salida: Se imprime el elemento más grande del arreglo.  


"""














