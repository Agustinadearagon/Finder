import os
import tkinter as tk
from tkinter import filedialog

def contar_campos(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8', errors='ignore') as file:
            header = file.readline()
            campos = header.strip().split(';')
            return len(campos)
    except Exception as e:
        return 0

def modificar_separador(input_file, output_file, nuevo_separador):
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as file_in, open(output_file, 'w', encoding='utf-8') as file_out:
            for line in file_in:
                nueva_linea = line.replace(',', nuevo_separador)
                file_out.write(nueva_linea)
    except Exception as e:
        print("Ocurrió un error:", str(e))

def eliminar_campos(input_file, output_file, campos_a_eliminar):
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as file_in, open(output_file, 'w', encoding='utf-8') as file_out:
            header = file_in.readline()
            header_campos = header.strip().split(';')
            campos_a_mantener = [campo for i, campo in enumerate(header_campos) if i not in campos_a_eliminar]

            file_out.write(';'.join(campos_a_mantener) + '\n')

            for line in file_in:
                campos = line.strip().split(';')
                nuevos_campos = [campo for i, campo in enumerate(campos) if i not in campos_a_eliminar]
                nueva_linea = ';'.join(nuevos_campos)
                file_out.write(nueva_linea + '\n')

    except Exception as e:
        print("Ocurrió un error:", str(e))

def limpiar_campos(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as file_in, open(output_file, 'w', encoding='utf-8') as file_out:
            header = file_in.readline()
            file_out.write(header)

            for line in file_in:
                campos_vacios = ['' for _ in line.strip().split(';')]
                nueva_linea = ';'.join(campos_vacios)
                file_out.write(nueva_linea + '\n')

    except Exception as e:
        print("Ocurrió un error:", str(e))

def eliminar_campos_dialogo():
    ventana = tk.Tk()
    ventana.title("Eliminar Campos")
    ventana.geometry("600x500")

    def eliminar_campos_seleccionados(archivo_entrada, archivo_salida, campos_a_eliminar):
        eliminar_campos(archivo_entrada, archivo_salida, campos_a_eliminar)

    def modificar_separador_archivo():
        archivo_entrada = archivo_seleccionado.get()
        archivo_modificado = os.path.splitext(archivo_entrada)[0] + "_nuevo_separador.txt"
        nuevo_separador = ';'
        modificar_separador(archivo_entrada, archivo_modificado, nuevo_separador)
        num_campos_modificados = contar_campos(archivo_modificado)
        if num_campos_modificados > 0:
            etiqueta_info.config(text=f"El archivo modificado contiene {num_campos_modificados} campos.")
        else:
            etiqueta_info.config(text="No se pudo obtener la información de los campos del archivo modificado.")
        print(f"Separador modificado con éxito en {archivo_modificado}")

    def procesar_archivo():
        archivo_entrada = archivo_seleccionado.get()
        campos_a_eliminar_str = entry_campos.get()
        if archivo_entrada and campos_a_eliminar_str:
            campos_a_eliminar = [int(campo) - 1 for campo in campos_a_eliminar_str.split(",")]
            archivo_salida = os.path.splitext(archivo_entrada)[0] + "_sin_campos.txt"
            eliminar_campos_seleccionados(archivo_entrada, archivo_salida, campos_a_eliminar)
            print(f"Campos eliminados con éxito en {archivo_salida}")
        else:
            print("Por favor, selecciona un archivo y especifica los campos a eliminar.")

    def limpiar_campos_archivo():
        archivo_entrada = archivo_seleccionado.get()
        archivo_limpiado = os.path.splitext(archivo_entrada)[0] + "_campos_vacios.txt"
        limpiar_campos(archivo_entrada, archivo_limpiado)
        num_campos_limpiados = contar_campos(archivo_limpiado)
        entry_campos.delete(0, 'end')
        if num_campos_limpiados > 0:
            etiqueta_info.config(text=f"El archivo limpiado contiene {num_campos_limpiados} campos.")
        else:
            etiqueta_info.config(text="No se pudo obtener la información de los campos del archivo limpiado.")
        print(f"Campos limpiados con éxito en {archivo_limpiado}")

    def seleccionar_archivo():
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        archivo_seleccionado.set(archivo)
        num_campos = contar_campos(archivo)
        if num_campos > 0:
            etiqueta_info.config(text=f"El archivo seleccionado contiene {num_campos} campos.")
        else:
            etiqueta_info.config(text="No se pudo obtener la información de los campos del archivo.")
        etiqueta_separador.config(text="")

    archivo_seleccionado = tk.StringVar()

    etiqueta_archivo = tk.Label(ventana, text="Selecciona un archivo de texto:")
    etiqueta_archivo.pack()

    boton_seleccionar = tk.Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo)
    boton_seleccionar.pack()

    tk.Label(ventana, textvariable=archivo_seleccionado).pack()

    etiqueta_info = tk.Label(ventana, text="")
    etiqueta_info.pack()

    etiqueta_separador = tk.Label(ventana, text="")
    etiqueta_separador.pack()

    boton_modificar = tk.Button(ventana, text="Modificar Separador a Punto y Coma", command=modificar_separador_archivo)
    boton_modificar.pack()

    boton_procesar = tk.Button(ventana, text="Procesar Archivo", command=procesar_archivo)
    boton_procesar.pack()

    etiqueta_campos = tk.Label(ventana, text="Ingresa los números de los campos a eliminar (separados por comas):")
    etiqueta_campos.pack()

    entry_campos = tk.Entry(ventana)
    entry_campos.pack()

    boton_limpiar = tk.Button(ventana, text="Limpiar Campos", command=limpiar_campos_archivo)
    boton_limpiar.pack()

    ventana.mainloop()

# Llama a la función para mostrar el cuadro de diálogo
eliminar_campos_dialogo()
