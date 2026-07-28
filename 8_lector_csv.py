import csv
def acumulador(ruta_csv,criterio):
    with open(ruta_csv,"r",encoding="utf-8") as archivo:
        ganancia_por_criterio = {}
        lector = csv.DictReader(archivo)
        for fila in lector:
            sales = float(fila['Sales'])
            quantity = int(fila['Quantity'])
            ganancia_fila = sales * quantity
            separador = fila[criterio]
            if separador in ganancia_por_criterio:
                ganancia_por_criterio[separador] = ganancia_por_criterio[separador] + ganancia_fila
            else:
                ganancia_por_criterio[separador] = ganancia_fila
    return ganancia_por_criterio
    
ganancia_por_region = acumulador("/home/acoriatonanez/dev/proyectos-python/superstore_muestra.csv","Region")      
print(f"Este: {ganancia_por_region['East']:.2f}")
print(f"Oeste: {ganancia_por_region['West']:.2f}")
print(f"Central: {ganancia_por_region['Central']:.2f}")
print(f"Sur: {ganancia_por_region['South']:.2f}")
def generador_lista_csv(diccionario,ruta_destino):
    lista_filas = []
    for clave, valor in diccionario.items():
        lista_filas.append([clave, round(valor,2)])
    with open(ruta_destino, "w", encoding="utf-8", newline="") as archivo_salida:
        escritor = csv.writer(archivo_salida)
        escritor.writerows(lista_filas)
generador_lista_csv(ganancia_por_region,"/ganancia_por_region.csv")