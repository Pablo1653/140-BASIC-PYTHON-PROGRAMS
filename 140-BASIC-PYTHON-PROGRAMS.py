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
# Lista de números
numbers = [30, 10, -45, 5, 20]

# Inicializar el valor mínimo con el primer elemento de la lista
minimum = numbers[0]

# Iterar a través de la lista para encontrar el número más pequeño
for i in numbers:
    if i < minimum:
        minimum = i

# Imprimir el número más pequeño
print("The smallest number in the list is:", minimum)

"""
Lista de números: Se define una lista de números.

Inicialización del mínimo: Se inicializa una variable minimum con el primer elemento de la lista.

Iteración y comparación: Se itera a través de la lista y se compara cada elemento con minimum. Si se encuentra un número más pequeño, se actualiza minimum.

Salida: Se imprime el número más pequeño de la lista.

"""
# Lista de números
numbers = [30, 10, -45, 5, 20]

# Inicializar el valor máximo con el primer elemento de la lista
maximum = numbers[0]

# Iterar a través de la lista para encontrar el número más grande
for i in numbers:
    if i > maximum:
        maximum = i

# Imprimir el número más grande
print("The largest number in the list is:", maximum)

"""

Lista de números: Se define una lista de números.

Inicialización del máximo: Se inicializa una variable maximum con el primer elemento de la lista.

Iteración y comparación: Se itera a través de la lista y se compara cada elemento con maximum. Si se encuentra un número más grande, se actualiza maximum.

Salida: Se imprime el número más grande de la lista.


"""

# Lista de números
numbers = [30, 10, 45, 5, 20]

# Ordenar la lista en orden descendente
numbers.sort(reverse=True)

# Verificar si hay al menos dos elementos en la lista
if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number.")


"""
Lista de números: Se define una lista de números.

Ordenación: Se ordena la lista en orden descendente.

Verificación: Se verifica si la lista tiene al menos dos elementos.

Salida: Se imprime el segundo número más grande de la lista.

"""
# Función para encontrar los N elementos más grandes de una lista
def find_n_largest_elements(lst, n):
    # Ordenar la lista en orden descendente
    sorted_lst = sorted(lst, reverse=True)

    # Obtener los primeros N elementos
    largest_elements = sorted_lst[:n]

    return largest_elements

# Lista de números
numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]

# Solicitar el valor de N al usuario
N = int(input("N = "))

# Encontrar los N elementos más grandes de la lista
result = find_n_largest_elements(numbers, N)

# Imprimir los N elementos más grandes
print(f"The {N} largest elements in the list are:", result)

"""
Función find_n_largest_elements(lst, n): Esta función encuentra los n elementos más grandes de una lista.

Se ordena la lista en orden descendente.

Se toman los primeros n elementos de la lista ordenada.

Entrada de datos: Se solicita al usuario que ingrese el valor de N.

Cálculo y salida: Se llama a la función para encontrar los N elementos más grandes y se imprimen.

"""

# Lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usar una comprensión de lista para filtrar números pares
even_numbers = [num for num in numbers if num % 2 == 0]

# Imprimir los números pares
print("Even numbers in the list:", even_numbers)

"""
Lista de números: Se define una lista de números.

Comprensión de lista: Se utiliza una comprensión de lista para filtrar los números pares.

Salida: Se imprimen los números pares de la lista.
"""
# Lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usar una comprensión de lista para filtrar números impares
odd_numbers = [num for num in numbers if num % 2 != 0]

# Imprimir los números impares
print("Odd numbers in the list:", odd_numbers)

"""
Lista de números: Se define una lista de números.

Comprensión de lista: Se utiliza una comprensión de lista para filtrar los números impares.

Salida: Se imprimen los números impares de la lista.
"""
# Función para encontrar palabras más largas que una longitud dada
def find_words(words, k):
    result = []
    for word in words:
        if len(word) > k:
            result.append(word)
    return result

# Lista de palabras
word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon fruit"]
k = 5

# Encontrar palabras más largas que k
long_words = find_words(word_list, k)

# Imprimir las palabras más largas
print(f"Words longer than {k} characters: {long_words}")

"""
Función find_words(words, k): Esta función encuentra palabras en una lista que son más largas que una longitud dada k.

Lista de palabras: Se define una lista de palabras.

Entrada de datos: Se define la longitud k.

Cálculo y salida: Se llama a la función para encontrar las palabras más largas que k y se imprimen.
"""
# Dividir una cadena en una lista de palabras
input_str = "Python program to split and join a string"
word_list = input_str.split()  # Divide por espacios automáticamente

# Unir la lista de palabras en una sola cadena
separator = " "  # Separador entre palabras
output_str = separator.join(word_list)

# Mostrar resultados
print("Cadena original:", input_str)
print("Lista de palabras:", word_list)
print("Cadena unida:", output_str)

"""
Funcionalidad
Este programa divide una cadena en palabras y luego las vuelve a unir en una sola cadena.

Entrada de datos:
Se proporciona una cadena de texto.
Cálculo y salida:
Se divide la cadena en una lista de palabras usando split().
Se vuelve a unir la lista en una cadena usando join().
Se imprimen los resultados.
"""

def is_binary_string(s):
    return all(char in '01' for char in s)

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Verificar si es binaria
if is_binary_string(input_str):
    print(f"{input_str} es una cadena binaria.")
else:
    print(f"{input_str} NO es una cadena binaria.")


"""
Funcionalidad
Este programa verifica si una cadena contiene solo 0 y 1, lo que indica que es una cadena binaria.

Entrada de datos:
Se proporciona una cadena de texto.
Cálculo y salida:
Se verifica que cada carácter sea 0 o 1.
Se imprime si la cadena es binaria o no.
"""
def find_uncommon_words(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    return list(set1.symmetric_difference(set2))  # Palabras no comunes

# Entrada del usuario
string1 = input("Ingrese la primera cadena: ")
string2 = input("Ingrese la segunda cadena: ")

# Encontrar palabras poco comunes
uncommon_words = find_uncommon_words(string1, string2)

# Mostrar resultados
print("Palabras poco comunes:", uncommon_words)

"""
Funcionalidad
Este programa encuentra las palabras que aparecen en una cadena pero no en la otra.

Entrada de datos:
Se ingresan dos cadenas de texto.
Cálculo y salida:
Se convierten ambas cadenas en conjuntos de palabras.
Se encuentra la diferencia simétrica entre ambos conjuntos.
Se imprimen las palabras poco comunes.
"""
def is_substring(main_str, sub_str):
    return sub_str in main_str

# Entrada del usuario
main_string = input("Ingrese la cadena principal: ")
sub_string = input("Ingrese la subcadena a buscar: ")

# Verificar si es subcadena
if is_substring(main_string, sub_string):
    print(f'"{sub_string}" es una subcadena de "{main_string}".')
else:
    print(f'"{sub_string}" NO es una subcadena de "{main_string}".')

"""
Funcionalidad
Este programa verifica si una palabra es una subcadena de otra.

Entrada de datos:
Se ingresan dos cadenas de texto.
Cálculo y salida:
Se usa el operador in para verificar si la segunda cadena está dentro de la primera.
Se imprime si la segunda cadena es una subcadena o no.
"""
from collections import Counter

def find_duplicates(s):
    char_count = Counter(s)  # Cuenta la frecuencia de cada carácter
    duplicates = [char for char, count in char_count.items() if count > 1]
    return duplicates

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Encontrar caracteres duplicados
duplicates = find_duplicates(input_str)

# Mostrar resultados
print("Caracteres duplicados:", duplicates if duplicates else "No hay caracteres duplicados.")

"""
Funcionalidad
Este programa encuentra y muestra los caracteres que aparecen más de una vez en una cadena.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa un diccionario para contar las ocurrencias de cada carácter.
Se imprimen los caracteres que aparecen más de una vez.
"""
from itertools import permutations

def get_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Generar permutaciones
perm_list = get_permutations(input_str)

# Mostrar resultados
print("Permutaciones:", perm_list)

"""
Funcionalidad
Este programa genera todas las permutaciones posibles de una cadena dada.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa itertools.permutations() para generar las permutaciones.
Se imprimen todas las permutaciones posibles.
"""
def count_words(s):
    return len(s.split())

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Contar palabras
word_count = count_words(input_str)

# Mostrar resultados
print(f"Número de palabras: {word_count}")

"""
Funcionalidad
Este programa cuenta cuántas palabras hay en una cadena de texto.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa split() para dividir la cadena en palabras.
Se cuenta el número de palabras en la lista resultante.
"""

from collections import Counter

def word_frequency(s):
    words = s.split()
    return Counter(words)  # Cuenta la frecuencia de cada palabra

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Calcular la frecuencia de palabras
freq = word_frequency(input_str)

# Mostrar resultados
print("Frecuencia de palabras:", dict(freq))

"""
Funcionalidad
Este programa cuenta cuántas veces aparece cada palabra en una cadena de texto.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa split() para dividir la cadena en palabras.
Se usa Counter() para contar la frecuencia de cada palabra.
Se imprimen las palabras junto con su frecuencia.
"""
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)  # Comparar las letras ordenadas

# Entrada del usuario
word1 = input("Ingrese la primera palabra: ")
word2 = input("Ingrese la segunda palabra: ")

# Verificar si son anagramas
if are_anagrams(word1, word2):
    print(f'"{word1}" y "{word2}" son anagramas.')
else:
    print(f'"{word1}" y "{word2}" NO son anagramas.')

""""
Funcionalidad
Este programa verifica si dos palabras son anagramas, es decir, si tienen las mismas letras en diferente orden.

Entrada de datos:
Se ingresan dos cadenas de texto.
Cálculo y salida:
Se ordenan las letras de ambas cadenas y se comparan.
Se imprime si las cadenas son anagramas o no.
"""""
def replace_character(s, old_char, new_char):
    return s.replace(old_char, new_char)  # Reemplazar el carácter

# Entrada del usuario
input_str = input("Ingrese una cadena: ")
old_char = input("Ingrese el carácter a reemplazar: ")
new_char = input("Ingrese el nuevo carácter: ")

# Reemplazar caracteres
new_str = replace_character(input_str, old_char, new_char)

# Mostrar resultados
print("Cadena modificada:", new_str)

""""
Funcionalidad
Este programa reemplaza todas las apariciones de un carácter en una cadena con otro carácter.

Entrada de datos:
Se ingresa una cadena de texto.
Se ingresa el carácter a reemplazar y el carácter nuevo.
Cálculo y salida:
Se usa replace() para reemplazar todas las apariciones del carácter.
Se imprime la nueva cadena.
"""""

def reverse_string(s):
    return s[::-1]  # Invertir la cadena

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Invertir la cadena
reversed_str = reverse_string(input_str)

# Mostrar resultados
print("Cadena invertida:", reversed_str)

""""
Funcionalidad
Este programa invierte una cadena de texto.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa [::-1] para invertir la cadena.
Se imprime la cadena invertida.
"""""
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
    return s == s[::-1]  # Comparar con su versión invertida

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Verificar si es un palíndromo
if is_palindrome(input_str):
    print(f'"{input_str}" es un palíndromo.')
else:
    print(f'"{input_str}" NO es un palíndromo.')


""""
Funcionalidad
Este programa verifica si una cadena es un palíndromo, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se convierte la cadena a minúsculas y se eliminan los espacios.
Se compara la cadena original con su versión invertida.
Se imprime si es un palíndromo o no.

"""""
from collections import Counter

def most_frequent_char(s):
    freq = Counter(s)  # Contar ocurrencias de cada carácter
    return max(freq, key=freq.get)  # Obtener el carácter más frecuente

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Encontrar el carácter más frecuente
most_frequent = most_frequent_char(input_str)

# Mostrar resultados
print(f'El carácter más frecuente en "{input_str}" es "{most_frequent}".')

""""
Funcionalidad
Este programa encuentra el carácter que más veces aparece en una cadena.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa Counter() para contar las ocurrencias de cada carácter.
Se obtiene el carácter con mayor frecuencia.
Se imprime el carácter más frecuente junto con su conteo.
"""""

def capitalize_words(s):
    return s.title()  # Convertir la primera letra de cada palabra a mayúscula

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Capitalizar palabras
capitalized_str = capitalize_words(input_str)

# Mostrar resultados
print("Cadena capitalizada:", capitalized_str)

""""
Funcionalidad
Este programa convierte la primera letra de cada palabra de una cadena en mayúscula.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa title() para capitalizar cada palabra.
Se imprime la cadena modificada.
"""""

def word_in_sentence(sentence, word):
    return word in sentence

# Entrada del usuario
sentence = input("Ingrese una oración: ")
word = input("Ingrese la palabra a buscar: ")

# Verificar si la palabra está en la oración
if word_in_sentence(sentence, word):
    print(f'La palabra "{word}" está en la oración.')
else:
    print(f'La palabra "{word}" NO está en la oración.')

""""
Funcionalidad
Este programa verifica si una palabra está presente en una oración.

Entrada de datos:
Se ingresa una oración y una palabra.
Cálculo y salida:
Se usa el operador in para verificar si la palabra está en la oración.
Se imprime si la palabra está presente o no.
"""""
def concatenate_strings(str1, str2):
    return "".join([str1, str2])  # Concatenar sin usar "+"

# Entrada del usuario
string1 = input("Ingrese la primera cadena: ")
string2 = input("Ingrese la segunda cadena: ")

# Concatenar cadenas
concatenated_str = concatenate_strings(string1, string2)

# Mostrar resultados
print("Cadena concatenada:", concatenated_str)

""""
Funcionalidad
Este programa concatena dos cadenas sin usar el operador +.

Entrada de datos:
Se ingresan dos cadenas de texto.
Cálculo y salida:
Se usa join() para unir ambas cadenas.
Se imprime la cadena concatenada.
"""""
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)  # Contar vocales

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Contar vocales
vowel_count = count_vowels(input_str)

# Mostrar resultados
print(f"Número de vocales en la cadena: {vowel_count}")

""""
Funcionalidad
Este programa cuenta cuántas vocales hay en una cadena.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se recorre la cadena y se cuentan las vocales (a, e, i, o, u).
Se imprime el número de vocales
"""""

def convert_case(s):
    return s.lower(), s.upper()  # Convertir a minúsculas y mayúsculas

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Convertir a mayúsculas y minúsculas
lower_str, upper_str = convert_case(input_str)

# Mostrar resultados
print("Minúsculas:", lower_str)
print("Mayúsculas:", upper_str)

""""
Funcionalidad
Este programa convierte una cadena a mayúsculas y minúsculas.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa lower() para convertir la cadena a minúsculas.
Se usa upper() para convertir la cadena a mayúsculas.
Se imprimen ambas versiones.
"""""
def swap_case(s):
    return s.swapcase()  # Intercambiar mayúsculas y minúsculas

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Intercambiar mayúsculas y minúsculas
swapped_str = swap_case(input_str)

# Mostrar resultados
print("Cadena modificada:", swapped_str)

""""
Funcionalidad
Este programa invierte las mayúsculas y minúsculas en una cadena.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa swapcase() para intercambiar mayúsculas y minúsculas.
Se imprime la cadena modificada.
"""""

def count_consonants(s):
    vowels = "aeiouAEIOU"
    consonants = [char for char in s if char.isalpha() and char not in vowels]
    return len(consonants)

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Contar consonantes
consonant_count = count_consonants(input_str)

# Mostrar resultados
print(f"Número de consonantes en la cadena: {consonant_count}")

""""
Funcionalidad
Este programa cuenta cuántas consonantes hay en una cadena.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se eliminan espacios y se convierten caracteres a minúsculas.
Se filtran las letras que no son vocales.
Se imprime la cantidad de consonantes.
"""""
def is_alpha_string(s):
    return s.isalpha()  # Verifica si la cadena solo tiene letras

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Comprobar si solo contiene letras
if is_alpha_string(input_str):
    print(f'"{input_str}" contiene solo letras.')
else:
    print(f'"{input_str}" contiene caracteres no alfabéticos.')

""""
Funcionalidad
Este programa verifica si una cadena contiene solo caracteres alfabéticos.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa isalpha() para verificar si la cadena contiene solo letras.
Se imprime si la cadena es válida o no.
"""""
def is_digit_string(s):
    return s.isdigit()  # Verifica si la cadena solo tiene números

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Comprobar si solo contiene números
if is_digit_string(input_str):
    print(f'"{input_str}" contiene solo números.')
else:
    print(f'"{input_str}" contiene caracteres no numéricos.')


""""
Funcionalidad
Este programa verifica si una cadena contiene solo números.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa isdigit() para verificar si la cadena contiene solo dígitos.
Se imprime si la cadena es válida o no.
"""""

def is_alnum_string(s):
    return s.isalnum()  # Verifica si la cadena solo tiene letras y números

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Comprobar si solo contiene letras y números
if is_alnum_string(input_str):
    print(f'"{input_str}" contiene solo caracteres alfanuméricos.')
else:
    print(f'"{input_str}" contiene caracteres especiales.')

""""
Funcionalidad
Este programa verifica si una cadena contiene solo letras y números.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa isalnum() para verificar si la cadena contiene solo caracteres alfanuméricos.
Se imprime si la cadena es válida o no.
"""""

def remove_spaces(s):
    return s.replace(" ", "")  # Eliminar todos los espacios en blanco

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Eliminar espacios
no_space_str = remove_spaces(input_str)

# Mostrar resultados
print("Cadena sin espacios:", no_space_str)

""""
Funcionalidad
Este programa elimina todos los espacios en blanco de una cadena.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa replace(" ", "") para eliminar los espacios.
Se imprime la cadena sin espacios.
"""""

def string_to_list(s):
    return s.split()  # Convertir la cadena en una lista de palabras

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Convertir cadena en lista de palabras
word_list = string_to_list(input_str)

# Mostrar resultados
print("Lista de palabras:", word_list)

""""
Funcionalidad
Este programa convierte una cadena en una lista de palabras separadas por espacios.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa split() para dividir la cadena en palabras.
Se imprime la lista de palabras.
"""""
def ends_with(s, suffix):
    return s.endswith(suffix)  # Verifica si la cadena termina con el sufijo

# Entrada del usuario
input_str = input("Ingrese una cadena: ")
suffix = input("Ingrese el sufijo: ")

# Comprobar si la cadena termina con el sufijo
if ends_with(input_str, suffix):
    print(f'La cadena "{input_str}" termina con "{suffix}".')
else:
    print(f'La cadena "{input_str}" NO termina con "{suffix}".')

""""
Funcionalidad
Este programa verifica si una cadena termina con un sufijo determinado.

Entrada de datos:
Se ingresa una cadena de texto y un sufijo.
Cálculo y salida:
Se usa endswith() para comprobar el sufijo.
Se imprime si la cadena tiene el sufijo o no.
"""""

def starts_with(s, prefix):
    return s.startswith(prefix)  # Verifica si la cadena comienza con el prefijo

# Entrada del usuario
input_str = input("Ingrese una cadena: ")
prefix = input("Ingrese el prefijo: ")

# Comprobar si la cadena comienza con el prefijo
if starts_with(input_str, prefix):
    print(f'La cadena "{input_str}" comienza con "{prefix}".')
else:
    print(f'La cadena "{input_str}" NO comienza con "{prefix}".')

""""
Funcionalidad
Este programa verifica si una cadena comienza con un prefijo determinado.

Entrada de datos:
Se ingresa una cadena de texto y un prefijo.
Cálculo y salida:
Se usa startswith() para comprobar el prefijo.
Se imprime si la cadena tiene el prefijo o no.

"""""

def find_word(s, word):
    return s.find(word)  # Encontrar el índice de la primera aparición

# Entrada del usuario
input_str = input("Ingrese una cadena: ")
word = input("Ingrese la palabra a buscar: ")

# Buscar la palabra
index = find_word(input_str, word)

# Mostrar resultados
if index != -1:
    print(f'La palabra "{word}" aparece por primera vez en el índice {index}.')
else:
    print(f'La palabra "{word}" no se encontró en la cadena.')

""""
Funcionalidad
Este programa encuentra la primera aparición de una palabra dentro de una cadena y devuelve su índice.

Entrada de datos:
Se ingresa una cadena y una palabra a buscar.
Cálculo y salida:
Se usa find() para encontrar la posición de la palabra.
Se imprime la posición si la palabra está presente, o un mensaje si no lo está.

"""""
def count_word_occurrences(s, word):
    return s.count(word)  # Contar ocurrencias de la palabra

# Entrada del usuario
input_str = input("Ingrese una cadena: ")
word = input("Ingrese la palabra a contar: ")

# Contar ocurrencias
word_count = count_word_occurrences(input_str, word)

# Mostrar resultados
print(f'La palabra "{word}" aparece {word_count} veces en la cadena.')

""""
Funcionalidad
Este programa cuenta cuántas veces aparece una palabra en una cadena de texto.

Entrada de datos:
Se ingresa una cadena de texto y una palabra a contar.
Cálculo y salida:
Se usa count() para contar la frecuencia de la palabra.
Se imprime la cantidad de veces que aparece.

"""""

def remove_non_alnum(s):
    return ''.join(char for char in s if char.isalnum())  # Filtrar solo letras y números

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Eliminar caracteres no alfanuméricos
clean_str = remove_non_alnum(input_str)

# Mostrar resultados
print("Cadena limpia:", clean_str)

""""
Funcionalidad
Este programa elimina todos los caracteres que no sean letras o números de una cadena.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa isalnum() para filtrar solo los caracteres alfanuméricos.
Se imprime la cadena limpia.
"""""
def longest_word(words):
    longest = max(words, key=len)  # Encontrar la palabra más larga
    return longest, len(longest)

# Entrada del usuario
word_list = input("Ingrese una lista de palabras separadas por espacios: ").split()

# Encontrar la palabra más larga
longest, length = longest_word(word_list)

# Mostrar resultados
print(f'La palabra más larga es "{longest}" con una longitud de {length} caracteres.')

""""
Funcionalidad
Este programa encuentra la palabra más larga en una lista y su longitud.

Entrada de datos:
Se ingresa una lista de palabras.
Cálculo y salida:
Se usa max() con key=len para encontrar la palabra más larga.
Se imprime la palabra más larga y su longitud.
"""""
def reverse_word_order(s):
    return ' '.join(s.split()[::-1])  # Invertir el orden de las palabras

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Invertir el orden de las palabras
reversed_str = reverse_word_order(input_str)

# Mostrar resultados
print("Cadena con palabras en orden invertido:", reversed_str)

""""
Funcionalidad
Este programa invierte el orden de las palabras en una cadena sin alterar el contenido de cada palabra.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa split() para dividir la cadena en palabras.
Se invierte la lista de palabras con [::-1].
Se usa join() para unir las palabras nuevamente.
Se imprime la cadena con el orden de palabras invertido.
"""""

def unique_words(s):
    return set(s.split())  # Obtener palabras únicas

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Encontrar palabras únicas
unique_word_list = unique_words(input_str)

# Mostrar resultados
print("Palabras únicas:", unique_word_list)


""""
Funcionalidad
Este programa extrae todas las palabras únicas de una cadena.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa split() para dividir la cadena en palabras.
Se usa set() para eliminar duplicados.
Se imprime la lista de palabras únicas.
"""""
def remove_extra_spaces(s):
    return ' '.join(s.split())  # Reemplazar múltiples espacios con uno solo

# Entrada del usuario
input_str = input("Ingrese una cadena con múltiples espacios: ")

# Limpiar espacios extra
clean_str = remove_extra_spaces(input_str)

# Mostrar resultados
print("Cadena con espacios corregidos:", clean_str)

""""
Funcionalidad
Este programa reemplaza múltiples espacios consecutivos por un solo espacio.

Entrada de datos:
Se ingresa una cadena de texto con múltiples espacios.
Cálculo y salida:
Se usa split() para dividir la cadena en palabras ignorando espacios adicionales.
Se usa join() para unir las palabras con un solo espacio.
Se imprime la cadena limpia.
"""""
def case_insensitive_compare(str1, str2):
    return str1.lower() == str2.lower()  # Comparar sin distinguir mayúsculas y minúsculas

# Entrada del usuario
string1 = input("Ingrese la primera cadena: ")
string2 = input("Ingrese la segunda cadena: ")

# Comparar cadenas
if case_insensitive_compare(string1, string2):
    print("Las cadenas son iguales (ignorando mayúsculas/minúsculas).")
else:
    print("Las cadenas NO son iguales.")

""""
Funcionalidad
Este programa compara dos cadenas sin considerar diferencias entre mayúsculas y minúsculas.

Entrada de datos:
Se ingresan dos cadenas de texto.
Cálculo y salida:
Se convierten ambas cadenas a minúsculas con lower().
Se comparan las cadenas y se imprime si son iguales o no.
"""""

def shortest_word(words):
    shortest = min(words, key=len)  # Encontrar la palabra más corta
    return shortest, len(shortest)

# Entrada del usuario
word_list = input("Ingrese una lista de palabras separadas por espacios: ").split()

# Encontrar la palabra más corta
shortest, length = shortest_word(word_list)

# Mostrar resultados
print(f'La palabra más corta es "{shortest}" con una longitud de {length} caracteres.')

""""
Funcionalidad
Este programa encuentra la palabra más corta en una lista de palabras.

Entrada de datos:
Se ingresa una lista de palabras.
Cálculo y salida:
Se usa min() con key=len para encontrar la palabra más corta.
Se imprime la palabra y su longitud.
"""""

def count_chars_no_spaces(s):
    return len(s.replace(" ", ""))  # Contar caracteres sin espacios

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Contar caracteres sin espacios
char_count = count_chars_no_spaces(input_str)

# Mostrar resultados
print(f"Número de caracteres (sin contar espacios): {char_count}")

""""
Funcionalidad
Este programa cuenta la cantidad de caracteres en una cadena, excluyendo los espacios.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa replace(" ", "") para eliminar los espacios.
Se usa len() para contar los caracteres restantes.
Se imprime el resultado.
"""""

def is_only_spaces(s):
    return s.isspace()  # Verificar si la cadena tiene solo espacios

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Verificar si la cadena tiene solo espacios
if is_only_spaces(input_str):
    print("La cadena contiene solo espacios en blanco.")
else:
    print("La cadena tiene caracteres diferentes a espacios.")

""""
Funcionalidad
Este programa verifica si una cadena contiene solo espacios en blanco.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa isspace() para verificar si la cadena está compuesta solo de espacios.
Se imprime si la cadena tiene solo espacios o no.
"""""
def words_starting_with(s, letter):
    return [word for word in s.split() if word.startswith(letter)]

# Entrada del usuario
input_str = input("Ingrese una cadena: ")
letter = input("Ingrese una letra: ")

# Buscar palabras
matching_words = words_starting_with(input_str, letter)

# Mostrar resultados
print("Palabras que comienzan con la letra:", matching_words)

""""
Funcionalidad
Este programa extrae todas las palabras de una cadena que comienzan con una letra dada.

Entrada de datos:
Se ingresa una cadena de texto y una letra.
Cálculo y salida:
Se usa split() para obtener la lista de palabras.
Se filtran las palabras que comienzan con la letra dada.
Se imprimen las palabras encontradas.
"""""
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)  # Filtrar vocales

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Eliminar vocales
no_vowel_str = remove_vowels(input_str)

# Mostrar resultados
print("Cadena sin vocales:", no_vowel_str)

""""
Funcionalidad
Este programa elimina todas las vocales de una cadena de texto.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa una comprensión de lista para filtrar los caracteres que no son vocales.
Se imprime la cadena sin vocales.
"""""
def reverse_each_word(s):
    return ' '.join(word[::-1] for word in s.split())  # Invertir cada palabra

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Invertir palabras individualmente
reversed_words_str = reverse_each_word(input_str)

# Mostrar resultados
print("Cadena con palabras invertidas:", reversed_words_str)

""""
Funcionalidad
Este programa invierte cada palabra de una cadena sin cambiar el orden de las palabras.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa split() para dividir la cadena en palabras.
Se invierten las palabras con [::-1].
Se imprimen las palabras invertidas manteniendo su orden original.
"""""
from collections import Counter

def letter_frequency(s):
    return Counter(s)  # Contar frecuencia de cada letra

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Contar letras
letter_count = letter_frequency(input_str)

# Mostrar resultados
print("Frecuencia de letras:", dict(letter_count))

""""
Funcionalidad
Este programa cuenta la cantidad de veces que aparece cada letra en una cadena.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa Counter() para contar la frecuencia de cada carácter.
Se imprime un diccionario con las letras y sus cantidades.
"""""
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Verificar si es un pangrama
if is_pangram(input_str):
    print("La cadena es un pangrama.")
else:
    print("La cadena NO es un pangrama.")

""""
Funcionalidad
Este programa verifica si una cadena contiene todas las letras del alfabeto.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa set() para obtener las letras únicas en la cadena.
Se compara con el conjunto de todas las letras del alfabeto.
Se imprime si la cadena es un pangrama o no.

"""""
def capitalize_sentences(s):
    return '. '.join(sentence.capitalize() for sentence in s.split('. '))  # Capitalizar cada oración

# Entrada del usuario
input_str = input("Ingrese un párrafo: ")

# Capitalizar oraciones
capitalized_text = capitalize_sentences(input_str)

# Mostrar resultados
print("Texto corregido:", capitalized_text)

""""
Funcionalidad
Este programa convierte la primera letra de cada oración en mayúscula.

Entrada de datos:
Se ingresa un párrafo de texto.
Cálculo y salida:
Se usa split(". ") para dividir las oraciones.
Se usa capitalize() para poner en mayúscula la primera letra de cada oración.
Se imprime el texto corregido.

"""""

def words_containing_letter(s, letter):
    return [word for word in s.split() if letter in word]

# Entrada del usuario
input_str = input("Ingrese una cadena: ")
letter = input("Ingrese una letra: ")

# Buscar palabras
matching_words = words_containing_letter(input_str, letter)

# Mostrar resultados
print("Palabras que contienen la letra:", matching_words)
""""
Funcionalidad
Este programa encuentra todas las palabras de una cadena que contienen una letra específica.

Entrada de datos:
Se ingresa una cadena de texto y una letra.
Cálculo y salida:
Se usa split() para dividir la cadena en palabras.
Se filtran las palabras que contienen la letra dada.
Se imprimen las palabras encontradas.

"""""

def sort_words(s):
    return ' '.join(sorted(s.split()))

# Entrada del usuario
input_str = input("Ingrese una cadena: ")

# Ordenar palabras
sorted_str = sort_words(input_str)

# Mostrar resultados
print("Palabras ordenadas:", sorted_str)

""""
Funcionalidad
Este programa ordena alfabéticamente las palabras de una cadena.

Entrada de datos:
Se ingresa una cadena de texto.
Cálculo y salida:
Se usa split() para dividir la cadena en palabras.
Se usa sorted() para ordenar la lista de palabras.
Se imprimen las palabras ordenadas.
"""""

def reversar_booleano(valor):
    if isinstance(valor, bool):
        return not valor
    else:
        return "boolean expected"

# Ejemplo de uso
print(reversar_booleano(True))  # False
print(reversar_booleano(False))  # True
print(reversar_booleano(0))      # "boolean expected"

""""
Funcionalidad:
Este programa toma un valor booleano y lo invierte. Si el valor no es booleano, devuelve un mensaje de error.

Entrada de datos:
Se ingresa un valor booleano (True o False) o cualquier otro tipo de dato.

Cálculo y salida:
Verificación del tipo de dato:
Se verifica si el valor ingresado es de tipo booleano usando isinstance().

Inversión del valor:
Si es booleano, se invierte usando not. Si no, se devuelve el mensaje "boolean expected".
"""""
def calcular_grosor(n):
    grosor_inicial_mm = 0.5
    grosor_final_mm = grosor_inicial_mm * (2 ** n)
    grosor_final_m = grosor_final_mm / 1000  # Convertir a metros
    return f"{grosor_final_m:.3f}m"

# Ejemplo de uso
print(calcular_grosor(1))  # 0.001m
print(calcular_grosor(4))  # 0.008m
print(calcular_grosor(21)) # 1048.576m

""""
Funcionalidad:
Este programa calcula el grosor de un papel después de doblarlo n veces, comenzando con un grosor de 0.5 mm.

Entrada de datos:
Se ingresa un número entero n que representa la cantidad de veces que se dobla el papel.

Cálculo y salida:
Cálculo del grosor final:
Se utiliza la fórmula grosor_final = grosor_inicial * (2 ** n), donde grosor_inicial = 0.5 mm.

Conversión a metros:
El grosor final se convierte de milímetros a metros dividiendo entre 1000.

Redondeo:
El resultado se redondea a 3 decimales.
"""""
def indices_mayusculas(cadena):
    return [i for i, char in enumerate(cadena) if char.isupper()]

# Ejemplo de uso
print(indices_mayusculas("eDaBiT"))        # [1, 3, 5]
print(indices_mayusculas("eQuINoX"))       # [1, 3, 4, 6]
print(indices_mayusculas("determine"))     # []
print(indices_mayusculas("STRIKE"))        # [0, 1, 2, 3, 4, 5]

""""
Funcionalidad:
Este programa toma una cadena y devuelve una lista con los índices de todas las letras mayúsculas en la cadena.

Entrada de datos:
Se ingresa una cadena de texto.

Cálculo y salida:
Identificación de mayúsculas:
Se recorre la cadena y se verifica si cada carácter es una letra mayúscula usando isupper().

Almacenamiento de índices:
Los índices de los caracteres mayúsculos se almacenan en una lista.
"""""
def encontrar_pares(n):
    return [x for x in range(1, n + 1) if x % 2 == 0]

# Ejemplo de uso
print(encontrar_pares(8))  # [2, 4, 6, 8]
print(encontrar_pares(4))  # [2, 4]
print(encontrar_pares(2))  # [2]

""""
Funcionalidad:
Este programa encuentra todos los números pares desde 1 hasta un número dado.

Entrada de datos:
Se ingresa un número entero n.

Cálculo y salida:
Generación de números pares:
Se utiliza una lista por comprensión para generar números pares en el rango de 1 a n.

Devolución de la lista:
Se devuelve la lista de números pares.
"""""
def filtrar_enteros(lista):
    return [x for x in lista if isinstance(x, int)]

# Ejemplo de uso
print(filtrar_enteros([1, 2, "a", "b", 4]))  # [1, 2, 4]
print(filtrar_enteros(["A", 0, "Edabit", 1729]))  # [0, 1729]

""""
Funcionalidad:
Este programa toma una lista que contiene tanto cadenas como enteros y devuelve una lista con solo los enteros.

Entrada de datos:
Se ingresa una lista que puede contener cadenas y enteros.

Cálculo y salida:
Filtrado de enteros:
Se utiliza una lista por comprensión para filtrar solo los elementos que son enteros usando isinstance().

Devolución de la lista filtrada:
Se devuelve la lista de enteros.
"""""
def sumar_indices(lista):
    return [i + valor for i, valor in enumerate(lista)]

# Ejemplo de uso
print(sumar_indices([0, 0, 0, 0, 0]))  # [0, 1, 2, 3, 4]
print(sumar_indices([1, 2, 3, 4, 5]))  # [1, 3, 5, 7, 9]

""""
Funcionalidad:
Este programa toma una lista de números y devuelve una nueva lista donde cada elemento es la suma del elemento original y su índice.

Entrada de datos:
Se ingresa una lista de números.

Cálculo y salida:
Suma de índices y valores:
Se utiliza una lista por comprensión para sumar cada elemento con su índice.

Devolución de la lista resultante:
Se devuelve la lista con los valores actualizados.
"""""
import math

def volumen_cono(altura, radio):
    if radio == 0:
        return 0
    volumen = (1/3) * math.pi * (radio ** 2) * altura
    return round(volumen, 2)

# Ejemplo de uso
print(volumen_cono(3, 2))  # 12.57
print(volumen_cono(15, 6)) # 565.49
print(volumen_cono(18, 0)) # 0

""""
Funcionalidad:
Este programa calcula el volumen de un cono dados su altura y radio.

Entrada de datos:
Se ingresan dos valores: la altura (height) y el radio (radius) del cono.

Cálculo y salida:
Fórmula del volumen:
Se utiliza la fórmula del volumen de un cono
Redondeo:
El resultado se redondea a 2 decimales.
"""""
def numero_triangular(n):
    if n < 1:
        return 0
    return n * (n + 1) // 2

# Ejemplo de uso
print(numero_triangular(1))   # 1
print(numero_triangular(6))   # 21
print(numero_triangular(215)) # 23220

""""
Funcionalidad:
Este programa calcula el número de puntos en un triángulo de nivel n en la secuencia de números triangulares.

Entrada de datos:
Se ingresa un número entero n que representa el nivel del triángulo.

Cálculo y salida:
Fórmula del número triangular
Devolución del resultado:
Se devuelve el número de puntos en el triángulo.
"""""
def numero_faltante(lista):
    suma_total = sum(range(1, 11))  # Suma del 1 al 10
    suma_lista = sum(lista)         # Suma de la lista dada
    return suma_total - suma_lista  # Número faltante

# Ejemplo de uso
print(numero_faltante([1, 2, 3, 4, 6, 7, 8, 9, 10]))  # 5
print(numero_faltante([7, 2, 3, 6, 5, 9, 1, 4, 8]))   # 10

""""
Funcionalidad:
Este programa encuentra el número faltante en una lista de números del 1 al 10.

Entrada de datos:
Se ingresa una lista de 9 números entre 1 y 10, faltando uno.

Cálculo y salida:
Suma total esperada:
Se calcula la suma de los números del 1 al 10.

Suma de la lista dada:
Se calcula la suma de los números en la lista.

Diferencia:
El número faltante es la diferencia entre la suma total y la suma de la lista.
"""""
def agregar_y_eliminar(lista, numero):
    if lista:
        lista.pop(0)        # Eliminar el primer elemento
        lista.append(numero) # Agregar el número al final
        return lista
    else:
        return "No list has been selected"

# Ejemplo de uso
print(agregar_y_eliminar([5, 6, 7, 8, 9], 1))  # [6, 7, 8, 9, 1]
print(agregar_y_eliminar([7, 6, 3, 23, 17], 10))  # [6, 3, 23, 17, 10]

""""
Funcionalidad:
Este programa agrega un número al final de una lista y elimina el primer elemento.

Entrada de datos:
Se ingresa una lista de números y un número para agregar.

Cálculo y salida:
Eliminar el primer elemento:
Se usa pop(0) para eliminar el primer elemento de la lista.

Agregar el número al final:
Se usa append() para agregar el número al final de la lista.

Devolución de la lista actualizada:
Se devuelve la lista modificada.
"""""
def sumar_presupuestos(lista):
    return sum(diccionario["budget"] for diccionario in lista)

# Ejemplo de uso
presupuestos = [
    {"name": "John", "age": 21, "budget": 23000},
    {"name": "Steve", "age": 32, "budget": 40000},
    {"name": "Martin", "age": 16, "budget": 2700}
]
print(sumar_presupuestos(presupuestos))  # 65700

""""
Funcionalidad:
Este programa suma los valores de la clave "budget" en una lista de diccionarios.

Entrada de datos:
Se ingresa una lista de diccionarios, donde cada diccionario tiene una clave "budget".

Cálculo y salida:
Suma de presupuestos:
Se recorre la lista y se suman los valores de la clave "budget".

Devolución del total:
Se devuelve la suma total.
"""""
def sumar_presupuestos(lista):
    return sum(diccionario["budget"] for diccionario in lista)

# Ejemplo de uso
presupuestos = [
    {"name": "John", "age": 21, "budget": 23000},
    {"name": "Steve", "age": 32, "budget": 40000},
    {"name": "Martin", "age": 16, "budget": 2700}
]
print(sumar_presupuestos(presupuestos))  # 65700

""""
Funcionalidad:
Este programa suma los valores de la clave "budget" en una lista de diccionarios.

Entrada de datos:
Se ingresa una lista de diccionarios, donde cada diccionario tiene una clave "budget".

Cálculo y salida:
Suma de presupuestos:
Se recorre la lista y se suman los valores de la clave "budget".

Devolución del total:
Se devuelve la suma total.
"""""
def ordenar_letras(cadena):
    return ''.join(sorted(cadena))

# Ejemplo de uso
print(ordenar_letras("hello"))        # ehllo
print(ordenar_letras("edabit"))       # abdeit
print(ordenar_letras("javascript"))   # aacijprstv

""""
Funcionalidad:
Este programa ordena las letras de una cadena en orden alfabético.

Entrada de datos:
Se ingresa una cadena de texto.

Cálculo y salida:
Ordenar las letras:
Se usa sorted() para ordenar las letras de la cadena.

Unión de letras:
Se usa join() para unir las letras ordenadas en una cadena.

Devolución de la cadena ordenada:
Se devuelve la cadena con las letras ordenadas.
"""""

def interes_compuesto(p, t, r, n):
    a = p * (1 + (r / n)) ** (n * t)
    return round(a, 2)

# Ejemplo de uso
print(interes_compuesto(10000, 10, 0.06, 12))  # 18193.97
print(interes_compuesto(100, 1, 0.05, 1))      # 105.0

""""
Funcionalidad:
Este programa calcula el valor de una inversión después de un período de tiempo con interés compuesto.

Entrada de datos:
Se ingresan: el capital inicial (p), el tiempo en años (t), la tasa de interés (r) y el número de períodos de capitalización por año (n).

Cálculo y salida:
Fórmula del interés compuesto:
Se usa la fórmula 
Redondeo:
El resultado se redondea a 2 decimales.
"""""
