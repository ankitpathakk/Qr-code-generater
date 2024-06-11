import qrcode
import tkinter as ankit
from tkinter import filedialog

class QRCodeGenerator:
    def __init__(self, ankit_master):
        self.ankit_master = ankit_master
        ankit_master.title("QR Code Generator")

        # Create label and entry widgets 🏫🍀

        self.ankit_label = ankit.Label(ankit_master, text="Enter text or URL:")
        self.ankit_label.pack()
        self.ankit_entry = ankit.Entry(ankit_master, width=50)
        self.ankit_entry.pack()

        # Create buttons 😕✅

        self.ankit_generate_button = ankit.Button(ankit_master, text="Generate QR Code", command=self.ankit_generate_qr_code)
        self.ankit_generate_button.pack()
        self.ankit_save_button = ankit.Button(ankit_master, text="Save QR Code", command=self.ankit_save_qr_code, state=ankit.DISABLED)
        self.ankit_save_button.pack()

        # Variable process 🧐😵

        self.ankit_qr_code = None

    def ankit_generate_qr_code(self):
     
        # Generate QR Code 🚀🚁

        ankit_data = self.ankit_entry.get()
        if ankit_data:
            self.ankit_qr_code = qrcode.make(ankit_data)
            self.ankit_save_button.config(state=ankit.NORMAL)
        else:
            self.ankit_qr_code = None
            self.ankit_save_button.config(state=ankit.DISABLED)

    def ankit_save_qr_code(self):
       
        # Save QR Code as image file 📁🗄

        ankit_file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if ankit_file_path and self.ankit_qr_code:
            self.ankit_qr_code.save(ankit_file_path)

ankit_root = ankit.Tk()
ankit_qrcode_generator = QRCodeGenerator(ankit_root)
ankit_root.mainloop()
