def calcular_precio_con_iva(precio_sin_iva : float , valor_iva : int = 21) -> float | None:
    """Permite calcular el valor con iva de un producto
    Args:
        precio_sin_iva (float): Recibe el valor sin iva aplicado.
        valor_iva (int, optional): El valor de aumento. Por defecto es 21%.

    Returns:
        float: El valor con iva aplicado.
        None: En caso de error.
    """
    resultado = None
    if (type(precio_sin_iva) == float or type(precio_sin_iva) == int) and type(valor_iva) == int:
        resultado = precio_sin_iva * (1 + valor_iva / 100)
    return resultado


valor_con_iva= calcular_precio_con_iva("sss")
if valor_con_iva != None:
    print(f"El valor con iva aplicado es de {valor_con_iva}")
else:
    print("Se produjo un error!!")