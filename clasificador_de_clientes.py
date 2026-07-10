premium = []
regular = []
bajo = []
clientes = {
    "Juan Pérez": 35000.00, 
    "María Magdalena": 15000.00, 
    "Carlos López": 5000.00, 
    "Carlos Villabuena": 25000.00, 
    "Ana Torres": 10000.00, 
    "Luis Fernández": 20000.00, 
    "Laura Gómez": 30000.00, 
    "Pedro Martínez": 40000.00, 
    "Sofía Ramírez": 15000.00, 
    "Diego Sánchez": 5000.00
    }
for nombre, compras in clientes.items():
    print (f" {nombre} ha realizado compras por un valor de ${compras:.2f}")
    if compras >= 50000.00:
        premium.append(nombre)
    elif compras >= 10000.00:
        regular.append(nombre)
    else:
        bajo.append(nombre)
print (f"Clientes Premium: {premium}")
print (f"Clientes Regulares: {regular}")
print (f"Clientes de Al Paso: {bajo}")
print (f"hay {len(premium)} clientes premium, {len(regular)} clientes regulares y {len(bajo)} clientes de al paso")