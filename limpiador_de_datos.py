nulo = []
valido = []
sin_arroba = []
email = ["juan@mail.com","pedro@mail.com","mario@mail.com"," pedro@mail.com","","maria@mail.com","antonio@mail.com ","  rita@mail.com","", "","pipimazzantiemail.com", "elcholosimeone.com","","lalosbar.com ", "todoporelasado@mail.com"]
for correo in email:
    correo = correo.strip()
    if correo == "":
        nulo.append(correo)
    elif "@" not in correo:
        sin_arroba.append(correo)
    else:
        valido.append(correo)
valido_deduplicado = list(set(valido))
print("Nulos:", nulo)
print("Sin arroba:", sin_arroba)
print("Válidos:", valido_deduplicado)
print("Total lista:", len(email))
print("Total clasificado:", len(nulo) + len(sin_arroba) + len(valido_deduplicado))