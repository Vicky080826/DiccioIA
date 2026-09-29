# Diccionario de palabras y significados
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "BRO": "Forma informal de decir amigo o compañero",
    "SUS": "Algo o alguien sospechoso",
    "XD": "Expresión utilizada para representar una risa"
}

# Pedimos una palabra al usuario
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

# Buscamos la palabra en el diccionario
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Lo siento, esa palabra no está en el diccionario.")
