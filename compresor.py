import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pikepdf

def compress_pdf(input_path, output_path):
    # Abrir el archivo PDF original
    with pikepdf.open(input_path) as pdf:
        # Guardar el PDF comprimido
        pdf.save(output_path, compress_streams=True)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, file_path)

def compress():
    input_path = entry_input.get()
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    if input_path and output_path:
        try:
            compress_pdf(input_path, output_path)
            messagebox.showinfo("Éxito", "Archivo PDF comprimido exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor selecciona un archivo de entrada y elige un destino.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Compresor de PDF")

# Entrada de archivo
frame = tk.Frame(root)
frame.pack(pady=20)

entry_input = tk.Entry(frame, width=50)
entry_input.pack(side=tk.LEFT)

btn_browse = tk.Button(frame, text="Seleccionar PDF", command=select_file)
btn_browse.pack(side=tk.LEFT)

# Botón para comprimir
btn_compress = tk.Button(root, text="Comprimir PDF", command=compress)
btn_compress.pack(pady=20)

root.mainloop()
