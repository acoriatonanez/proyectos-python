productos = [
    {"nombre": "heladera", "precio": 2000.00},
    {"nombre": "lavarropas", "precio": 1500.00},
    {"nombre": "microondas", "precio": 800.00},
    {"nombre": "cafetera", "precio": 500.00},
    {"nombre": "tostadora", "precio": 300.00},
    {"nombre": "licuadora", "precio": 400.00},
    {"nombre": "batidora", "precio": 200.00},
    {"nombre": "sodastream", "precio": 100.00},
    {"nombre": "secadora", "precio": 1200.00},
    {"nombre": "lavasecadora", "precio": 1800.00}
]
for producto in productos:
    if producto["precio"] > 1000:
        producto["precio_con_descuento"] = producto["precio"] * 0.9
    else:
            producto["precio_con_descuento"] = producto["precio"]
    producto["precio_con_iva"] = producto["precio_con_descuento"] * 1.21
    print(f"El producto es {producto["nombre"]}, su precio original con o sin descuento es ${producto["precio_con_descuento"]:.2f} y su precio con IVA es ${producto["precio_con_iva"]:.2f}")