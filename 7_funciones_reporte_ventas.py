ventas = [
    {
        "fecha": "2026-07-01",
        "producto": "Café en grano (500g)",
        "cantidad": 2,
        "precio_unitario": 4200.50
    },
    {
        "fecha": "2026-07-02",
        "producto": "Termo de acero inoxidable",
        "cantidad": 1,
        "precio_unitario": 18500.00
    },
    {
        "fecha": "2026-07-02",
        "producto": "Taza cerámica",
        "cantidad": 4,
        "precio_unitario": 1200.00
    },
    {
        "fecha": "2026-07-03",
        "producto": "Café en grano (500g)",
        "cantidad": 5,
        "precio_unitario": 4200.50
    },
    {
        "fecha": "2026-07-04",
        "producto": "Filtros de papel (x100)",
        "cantidad": 3,
        "precio_unitario": 850.00
    },
    {
        "fecha": "2026-07-05",
        "producto": "Prensa francesa",
        "cantidad": 1,
        "precio_unitario": 12400.00
    },
    {
        "fecha": "2026-07-06",
        "producto": "Taza cerámica",
        "cantidad": 2,
        "precio_unitario": 1200.00
    },
    {
        "fecha": "2026-07-07",
        "producto": "Molinillo de café manual",
        "cantidad": 1,
        "precio_unitario": 15900.00
    }
]
def acotador_lista_periodo(ventas,fecha_inicio,fecha_fin):
    output = [] 
    for venta in ventas:
        if fecha_inicio <= venta['fecha'] <= fecha_fin:
            output.append(venta)
    return output
def acotador_periodo_lista(ventas,fecha_inicio,fecha_fin):
    output = [venta for venta in ventas if fecha_inicio <= venta['fecha'] <= fecha_fin]
    return output
def sumador_ventas(ventas):
    total_ventas = {}
    for venta in ventas:
        importe = venta['precio_unitario'] * venta['cantidad']
        if venta['producto'] in total_ventas:
            total_ventas[venta['producto']] = total_ventas[venta['producto']] + importe
        else:
            total_ventas[venta['producto']] = importe
    return total_ventas
def sumador_cantidad(ventas):
    total_cantidad = {}
    for venta in ventas:
        if venta['producto'] in total_cantidad:
            total_cantidad[venta['producto']] = total_cantidad[venta['producto']] + venta['cantidad']
        else:
            total_cantidad[venta['producto']] = venta['cantidad']
    return total_cantidad
def encontrar_mayor(diccionario):
    mayor = max(diccionario, key=diccionario.get)
    return mayor
def reportador_de_ventas(importe,cantidad,mayor_importe,mayor_cantidad):
    for producto, ventas in importe.items():
        cantidad_vendida = cantidad[producto]
        print(f"el producto {producto} fue vendido {cantidad_vendida} veces por un importe de ${ventas:.2f}")
    print(f"el lider de ingresos fue {mayor_importe}")
    print(f"el lider de cantidad vendida fue {mayor_cantidad}")
#
ventas_acote_for = acotador_lista_periodo(ventas,'2026-07-02','2026-07-06')
ventas_acote_listcom = acotador_periodo_lista(ventas,'2026-07-02','2026-07-06')
total_ventas = sumador_ventas(ventas_acote_for)
total_cantidad = sumador_cantidad(ventas_acote_for)
mayor_ventas = encontrar_mayor(total_ventas)
mayor_cantidad = encontrar_mayor(total_cantidad)
#
reportador_de_ventas(total_ventas,total_cantidad,mayor_ventas,mayor_cantidad)