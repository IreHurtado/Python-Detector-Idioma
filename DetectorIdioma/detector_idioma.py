
# Importamos modulos
from langdetect import detect
from langdetect import DetectorFactory
from tkinter import *
from tkinter import font, filedialog, PhotoImage

DetectorFactory.seed = 0

# Definimos nuestras funciones
def detectar():
    sentence = input_entry.get()
    try:
        idioma = detect(sentence)
        if idioma == "en":
            label2.config(text="Idioma del texto ingresado: Inglés", font=("Arial", 18), fg="green")
        elif idioma == "es":
            label2.config(text="Idioma del texto ingresado: Español", font=("Arial", 18), fg="green")
        elif idioma == "it":
            label2.config(text="Idioma del texto ingresado: Italiano", font=("Arial", 18), fg="green")
        else:
            label2.config(text=f"Idioma del texto ingresado: {idioma}", font=("Arial", 18), fg="green")
        print(idioma)
    except Exception as e:
        label2.config(text="No se pudo detectar el idioma", font=("Arial", 18), fg="red")
        print(f"Error al detectar el idioma: {e}")

# Creamos la ventana
root = Tk()
root.title("Detector de lenguajes en Python")

# Agregamos los botones e insertamos comandos
imagen = PhotoImage(file="detector.png")
imagen_head = Label(root, image=imagen)
imagen_head.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

label1 = Label(root, text="Ingrese el texto para detectar el idioma:", font=("Arial", 18))
label1.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

input_entry = Entry(root, width=40, font=("Arial", 24))
input_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

detectar_button = Button(root, text="Detectar", command=detectar)
detectar_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

label2 = Label(root, text="Idioma del texto ingresado a definir", font=("Arial", 18), fg="black")
label2.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

mainloop()