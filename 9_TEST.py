import openpyxl
libro = openpyxl.load_workbook("Dataset-Supertienda.xlsx")
hoja = libro["Ventas"]
for numero_fila, fila in enumerate(
        hoja.iter_rows(min_row=2, values_only=True),
        start=2):

    if fila[16] is None:
        print(numero_fila, fila)