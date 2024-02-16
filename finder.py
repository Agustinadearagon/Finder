import re
import tkinter as tk
from tkinter import filedialog

class ProcesadorArchivo:
    def __init__(self):
        self.nombre_archivo_entrada = None
        self.resultados_temporales = None

    def seleccionar_archivo(self):
        opciones = {'title': 'Seleccionar archivo de entrada'}
        self.nombre_archivo_entrada = filedialog.askopenfilename(**opciones)

    def procesar_y_exportar(self, expresion):
        self.procesar_archivo(expresion)
        self.exportar_resultados()

    def procesar_archivo(self, expresion):
        if self.nombre_archivo_entrada:
            with open(self.nombre_archivo_entrada, 'r', encoding='latin-1') as archivo_entrada:
                lineas = archivo_entrada.readlines()

            patron_personalizado = re.compile(expresion)
            self.resultados_temporales = []

            for linea in lineas:
                elementos_encontrados = re.findall(patron_personalizado, linea)
                if elementos_encontrados:
                    self.resultados_temporales.extend(elementos_encontrados)
                else:
                    self.resultados_temporales.append('\n')

            print('Se han procesado los resultados con la expresión proporcionada.')
            self.exportar_resultados()  # Exportar automáticamente después de procesar

        else:
            self.resultados_temporales = []

    def exportar_resultados(self):
        if self.resultados_temporales is not None and any(result for result in self.resultados_temporales if result != '\n'):
            nombre_archivo_resultados = 'resultados_personalizados.txt'
            with open(nombre_archivo_resultados, 'w') as archivo_resultados:
                archivo_resultados.write('\n'.join(str(result) for result in self.resultados_temporales if result != '\n'))

            print(f'Se han guardado los resultados en {nombre_archivo_resultados}.')
        else:
            print('No hay resultados válidos para exportar.')

    def salir(self):
        root.destroy()

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Procesar Archivo")
root.geometry("600x400")  # Establece el tamaño de la ventana

procesador = ProcesadorArchivo()

# Botón para seleccionar cualquier tipo de archivo
boton_seleccionar = tk.Button(root, text="Seleccionar Archivo", command=procesador.seleccionar_archivo)
boton_seleccionar.pack(pady=10)

# Botón para buscar números de 9 dígitos
boton_9_digitos = tk.Button(root, text="Buscar números de 9 dígitos", command=lambda: procesador.procesar_y_exportar(r'\b\d{9}\b'))
boton_9_digitos.pack(pady=10)

# Botón para buscar números de 5 dígitos seguidos de una letra
boton_5_digitos_letra = tk.Button(root, text="Buscar números de 5 dígitos seguidos de una letra", command=lambda: procesador.procesar_y_exportar(r'\b\d{5}[A-Za-z]\b'))
boton_5_digitos_letra.pack(pady=10)

# Botón para buscar palabras que comienzan con "Hola"
boton_palabras_hola = tk.Button(root, text="Buscar palabras que comienzan con 'Hola'", command=lambda: procesador.procesar_y_exportar(r'\bHola\w*\b'))
boton_palabras_hola.pack(pady=10)

# Botón para exportar resultados
boton_exportar_resultados = tk.Button(root, text="Exportar Resultados", command=procesador.exportar_resultados)
boton_exportar_resultados.pack(pady=10)

# Botón para salir
boton_salir = tk.Button(root, text="Salir", command=procesador.salir)
boton_salir.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()

