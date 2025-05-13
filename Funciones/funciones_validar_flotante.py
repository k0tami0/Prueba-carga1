

mensaje_usuario = input("Ingrese su mensaje: ")

for i in mensaje_usuario:
    print(i)


palabra = "abcdefghijklazb"
letras={}
letras_repetidas=''

for letra in palabra:
    if letras.get(letra):
        letras_repetidas += letra
    else:
        letras[letra] = True
        
print(letras_repetidas)