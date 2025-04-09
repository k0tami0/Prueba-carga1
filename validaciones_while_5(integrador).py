"""
Integrador Validaciones
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.
"""
print("Bienvenido a la empresa de Censos a continuación se le pediran los siquientes datos: ")
apellido= input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad (debe estar entre 18 y 90 años): "))
while edad > 90 or edad < 18:
    edad = int(input("Edad inválida, por favor ingrese una edad entre 18 y 90 años."))

estado_civil = ["Soltero","Soltera", "Casado", "Casada", "Divorciado", "Divorciada", "Viudo", "Viuda"]
estado_civil_ingresado= input("Escriba su estado civil \n Soltero/a \n Casado/a \n Divorciado/a \n Viudo : ")

while estado_civil_ingresado not in estado_civil:
    print("Escriba unos de los estados civiles mostrados")
    estado_civil_ingresado= input("Ingrese su estado civil \n 1: Soltero/a \n 2: Casado/a \n 3: Divorciado/a \n 4: Viudo/a : ")

legajo = int(input("Ingrese su numero de legajo: "))
while legajo < 999:
    print("El numero de legajo contiene 4 cifras y no puede empezar con 0")
    legajo = int(input("Ingrese su numero de legajo: "))

print(f"{apellido}, {edad} años, estado civil {estado_civil_ingresado}, legajo {legajo}")