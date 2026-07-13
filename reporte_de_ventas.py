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
total_ventas = {}
total_cantidad = {}
total_importe = 0
for venta in ventas:
    importe = venta['precio_unitario'] * venta['cantidad']
    if venta['producto'] in total_ventas:
        total_ventas[venta['producto']] = total_ventas[venta['producto']] + importe
    else:
        total_ventas[venta['producto']] = importe
    if venta['producto'] in total_cantidad:
        total_cantidad[venta['producto']] = total_cantidad[venta['producto']] + venta['cantidad']
    else:
        total_cantidad[venta['producto']] = venta['cantidad']
    total_importe = total_importe + importe
print(total_ventas)
print(total_cantidad)
print(total_importe)
producto_mas_vendido = max(total_cantidad, key=total_cantidad.get)
print(producto_mas_vendido)