jugadores = [
    {"nombre": "Lionel Messi", "pais": "ARG", "goles": 8, "asistencias": 4, "minutos_jugados": 712},
    {"nombre": "Kylian Mbappe", "pais": "FRA", "goles": 8, "asistencias": 3, "minutos_jugados": 666},
    {"nombre": "Erling Haaland", "pais": "NOR", "goles": 7, "asistencias": 0, "minutos_jugados": 537},
    {"nombre": "Jude Bellingham", "pais": "ENG", "goles": 6, "asistencias": 1, "minutos_jugados": 679},
    {"nombre": "Harry Kane", "pais": "ENG", "goles": 6, "asistencias": 1, "minutos_jugados": 732},
    {"nombre": "Ousmane Dembele", "pais": "FRA", "goles": 5, "asistencias": 2, "minutos_jugados": 595},
    {"nombre": "Mikel Oyarzabal", "pais": "ESP", "goles": 5, "asistencias": 1, "minutos_jugados": 599},
    {"nombre": "Ismaila Sarr", "pais": "SEN", "goles": 4, "asistencias": 1, "minutos_jugados": 419},
    {"nombre": "Julian Quinones", "pais": "MEX", "goles": 4, "asistencias": 1, "minutos_jugados": 440},
    {"nombre": "Vinicius Junior", "pais": "BRA", "goles": 4, "asistencias": 1, "minutos_jugados": 505},
    {"nombre": "Deniz Undav", "pais": "GER", "goles": 3, "asistencias": 2, "minutos_jugados": 174},
    {"nombre": "Johan Manzambi", "pais": "SUI", "goles": 3, "asistencias": 2, "minutos_jugados": 220},
    {"nombre": "Romelu Lukaku", "pais": "BEL", "goles": 3, "asistencias": 1, "minutos_jugados": 279},
    {"nombre": "Lautaro Martinez", "pais": "ARG", "goles": 3, "asistencias": 1, "minutos_jugados": 368},
    {"nombre": "Charles De Ketelaere", "pais": "BEL", "goles": 3, "asistencias": 1, "minutos_jugados": 385},
    {"nombre": "Cody Gakpo", "pais": "NED", "goles": 3, "asistencias": 1, "minutos_jugados": 394},
    {"nombre": "Brian Brobbey", "pais": "NED", "goles": 3, "asistencias": 0, "minutos_jugados": 245},
    {"nombre": "Elijah Just", "pais": "NZL", "goles": 3, "asistencias": 0, "minutos_jugados": 291},
    {"nombre": "Matheus Cunha", "pais": "BRA", "goles": 3, "asistencias": 0, "minutos_jugados": 324},
    {"nombre": "Folarin Balogun", "pais": "USA", "goles": 3, "asistencias": 0, "minutos_jugados": 348},
    {"nombre": "Raul Jimenez", "pais": "MEX", "goles": 3, "asistencias": 0, "minutos_jugados": 348},
    {"nombre": "Kai Havertz", "pais": "GER", "goles": 3, "asistencias": 0, "minutos_jugados": 392},
    {"nombre": "Yoane Wissa", "pais": "COD", "goles": 3, "asistencias": 0, "minutos_jugados": 409},
    {"nombre": "Ismael Saibari", "pais": "MAR", "goles": 3, "asistencias": 0, "minutos_jugados": 411},
    {"nombre": "Jonathan David", "pais": "CAN", "goles": 3, "asistencias": 0, "minutos_jugados": 475},
    {"nombre": "Cristiano Ronaldo", "pais": "POR", "goles": 3, "asistencias": 0, "minutos_jugados": 490},
    {"nombre": "Crysencio Summerville", "pais": "NED", "goles": 2, "asistencias": 2, "minutos_jugados": 282},
    {"nombre": "Breel Embolo", "pais": "SUI", "goles": 2, "asistencias": 2, "minutos_jugados": 531},
    {"nombre": "Leandro Trossard", "pais": "BEL", "goles": 2, "asistencias": 2, "minutos_jugados": 561},
    {"nombre": "Soufiane Rahimi", "pais": "MAR", "goles": 2, "asistencias": 1, "minutos_jugados": 215},
    {"nombre": "Nicolas Pepe", "pais": "CIV", "goles": 2, "asistencias": 1, "minutos_jugados": 255},
    {"nombre": "Pape Gueye", "pais": "SEN", "goles": 2, "asistencias": 1, "minutos_jugados": 257},
    {"nombre": "Maxi Araujo", "pais": "URU", "goles": 2, "asistencias": 1, "minutos_jugados": 278},
    {"nombre": "Riyad Mahrez", "pais": "ALG", "goles": 2, "asistencias": 1, "minutos_jugados": 288},
    {"nombre": "Ramin Rezaeian", "pais": "IRN", "goles": 2, "asistencias": 1, "minutos_jugados": 309},
    {"nombre": "Ruben Vargas", "pais": "SUI", "goles": 2, "asistencias": 1, "minutos_jugados": 314},
    {"nombre": "Ayase Ueda", "pais": "JPN", "goles": 2, "asistencias": 1, "minutos_jugados": 349},
    {"nombre": "Bradley Barcola", "pais": "FRA", "goles": 2, "asistencias": 1, "minutos_jugados": 379},
    {"nombre": "Mostafa Zico", "pais": "EGY", "goles": 2, "asistencias": 1, "minutos_jugados": 398},
    {"nombre": "Malik Tillman", "pais": "USA", "goles": 2, "asistencias": 1, "minutos_jugados": 415},
    {"nombre": "Ermin Mahmic", "pais": "BIH", "goles": 2, "asistencias": 0, "minutos_jugados": 88},
    {"nombre": "Habib Diarra", "pais": "SEN", "goles": 2, "asistencias": 0, "minutos_jugados": 168},
    {"nombre": "Marko Arnautovic", "pais": "AUT", "goles": 2, "asistencias": 0, "minutos_jugados": 173},
    {"nombre": "Mikel Merino", "pais": "ESP", "goles": 2, "asistencias": 0, "minutos_jugados": 200},
    {"nombre": "Amad Diallo", "pais": "CIV", "goles": 2, "asistencias": 0, "minutos_jugados": 211},
    {"nombre": "Cyle Larin", "pais": "CAN", "goles": 2, "asistencias": 0, "minutos_jugados": 224},
    {"nombre": "Anthony Elanga", "pais": "SWE", "goles": 2, "asistencias": 0, "minutos_jugados": 247},
    {"nombre": "Daichi Kamada", "pais": "JPN", "goles": 2, "asistencias": 0, "minutos_jugados": 359},
    {"nombre": "Yasin Ayari", "pais": "SWE", "goles": 2, "asistencias": 0, "minutos_jugados": 371},
    {"nombre": "Emam Ashour", "pais": "EGY", "goles": 2, "asistencias": 0, "minutos_jugados": 395},
    {"nombre": "Dan Ndoye", "pais": "SUI", "goles": 2, "asistencias": 0, "minutos_jugados": 437},
    {"nombre": "Daniel Munoz", "pais": "COL", "goles": 2, "asistencias": 0, "minutos_jugados": 451},
    {"nombre": "Azzedine Ounahi", "pais": "MAR", "goles": 2, "asistencias": 0, "minutos_jugados": 477},
    {"nombre": "Pedro Porro", "pais": "ESP", "goles": 2, "asistencias": 0, "minutos_jugados": 499},
    {"nombre": "Youri Tielemans", "pais": "BEL", "goles": 2, "asistencias": 0, "minutos_jugados": 538},
    {"nombre": "Enzo Fernandez", "pais": "ARG", "goles": 2, "asistencias": 0, "minutos_jugados": 658},
    {"nombre": "Andreas Schjelderup", "pais": "NOR", "goles": 1, "asistencias": 3, "minutos_jugados": 297},
    {"nombre": "Alexander Isak", "pais": "SWE", "goles": 1, "asistencias": 3, "minutos_jugados": 389},
    {"nombre": "Anthony Gordon", "pais": "ENG", "goles": 1, "asistencias": 3, "minutos_jugados": 442},
    {"nombre": "Iliman Ndiaye", "pais": "SEN", "goles": 1, "asistencias": 2, "minutos_jugados": 134},
    {"nombre": "Nathan Saliba", "pais": "CAN", "goles": 1, "asistencias": 2, "minutos_jugados": 206},
    {"nombre": "Hans Vanaken", "pais": "BEL", "goles": 1, "asistencias": 2, "minutos_jugados": 362},
    {"nombre": "Viktor Gyokeres", "pais": "SWE", "goles": 1, "asistencias": 2, "minutos_jugados": 400},
    {"nombre": "Julio Enciso", "pais": "PAR", "goles": 1, "asistencias": 2, "minutos_jugados": 431},
    {"nombre": "Mohamed Salah", "pais": "EGY", "goles": 1, "asistencias": 2, "minutos_jugados": 469},
    {"nombre": "Achraf Hakimi", "pais": "MAR", "goles": 1, "asistencias": 2, "minutos_jugados": 650},
    {"nombre": "Promise David", "pais": "CAN", "goles": 1, "asistencias": 1, "minutos_jugados": 105},
    {"nombre": "Baris Alper Yilmaz", "pais": "TUR", "goles": 1, "asistencias": 1, "minutos_jugados": 200},
    {"nombre": "Rafael Leao", "pais": "POR", "goles": 1, "asistencias": 1, "minutos_jugados": 203},
    {"nombre": "Trezeguet", "pais": "EGY", "goles": 1, "asistencias": 1, "minutos_jugados": 204},
    {"nombre": "Mousa Altamari", "pais": "JOR", "goles": 1, "asistencias": 1, "minutos_jugados": 230},
    {"nombre": "Sebastian Berhalter", "pais": "USA", "goles": 1, "asistencias": 1, "minutos_jugados": 231},
    {"nombre": "Luis Romo", "pais": "MEX", "goles": 1, "asistencias": 1, "minutos_jugados": 284},
    {"nombre": "Hwang Inbeom", "pais": "KOR", "goles": 1, "asistencias": 1, "minutos_jugados": 286},
    {"nombre": "Felix Nmecha", "pais": "GER", "goles": 1, "asistencias": 1, "minutos_jugados": 299},
    {"nombre": "Kaishu Sano", "pais": "JPN", "goles": 1, "asistencias": 1, "minutos_jugados": 303},
    {"nombre": "Nathaniel Brown", "pais": "GER", "goles": 1, "asistencias": 1, "minutos_jugados": 319},
    {"nombre": "Keito Nakamura", "pais": "JPN", "goles": 1, "asistencias": 1, "minutos_jugados": 330},
    {"nombre": "Petar Sucic", "pais": "CRO", "goles": 1, "asistencias": 1, "minutos_jugados": 338},
    {"nombre": "Desire Doue", "pais": "FRA", "goles": 1, "asistencias": 1, "minutos_jugados": 400},
    {"nombre": "Ivan Perisic", "pais": "CRO", "goles": 1, "asistencias": 1, "minutos_jugados": 413},
    {"nombre": "Virgil Van Dijk", "pais": "NED", "goles": 1, "asistencias": 1, "minutos_jugados": 432},
    {"nombre": "Matias Galarza", "pais": "PAR", "goles": 1, "asistencias": 1, "minutos_jugados": 439},
    {"nombre": "Alex Freeman", "pais": "USA", "goles": 1, "asistencias": 1, "minutos_jugados": 442},
    {"nombre": "Alex Baena", "pais": "ESP", "goles": 1, "asistencias": 1, "minutos_jugados": 444},
    {"nombre": "Luis Diaz", "pais": "COL", "goles": 1, "asistencias": 1, "minutos_jugados": 525},
    {"nombre": "Lisandro Martinez", "pais": "ARG", "goles": 1, "asistencias": 1, "minutos_jugados": 664},
    {"nombre": "Alexis Mac Allister", "pais": "ARG", "goles": 1, "asistencias": 1, "minutos_jugados": 728},
    {"nombre": "Kaan Ayhan", "pais": "TUR", "goles": 1, "asistencias": 0, "minutos_jugados": 11},
    {"nombre": "Mattias Svanberg", "pais": "SWE", "goles": 1, "asistencias": 0, "minutos_jugados": 25},
    {"nombre": "Mahmoud Saber", "pais": "EGY", "goles": 1, "asistencias": 0, "minutos_jugados": 51},
    {"nombre": "Nadhir Benbouali", "pais": "ALG", "goles": 1, "asistencias": 0, "minutos_jugados": 52},
    {"nombre": "Neymar Jr", "pais": "BRA", "goles": 1, "asistencias": 0, "minutos_jugados": 55},
    {"nombre": "Fiston Mayele", "pais": "COD", "goles": 1, "asistencias": 0, "minutos_jugados": 55},
    {"nombre": "Goncalo Ramos", "pais": "POR", "goles": 1, "asistencias": 0, "minutos_jugados": 58},
    {"nombre": "Giovani Lo Celso", "pais": "ARG", "goles": 1, "asistencias": 0, "minutos_jugados": 64},
    {"nombre": "Hassan Alhaydos", "pais": "QAT", "goles": 1, "asistencias": 0, "minutos_jugados": 69},
    {"nombre": "Jovo Lukic", "pais": "BIH", "goles": 1, "asistencias": 0, "minutos_jugados": 77},
    {"nombre": "Mateo Chavez", "pais": "MEX", "goles": 1, "asistencias": 0, "minutos_jugados": 81},
    {"nombre": "Sasa Kalajdzic", "pais": "AUT", "goles": 1, "asistencias": 0, "minutos_jugados": 88}
]
maximos_goleadores = []
buenos_goleadores = []
otros_goleadores = []
goleadores = {}
#Para poder recrear lo realizado el día 3 'clasigficador de clientes', debo generar a partir de esta
#lista, una diccionario con llave = nombre u valor = cantidad de goles, eso imita el nombre y compras.
for jugador in jugadores:
    goleadores[jugador['nombre']] = jugador['goles']
for nombre, goles in goleadores.items():
    if goles >= 6:
        maximos_goleadores.append(nombre)
    elif goles >=3:
        buenos_goleadores.append(nombre)
    else:
        otros_goleadores.append(nombre)
print(f"""Los máximos goleadores de la comeptición hasta la fecha son:
{', '.join(maximos_goleadores) if maximos_goleadores else 'Ninguno'}""")
print(" ")
print(f"""Los goleadores destacables de la competición hasta la fecha son:
{', '.join(buenos_goleadores) if buenos_goleadores else 'Ninguno'}""")
print(" ")
print(f"""Los otros goleadores de la competición hasta la fecha son:
{', '.join(otros_goleadores) if otros_goleadores else 'Ninguno'}""")