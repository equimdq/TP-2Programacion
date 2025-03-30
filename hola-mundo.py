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

