def clima_celcius(grados_celcius):
    if grados_celcius > 24:
        print(f"Con {grados_celcius}°C hace calor.")
    elif grados_celcius > 15:
        print(f"Con {grados_celcius}°C la temperatura es agradable.")
    else:
        print(f"Con {grados_celcius}°C hace frío. ¡Recomiendo abrigarse!")

def clima_fahrenheit(grados_fahrenheit):
    if grados_fahrenheit > 75:
        print(f"Con {grados_fahrenheit}°F hace calor.")
    elif grados_fahrenheit > 59:
        print(f"Con {grados_fahrenheit}°F la temperatura es agradable.")
    else:
        print(f"Con {grados_fahrenheit}°F hace frío. ¡Recomiendo abrigarse!")

def conversor_farenheit(temperatura):   
    valor_fahrenheit = 1.8 * temperatura + 32
    return valor_fahrenheit
    

ingreso_usuario = int(input("Ingrese la temperatura (La unidad por defecto es Celcius): "))
pregunta = input("¿Desea convertir la temperatura ingresada a grados farenheit? si / no ")
if pregunta == "si":
    temperatura_fahrenheit = conversor_farenheit(ingreso_usuario)
    clima_fahrenheit(temperatura_fahrenheit)
else:
    clima_celcius(ingreso_usuario)


