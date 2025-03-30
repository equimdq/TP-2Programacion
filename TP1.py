# ejercicio 1

print ("Hola mundo") 


# ejercicio 2

# Solicitar el nombre del usuario
nombre = input("Ingrese su nombre: ")

# Saludar al usuario
print(f"Hola {nombre}!") 


# ejercicio 3

# Solicitar el nombre, apellido, edad y lugar de residencia del usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))  # Convertir la edad a entero
residencia = input("Ingrese su lugar de residencia: ")

# presentar los datos ingresados
print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")


# ejercicio 4

radio = float(input("Ingrese el radio del círculo: "))

area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio

print(f"El área del círculo es: {area} y su perímetro es: {perimetro}")


# ejercicio 5

segundos = int (input ("Ingrese los segundos a convertir: ")) # Convertir los segundos a entero
horas = segundos // 3600 # Dividir los segundos por 3600 para obtener las horas
print ("Los segundos ingresados equivalen a: ", horas, "horas") # Mostrar el resultado por pantalla


# ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Se le pide un número al usuario
numero = int(input("Ingrese un número: "))

# Llamamos a la función tabla_multiplicar para calcular la tabla de multiplicar del número ingresado1
tabla_multiplicar(numero)


# ejercicio 7

# Pedir al usuario un número distinto de 0
while True:
    num1 = int(input("Ingrese el primer número entero distinto de 0: "))
    num2 = int(input("Ingrese el segundo número entero distinto de 0: "))
    if num1 != 0 and num2 != 0:
        break
    print("Ambos números deben ser distintos de 0. Intente nuevamente.")

# Hacer las operaciones aritméticas básicas con los números ingresados
print(f"Suma: {num1} + {num2} = {num1 + num2}")
print(f"Resta: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicación: {num1} x {num2} = {num1 * num2}")

# Realizar la división y redondear el resultado a 2 decimales
if num2 != 0:
    division = round(num1 / num2, 2)  # Redondea a 2 decimales
    print(f"División: {num1} / {num2} = {division}")
else:
    print("Error: No se puede dividir por 0")


# ejercicio 8

altura_cm = float(input("Ingrese su altura en centímetros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

# Convertir la altura de centímetros a metros para calcular el IMC
altura_m = altura_cm / 100

imc = peso / (altura_m ** 2)

# Mostrar el resultado
print("Su índice de masa corporal es:", imc)


# ejercicio 9

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C equivalen a {fahrenheit}°F")


# ejercicio 10

# Le solicitamos 3 números al usuario
num1 = float(input("Ingrese el primer número: ")) # Convertir el número a flotante
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calculamos el promedio de los números ingresados
promedio = (num1 + num2 + num3) / 3

# Mostramos el promedio por pantalla
print(f"El promedio de los números ingresados es: {round(promedio, 2)}") # Redondear a 2 decimales