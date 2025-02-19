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