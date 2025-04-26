"""
Crear una app de venta, donde se seleccione el tipo de producto y valor.
El cliente es consumidor final o necesita factura A?

1- Mostrar sub total
2- Mostrar Sub total con descuentos aplicados con iva en caso de ser consumidor final
3- Mostrar Sub total con descuentos aplicados sin iva en caso de ser Factura A
"""

tipo_cliente= int(input("Ingrese el tipo de cliente \n 1- Consumidor final \n 2- Factura A \n Su respuesta: "))
contador_productos = 0
total_productos= 0
producto_mas_caro = ""
valor_mas_caro = 0
factura_a = False

while True :
    if tipo_cliente == 2:
        factura_a = True
        cuit_cliente = input("Ingrese el cuit del cliente: ")

    ingreso_producto = input("Ingrese el nombre del producto o presione '*' Para finalizar: ")

    if ingreso_producto == "*":
        break
    
    valor_producto = int(input("Ingrese el valor del producto: "))
    cantidad_producto = int(input("Ingrese la cantidad que lleva: "))

    if valor_producto > valor_mas_caro:
        producto_mas_caro = ingreso_producto
        valor_mas_caro = valor_producto

    contador_productos += cantidad_producto

    if cantidad_producto > 1:
        valor_producto *= cantidad_producto
        costo_mas_de_uno = 0
        costo_mas_de_uno += valor_producto

    total_productos += valor_producto + costo_mas_de_uno

iva_aplicado = total_productos * 0.21
subtotal_con_iva = total_productos + iva_aplicado

print(f"""El subtotal sin iva es {total_productos}
El subtotal con iva es {subtotal_con_iva}
la cantidad de productos ingresados fue de {contador_productos}
El producto mas caro fue {producto_mas_caro} y costó {valor_mas_caro}
""")
