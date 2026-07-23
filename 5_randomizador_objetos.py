objetos = [
    {'ID': 1, 'nombre': 'Diadema de estallidos', 'tipo': 'Objeto maravilloso', 'rareza': 'Poco comun', 'locacion': ['estatua', 'cadaver']},
    {'ID': 2, 'nombre': 'Maceta del despertar', 'tipo': 'Objeto maravilloso', 'rareza': 'Comun', 'locacion': ['mesa', 'escombros']},
    {'ID': 3, 'nombre': 'Anillo de natacion', 'tipo': 'Anillo', 'rareza': 'Poco comun', 'locacion': ['armario', 'cadaver']},
    {'ID': 4, 'nombre': 'Pocion de amistad animal', 'tipo': 'Pocion', 'rareza': 'Comun', 'locacion': ['cofre']},
    {'ID': 5, 'nombre': 'Armadura de resistencia (relampago)', 'tipo': 'Armadura', 'rareza': 'Poco comun', 'locacion': ['cofre']},
    {'ID': 6, 'nombre': 'Baston de Wyllow', 'tipo': 'Objeto maravilloso (unico)', 'rareza': 'Poco comun', 'locacion': ['mesa', 'altar']},
    {'ID': 7, 'nombre': 'Perla negra de deteccion de no-muertos', 'tipo': 'Objeto maravilloso (unico)', 'rareza': 'Menor', 'locacion': ['boveda', 'cofre']},
    {'ID': 8, 'nombre': 'Coraza +1 (drow)', 'tipo': 'Armadura', 'rareza': 'Poco comun', 'locacion': ['cadaver', 'botin de combate']},
    {'ID': 9, 'nombre': 'Cetro de mando', 'tipo': 'Vara/cetro', 'rareza': 'Raro', 'locacion': ['botin de combate']},
    {'ID': 10, 'nombre': 'Diadema de intelecto', 'tipo': 'Objeto maravilloso', 'rareza': 'Raro', 'locacion': ['boveda', 'altar']},
    {'ID': 11, 'nombre': 'Gema de vision', 'tipo': 'Objeto maravilloso', 'rareza': 'Raro', 'locacion': ['cofre']},
    {'ID': 12, 'nombre': 'Guanteletes de fuerza de ogro', 'tipo': 'Objeto maravilloso', 'rareza': 'Poco comun', 'locacion': ['cadaver']},
    {'ID': 13, 'nombre': 'Daga de la ponzona', 'tipo': 'Arma', 'rareza': 'Poco comun', 'locacion': ['botin de combate']},
    {'ID': 14, 'nombre': 'Pocion de sanacion suprema', 'tipo': 'Pocion', 'rareza': 'Muy rara', 'locacion': ['botin de combate', 'cofre']},
    {'ID': 15, 'nombre': 'Cuerno del Laberinto Infinito', 'tipo': 'Objeto maravilloso (unico)', 'rareza': 'Muy raro', 'locacion': ['botin de combate']},
    {'ID': 16, 'nombre': 'Pergamino de conjuro de telequinesis', 'tipo': 'Pergamino', 'rareza': 'Muy raro', 'locacion': ['botin de combate', 'biblioteca']},
    {'ID': 17, 'nombre': 'Pocion de vitalidad', 'tipo': 'Pocion', 'rareza': 'Muy rara', 'locacion': ['cofre']},
    {'ID': 18, 'nombre': 'Pocion de encoger', 'tipo': 'Pocion', 'rareza': 'Poco comun', 'locacion': ['gruta']},
    {'ID': 19, 'nombre': 'Pocion de longevidad', 'tipo': 'Pocion', 'rareza': 'Rara', 'locacion': ['gruta']},
    {'ID': 20, 'nombre': 'Vara de Puerto Estelar', 'tipo': 'Vara (unica)', 'rareza': 'Unica', 'locacion': ['botin de combate']},
    {'ID': 21, 'nombre': 'Pocion de resistencia (fuego/acido)', 'tipo': 'Pocion', 'rareza': 'Poco comun', 'locacion': ['botin de combate', 'cofre']},
    {'ID': 22, 'nombre': 'Varita de deteccion magica', 'tipo': 'Varita', 'rareza': 'Poco comun', 'locacion': ['botin de combate']},
    {'ID': 23, 'nombre': 'Ficha de pluma de Quaal (arbol)', 'tipo': 'Objeto maravilloso (consumible)', 'rareza': 'Poco comun', 'locacion': ['cofre']},
    {'ID': 24, 'nombre': 'Gema del resplandor', 'tipo': 'Objeto maravilloso', 'rareza': 'Poco comun', 'locacion': ['recompensa']},
    {'ID': 25, 'nombre': 'Botas de pista falsa', 'tipo': 'Objeto maravilloso', 'rareza': 'Poco comun', 'locacion': ['recompensa']},
    {'ID': 26, 'nombre': 'Orbe de la direccion', 'tipo': 'Objeto maravilloso', 'rareza': 'Poco comun', 'locacion': ['recompensa']},
    {'ID': 27, 'nombre': 'Piedras mensajeras (par)', 'tipo': 'Objeto maravilloso', 'rareza': 'Poco comun', 'locacion': ['cofre', 'escritorio']},
    {'ID': 28, 'nombre': 'Pocion de leer mentes', 'tipo': 'Pocion', 'rareza': 'Poco comun', 'locacion': ['gruta', 'recompensa']},
    {'ID': 29, 'nombre': 'Pocion de curacion superior', 'tipo': 'Pocion', 'rareza': 'Muy rara', 'locacion': ['gruta', 'recompensa']},
    {'ID': 30, 'nombre': 'Carillon de apertura', 'tipo': 'Objeto maravilloso', 'rareza': 'Poco comun', 'locacion': ['boveda', 'gruta']},
    {'ID': 31, 'nombre': 'Amuleto a prueba de deteccion y localizacion', 'tipo': 'Objeto maravilloso', 'rareza': 'Raro', 'locacion': ['botin de combate']},
    {'ID': 32, 'nombre': 'Pocion de invisibilidad', 'tipo': 'Pocion', 'rareza': 'Muy rara', 'locacion': ['laboratorio']},
    {'ID': 33, 'nombre': 'Decantador de agua interminable', 'tipo': 'Objeto maravilloso', 'rareza': 'Poco comun', 'locacion': ['fuente']},
    {'ID': 34, 'nombre': 'Pocion de fuerza de gigante de las nubes', 'tipo': 'Pocion', 'rareza': 'Muy rara', 'locacion': ['cofre']},
    {'ID': 35, 'nombre': 'Tablilla de cristal negro', 'tipo': 'Objeto maravilloso (unico)', 'rareza': 'Legendario', 'locacion': ['escritorio', 'altar']},
    {'ID': 36, 'nombre': 'Anillo de control de scaladars', 'tipo': 'Anillo (unico)', 'rareza': 'Unica', 'locacion': ['botin de combate']},
    {'ID': 37, 'nombre': 'Arpa de Anstruth (instrumento de los bardos)', 'tipo': 'Objeto maravilloso', 'rareza': 'Raro', 'locacion': ['altar']},
    {'ID': 38, 'nombre': 'Libro de conjuros de Halaster', 'tipo': 'Grimorio (unico)', 'rareza': 'Unica', 'locacion': ['biblioteca', 'escritorio']},
    {'ID': 39, 'nombre': 'Monedas sueltas (bandidos/goblins/drows menores)', 'tipo': 'Moneda', 'rareza': 'No aplica', 'locacion': ['botin de combate', 'cofre']},
    {'ID': 40, 'nombre': 'Gemas menores (agata, circonita, granate, amatista, turmalina)', 'tipo': 'Gema', 'rareza': 'No aplica', 'locacion': ['estatua', 'cadaver', 'mural']},
    {'ID': 41, 'nombre': 'Joyeria menor (coronas, brazaletes, colgantes)', 'tipo': 'Objeto de arte', 'rareza': 'No aplica', 'locacion': ['cadaver', 'cofre']},
    {'ID': 42, 'nombre': 'Alijo del arbol-druida', 'tipo': 'Moneda', 'rareza': 'No aplica', 'locacion': ['boveda']},
    {'ID': 43, 'nombre': 'Piedras de talla (agatas, cornalinas, citrinas, amatista)', 'tipo': 'Gema', 'rareza': 'No aplica', 'locacion': ['mural']},
    {'ID': 44, 'nombre': 'Paneles de cristal de pared', 'tipo': 'Objeto de arte', 'rareza': 'No aplica', 'locacion': ['mural']},
    {'ID': 45, 'nombre': 'Ajedrez dragon imperial', 'tipo': 'Objeto de arte (unico)', 'rareza': 'No aplica', 'locacion': ['mesa']},
    {'ID': 46, 'nombre': 'Boveda de los bullywugs', 'tipo': 'Moneda', 'rareza': 'No aplica', 'locacion': ['boveda']},
    {'ID': 47, 'nombre': 'Cofre con gemas y pociones', 'tipo': 'Mixto', 'rareza': 'No aplica', 'locacion': ['cofre']},
    {'ID': 48, 'nombre': 'Cuna con aranas enjoyadas', 'tipo': 'Objeto de arte', 'rareza': 'No aplica', 'locacion': ['cuna']},
    {'ID': 49, 'nombre': 'Cofres de componentes de conjuro (x24)', 'tipo': 'Recurso de lanzador', 'rareza': 'No aplica', 'locacion': ['cofre', 'laboratorio']},
    {'ID': 50, 'nombre': 'Zafiros negros (ojos de golem)', 'tipo': 'Gema', 'rareza': 'No aplica', 'locacion': ['estatua']},
    {'ID': 51, 'nombre': 'Tesoro de los dragones jovenes', 'tipo': 'Moneda masiva', 'rareza': 'No aplica', 'locacion': ['boveda', 'gruta']},
    {'ID': 52, 'nombre': 'Diamante suelto', 'tipo': 'Gema', 'rareza': 'No aplica', 'locacion': ['cofre']},
    {'ID': 53, 'nombre': 'Diadema de ambar', 'tipo': 'Objeto de arte', 'rareza': 'No aplica', 'locacion': ['botin de combate']},
    {'ID': 54, 'nombre': 'Concha de caracol de oro', 'tipo': 'Metal precioso', 'rareza': 'No aplica', 'locacion': ['botin de combate']},
    {'ID': 55, 'nombre': 'Diadema funeraria enana (con aguamarinas)', 'tipo': 'Objeto de arte', 'rareza': 'No aplica', 'locacion': ['boveda']},
    {'ID': 56, 'nombre': 'Escudo artesanal (no magico)', 'tipo': 'Objeto de arte', 'rareza': 'No aplica', 'locacion': ['taller']},
    {'ID': 57, 'nombre': 'Zafiros amarillos (llaves de mecanismo)', 'tipo': 'Gema', 'rareza': 'No aplica', 'locacion': ['botin de combate']},
    {'ID': 58, 'nombre': 'Sujetalibros de oro + tomos magicos', 'tipo': 'Objeto de arte / libro', 'rareza': 'No aplica', 'locacion': ['biblioteca']},
]
import random
locacion_usuario = input("¿Qué locación estás abriendo?\n").strip().lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
posibles_objetos = []
for objeto in objetos:
    if locacion_usuario in objeto['locacion']:
        posibles_objetos.append(objeto)
if len(posibles_objetos) == 0:
    print("No hay objeto :(")
    exit()
objeto_concreto = random.choice(posibles_objetos)
print(f"Allí encuentra: {objeto_concreto['nombre']}")
print(f"Su ID es: {objeto_concreto['ID']}")