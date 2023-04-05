# QR maker
import tkinter as tk
from tkinter import filedialog

import qrcode


class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        self.label_url = tk.Label(master, text="Введите ссылку:")
        self.label_url.grid(row=0, column=0)

        self.entry_url = tk.Entry(master, width=40)
        self.entry_url.grid(row=0, column=1)

        self.button_generate = tk.Button(master, text="Создать", command=self.generate_qr)
        self.button_generate.grid(row=1, column=1)

        self.label_qr = tk.Label(master, text="QR код")
        self.label_qr.grid(row=2, column=0)

        self.canvas_qr = tk.Canvas(master, width=500, height=400)
        self.canvas_qr.grid(row=3, column=0, columnspan=2)

        self.button_save = tk.Button(master, text="Сохранить", command=self.save_qr)
        self.button_save.grid(row=4, column=1)

    def generate_qr(self):
        url = self.entry_url.get()
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        self.qr_image = img
        self.qr_image.save("qr_code.jpg")  # Сохраняем изображение как файл
        self.photo = tk.PhotoImage(file="qr_code.jpg")  # Используем имя файла при создании объекта PhotoImage
        self.canvas_qr.delete("all")  # Очищаем canvas от предыдущей картинки
        self.canvas_qr.create_image(
            self.canvas_qr.winfo_width() / 2, self.canvas_qr.winfo_height() / 2, image=self.photo
        )  # Рисуем новую картинку по центру

    def save_qr(self):
        filename = filedialog.asksaveasfilename(
            initialdir="./",
            title="Select file",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")],
        )
        self.qr_image.save(filename)


root = tk.Tk()
my_gui = QRCodeGenerator(root)
root.mainloop()
