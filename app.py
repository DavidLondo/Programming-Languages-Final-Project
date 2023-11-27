from flask import Flask, render_template, request
import re
import os

app = Flask(__name__)

def cargar_palabras_espanol_desde_txt(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        palabras_espanol = set(line.strip() for line in file)

    return palabras_espanol

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado_texto = ""
    resultado_palabras = ""
    resultado_emojis = ""

    #Flask recibe el texto del formulario
    if request.method == 'POST':
        texto = request.form['texto']

        emojis_diccionario = {
            ":)": "😊",
            ":(": "☹️",
            ":D": "😃",
            ";)": "😉",
            ":P": "😛",
            "xD": "😆",
            ":-)": "😊",
            ":-(": "☹️",
            "(y)": "👍",
            "(n)": "👎",
            "<3": "❤️",
            "\\m/": "🤘",
            ":-O": "😲",
            ":O": "😲",
            ":-|": "😐",
            ":|": "😐",
            ":*": "😘",
            ">:(": "😠",
            "^^": "😊",
            ":-]": "😊"
        }

        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_diccionario = os.path.join(directorio_actual, '0_palabras_todas.txt')
        palabras_espanol = cargar_palabras_espanol_desde_txt(ruta_diccionario)

        texto_sin_emojis = texto
        for emoji, valor in emojis_diccionario.items():
            texto_sin_emojis = texto_sin_emojis.replace(emoji, valor)

        palabras_emojis_encontrados = re.findall(r'\b(?:(?<=\()|\b)(?!(?:B|C|D|F|G|H|I|J|K|L|M|N|Ñ|P|Q|R|S|T|V|W|X|Z)\b)\w{1,}\b', texto, re.IGNORECASE)

        emojis_encontrados = [emoji for emoji, valor in emojis_diccionario.items() if emoji in texto]

        palabras_espanol_contadas = sum(1 for palabra in palabras_emojis_encontrados if palabra.lower() in palabras_espanol)

        resultado_texto = "Texto sin emojis:\n" + texto_sin_emojis
        resultado_palabras = "Número de palabras en español: " + str(palabras_espanol_contadas)
        resultado_emojis = "Número total de emojis: " + str(len(emojis_encontrados))

    return render_template('index.html', resultado_texto=resultado_texto, resultado_palabras=resultado_palabras, resultado_emojis=resultado_emojis)

if __name__ == '__main__':
    app.run(debug=True)
