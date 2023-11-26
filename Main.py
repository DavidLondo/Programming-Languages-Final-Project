import customtkinter as ctk
import re

def cargar_palabras_espanol_desde_txt(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        palabras_espanol = set(line.strip() for line in file)

    return palabras_espanol

def contar_palabras_y_emojis():
    # Obtener el texto ingresado por el usuario
    texto = text.get("1.0", "end-1c")

    # Definir diccionario de emojis
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

    # Cargar diccionario de palabras en español desde el archivo txt
    ruta_diccionario = r'C:\Users\David\OneDrive - Universidad EAFIT\Documentos\Programación\Lenguajes de programacion\Final\0_palabras_todas.txt'
    palabras_espanol = cargar_palabras_espanol_desde_txt(ruta_diccionario)

    # Reemplazar emojis en el texto
    texto_sin_emojis = texto
    for emoji, valor in emojis_diccionario.items():
        texto_sin_emojis = texto_sin_emojis.replace(emoji, valor)

    # Encontrar emojis y palabras en español utilizando expresiones regulares
    emojis_encontrados = re.findall(r'(?::\)|:\(|:D|;\)|:P|xD|:-\)|:-\(|\(y\)|\(n\)|<3|\\m/|:-O|:O|:-\||:\||:\*|>:\(|\^\^|:-\])', texto)
    palabras_encontradas = re.findall(r'\b(?<!\()(?!(?:B|C|D|F|G|H|I|J|K|L|M|N|Ñ|P|Q|R|S|T|V|W|X|Z)\b)[\w😊-😐]*[\w😊-😐]+\b', texto, re.IGNORECASE)

    # Contar el número de palabras en español
    palabras_espanol_contadas = sum(1 for palabra in palabras_encontradas if palabra.lower() in palabras_espanol)

    # Mostrar resultados en la interfaz gráfica
    resultado_texto.set("Texto sin emojis:\n" + texto_sin_emojis)
    resultado_palabras.set("Número de palabras en español: " + str(palabras_espanol_contadas))
    resultado_emojis.set("Número de emojis diferentes: " + str(len(set(emojis_encontrados))))

window = ctk.CTk()
window.title("Contador de palabras y emojis")
window.geometry("500x500")
window.bg = "lightblue" # Cambiar el color de fondo

# Crear widgets
label = ctk.CTkLabel(window, text="Ingrese el texto a analizar")
label.font = ("Arial", 16) # Cambiar el tipo y el tamaño de la fuente
label.place(x=50, y=50) # Colocar la etiqueta en una posición específica

text = ctk.CTkTextbox(window, height=10, width=400)
text.borderwidth = 2 # Agregar un borde al cuadro de texto
text.place(x=50, y=100) # Colocar el cuadro de texto en una posición específica

button = ctk.CTkButton(window, text="Analizar", command=contar_palabras_y_emojis)
button.place(x=200, y=250) # Colocar el botón en una posición específica

resultado_texto = ctk.StringVar()
resultado_palabras = ctk.StringVar()
resultado_emojis = ctk.StringVar()

label_resultado_texto = ctk.CTkLabel(window, textvariable=resultado_texto, font=("Arial", 20))
label_resultado_texto.place(x=160, y=350)
label_resultado_texto.justify = "center"

label_resultado_palabras = ctk.CTkLabel(window, textvariable=resultado_palabras, font=("Arial", 20))
label_resultado_palabras.place(x=160, y=400)
label_resultado_palabras.justify = "center"

label_resultado_emojis = ctk.CTkLabel(window, textvariable=resultado_emojis, font=("Arial", 20))
label_resultado_emojis.place(x=160, y=450)
label_resultado_emojis.justify = "center"

window.mainloop()