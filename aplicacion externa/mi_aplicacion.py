import tkinter as tk

ventana = tk.Tk()
ventana.title("Hola mundo")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="¡Hola desde una ventana!")
etiqueta.pack()

boton = tk.Button(ventana, text="Cerrar", command=ventana.quit)
boton.pack()

ventana.mainloop()