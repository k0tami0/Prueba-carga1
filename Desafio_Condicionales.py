#VALORES FIJOS
CARGO_FIJO = 7000
VALOR_M_CUBICO = 200
IVA= 0.21
bonificacion = 0
recargo = 0

#ENTRADAS
consumo_cliente = int(input("Ingrese el consumo del cliente: "))
tipo_cliente = input("Ingrese el tipo de cliente que realizó el consumo (Residencial, Comercial o Industrial): ") 

#PROCESOS
subtotal = CARGO_FIJO + (consumo_cliente * VALOR_M_CUBICO)

if tipo_cliente == "Residencial":
    if consumo_cliente < 30:
        bonificacion = 0.10
    elif consumo_cliente > 80:
        recargo = 0.15

elif tipo_cliente == "Comercial":
    if consumo_cliente > 300:
        bonificacion = 0.12
    elif consumo_cliente > 150:
        bonificacion = 0.08
    elif consumo_cliente < 50:
        recargo = 0.05
    
else:
    if consumo_cliente > 1000:
        bonificacion = 0.30
    elif consumo_cliente > 500:
        bonificacion = 0.20
    elif consumo_cliente < 200:
        recargo = 0.10

valor_bonificaciones = subtotal * bonificacion
valor_recargo = subtotal * recargo

subtotal_a_pagar = subtotal - valor_bonificaciones + valor_recargo
valor_iva = subtotal_a_pagar * 0.21

total_a_pagar = subtotal_a_pagar + valor_iva

#SALIDAS
print(f"""
El tipo de cliente {tipo_cliente}, con un consumo de {consumo_cliente} m2 de agua
el subtotal es ${subtotal}
tiene una bonificación de ${valor_bonificaciones}
tiene un recargo de ${valor_recargo}
el subtotal a pagar  es ${subtotal_a_pagar}
el valor final con impuestos agregados (IVA) es de ${total_a_pagar}
""")


