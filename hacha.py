import tkinter as tk
from tkinter import filedialog
import os

# Variables globales
archivo_seleccionado = None  # Almacenará la ruta del archivo seleccionado

# Función que se ejecuta cuando se presiona el botón "Elegir Archivo"
def elegir_archivo():
    global archivo_seleccionado
    archivo_seleccionado = filedialog.askopenfilename()

# Función que se ejecuta cuando se presiona el botón "Cortar"
def cortar_archivo():
    if archivo_seleccionado is None:
        resultado_label.config(text="Primero elija un archivo.")
        return

    try:
        num_partes = int(partes_entry.get())
        if num_partes < 1 or num_partes > 100:
            resultado_label.config(text="Ingrese un número entre 1 y 100")
            return

        # Obtiene el tamaño del archivo
        tamaño_archivo = os.path.getsize(archivo_seleccionado)
        nombre_base, extension = os.path.splitext(os.path.basename(archivo_seleccionado))

        # Calcula el tamaño de cada parte
        tamaño_parte = tamaño_archivo // num_partes

        # Divide el archivo en partes
        with open(archivo_seleccionado, 'rb') as archivo:
            for i in range(num_partes):
                datos = archivo.read(tamaño_parte)
                nombre_archivo = f"{nombre_base}_{i + 1}{extension}"
                ruta_destino = os.path.join(os.path.dirname(archivo_seleccionado), nombre_archivo)
                with open(ruta_destino, 'wb') as parte:
                    parte.write(datos)

        resultado_label.config(text=f"Archivo dividido en {num_partes} partes y guardado en la misma carpeta")
    except ValueError:
        resultado_label.config(text="Ingrese un número válido")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Dividir Archivo")
ventana.geometry("600x300")  # Tamaño de la ventana

# Crear botón "Elegir Archivo"
elegir_archivo_button = tk.Button(ventana, text="Elegir Archivo", command=elegir_archivo)
elegir_archivo_button.pack()

# Campo para ingresar el número de partes
partes_label = tk.Label(ventana, text="Número de Partes (1-100):")
partes_label.pack()
partes_entry = tk.Entry(ventana)
partes_entry.pack()

# Botón para cortar el archivo
cortar_button = tk.Button(ventana, text="Cortar", command=cortar_archivo)
cortar_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()
