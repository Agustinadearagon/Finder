import tkinter as tk
from tkinter import filedialog
import pandas as pd
from tkinter import messagebox
import os

def seleccionar_archivo():
    global input_files
    input_files = filedialog.askopenfilenames(filetypes=[
        ("CSV files", "*.csv"),
        ("Excel files", "*.xls *.xlsx"),
        ("JSON files", "*.json")
    ])
    if input_files:
        status_label.config(text=f"Archivos seleccionados: {', '.join(input_files)}")
    else:
        status_label.config(text="Ningún archivo seleccionado")

def convertir_a_txt():
    if not input_files:
        status_label.config(text="Selecciona archivos primero")
        return

    for input_file in input_files:
        try:
            output_folder = os.path.dirname(input_file)
            output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + '.txt')
            if input_file.endswith(".csv"):
                df = pd.read_csv(input_file)
            elif input_file.endswith((".xls", ".xlsx")):
                df = pd.read_excel(input_file)
            elif input_file.endswith(".json"):
                with open(input_file, 'r') as archivo_json:
                    data = archivo_json.read()

                with open(output_file, 'w') as archivo_txt:
                    archivo_txt.write(data)

                print(f'Se ha convertido el archivo JSON en {output_file}')
            else:
                messagebox.showerror("Error", f"Formato de archivo no compatible: {input_file}")
                return

            df.to_csv(output_file, sep=';', index=False)
            status_label.config(text=f"Conversión exitosa. Se ha creado {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la conversión: {e}")

ventana = tk.Tk()
ventana.title("Conversión de CSV/Excel/JSON a TXT")
ventana.geometry("800x400")

seleccionar_archivo_button = tk.Button(ventana, text="Seleccionar Archivos", command=seleccionar_archivo, width=20, height=2)
convertir_a_txt_button = tk.Button(ventana, text="Convertir a TXT", command=convertir_a_txt, width=20, height=2)
status_label = tk.Label(ventana, text="")

seleccionar_archivo_button.pack(pady=20)
convertir_a_txt_button.pack()
status_label.pack(pady=20)

input_files = None

ventana.mainloop()
