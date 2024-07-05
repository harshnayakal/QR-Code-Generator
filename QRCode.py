import pyqrcode
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def generate_qr_code(data):
    qr = pyqrcode.create(data)
    qr_image_path = "qr_code.png"
    qr.png(qr_image_path, scale=10)
    return qr_image_path

def show_qr_code_image():
    qr_image_path = generate_qr_code(entry.get())
    img = Image.open(qr_image_path)
    img = img.resize((300, 300), Image.LANCZOS)
    qr_image = ImageTk.PhotoImage(img)
    
    qr_label.config(image=qr_image)
    qr_label.image = qr_image
    qr_label.pack(pady=20)

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x700")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 16), background="#f0f0f0", foreground="#333")
style.configure('TButton', font=('Helvetica', 14), padding=10, background="#007acc", foreground="#000000")
style.configure('TEntry', font=('Helvetica', 14), padding=10)

title_label = ttk.Label(root, text="QR Code Generator", font=("Helvetica", 20, "bold"), background="#f0f0f0", foreground="#007acc")
title_label.pack(pady=20)

input_label = ttk.Label(root, text="Enter data for QR code:", background="#f0f0f0", foreground="#333")
input_label.pack(pady=10)

entry = ttk.Entry(root, width=50)
entry.pack(pady=10)

generate_button = ttk.Button(root, text="Generate QR Code", command=show_qr_code_image, style="TButton")
generate_button.pack(pady=20)

qr_label = ttk.Label(root, background="#f0f0f0")
qr_label.pack(pady=20)

for widget in root.winfo_children():
    widget.pack_configure(padx=20, pady=10)

style.map('TButton',
          background=[('active', '#005f99')],
          foreground=[('active', '#000000')])

root.mainloop()
