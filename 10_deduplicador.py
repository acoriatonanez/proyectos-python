import csv
def combinador(lista_de_rutas):
    consolidado = []
    for ruta in lista_de_rutas:
        with open(ruta,"r",encoding="utf-8") as archivo:
            for fila in csv.DictReader(archivo):
                consolidado.append(fila)
    return consolidado
def limpiador(lista_a_deduplicar, columna):
    deduplicado = []
    repetidos = []
    vistos = set()
    for fila in lista_a_deduplicar:
        clave = fila[columna]
        if clave not in vistos:
            vistos.add(clave)
            deduplicado.append(fila)
        else:
            repetidos.append(fila)
    return deduplicado, repetidos
def escritor_csv(diccionarios,ruta_csv):
    with open(ruta_csv, "w", encoding="utf-8", newline="") as archivo_salida:
        campos = diccionarios[0].keys()
        escritor = csv.DictWriter(archivo_salida,fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(diccionarios)
rutas = ['10_pedidos_2017.csv','10_pedidos_2018.csv']
consolidado = combinador(rutas)
consolidado_deduplicado,repetidas = limpiador(consolidado,'Id_Pedido')
escritor_csv(consolidado_deduplicado, "10_consolidado.csv")
print(len(consolidado))
print(len(consolidado_deduplicado))
print(len(repetidas))