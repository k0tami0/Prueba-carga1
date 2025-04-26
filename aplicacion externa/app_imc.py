"""
App IMC:
Pedir: Altura, Peso 
Calcular IMC con la formula peso / altura ** 2
"""
import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("300x200")  # ancho x alto (en píxeles)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=3, column=0, columnspan=2)

def IMC(altura, peso):
    altura = float(altura)
    peso= int(peso)
    resultado_imc = peso / altura ** 2
    if resultado_imc >= 30:
        print(f"Su IMC es {resultado_imc:.2f} lo que indica obesisdad.")
    elif resultado_imc >= 25:
        print(f"Su IMC es {resultado_imc:.2f} lo que indica sobrepeso.")
    elif resultado_imc >= 18.5:
        print(f"Su IMC es {resultado_imc:.2f} lo que indica peso normal.")
    else:
        print(f"Su IMC es {resultado_imc:.2f} lo que indica bajo peso.")


print("""Bienvenido a la calculadora de IMC:
Acá te paso una tabla común:

🟦 Menos de 18.5 → Bajo peso

🟩 18.5 - 24.9 → Peso normal

🟨 25 - 29.9 → Sobrepeso

🟥 30 o más → Obesidad""")

# Etiqueta y campo para la altura
etiqueta_altura = tk.Label(ventana, text="Altura (m):")
etiqueta_altura.grid(row=0, column=0)

entrada_altura = tk.Entry(ventana)
entrada_altura.grid(row=0, column=1)

# Etiqueta y campo para el peso
etiqueta_peso = tk.Label(ventana, text="Peso (kg):")
etiqueta_peso.grid(row=1, column=0)

entrada_peso = tk.Entry(ventana)
entrada_peso.grid(row=1, column=1)

boton = tk.Button(ventana, text="Calcular.", command="")

boton_calcular = tk.Button(ventana, text="Calcular IMC")
boton_calcular.grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()
IMC(entrada_altura,entrada_peso)
