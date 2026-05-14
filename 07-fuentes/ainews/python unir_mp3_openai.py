import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment

class MP3JoinerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unidor de MP3")
        self.root.geometry("700x500")

        self.files = []

        title = tk.Label(
            root,
            text="Unidor de archivos MP3",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)

        instructions = tk.Label(
            root,
            text="Agrega varios MP3, ordénalos y exporta un solo archivo.",
            font=("Arial", 10)
        )
        instructions.pack(pady=5)

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=90, height=18)
        self.listbox.pack(pady=10)

        buttons_frame = tk.Frame(root)
        buttons_frame.pack(pady=5)

        tk.Button(buttons_frame, text="Agregar MP3", width=15, command=self.add_files).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(buttons_frame, text="Quitar seleccionado", width=15, command=self.remove_selected).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(buttons_frame, text="Subir", width=15, command=self.move_up).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(buttons_frame, text="Bajar", width=15, command=self.move_down).grid(row=0, column=3, padx=5, pady=5)

        export_frame = tk.Frame(root)
        export_frame.pack(pady=15)

        tk.Label(export_frame, text="Nombre de salida:").grid(row=0, column=0, padx=5)
        self.output_name = tk.Entry(export_frame, width=30)
        self.output_name.insert(0, "mezcla_final.mp3")
        self.output_name.grid(row=0, column=1, padx=5)

        tk.Button(root, text="Unir y exportar", width=20, height=2, command=self.export_joined).pack(pady=10)

    def add_files(self):
        selected_files = filedialog.askopenfilenames(
            title="Selecciona archivos MP3",
            filetypes=[("Archivos MP3", "*.mp3")]
        )

        for file in selected_files:
            if file not in self.files:
                self.files.append(file)
                self.listbox.insert(tk.END, os.path.basename(file))

    def remove_selected(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            return

        index = selected_index[0]
        self.listbox.delete(index)
        del self.files[index]

    def move_up(self):
        selected_index = self.listbox.curselection()
        if not selected_index or selected_index[0] == 0:
            return

        index = selected_index[0]
        self.files[index - 1], self.files[index] = self.files[index], self.files[index - 1]
        self.refresh_listbox()
        self.listbox.select_set(index - 1)

    def move_down(self):
        selected_index = self.listbox.curselection()
        if not selected_index or selected_index[0] == len(self.files) - 1:
            return

        index = selected_index[0]
        self.files[index + 1], self.files[index] = self.files[index], self.files[index + 1]
        self.refresh_listbox()
        self.listbox.select_set(index + 1)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for file in self.files:
            self.listbox.insert(tk.END, os.path.basename(file))

    def export_joined(self):
        if not self.files:
            messagebox.showwarning("Aviso", "Primero agrega al menos un archivo MP3.")
            return

        output_filename = self.output_name.get().strip()
        if not output_filename:
            messagebox.showwarning("Aviso", "Escribe un nombre de salida.")
            return

        if not output_filename.lower().endswith(".mp3"):
            output_filename += ".mp3"

        save_path = filedialog.asksaveasfilename(
            title="Guardar archivo final",
            defaultextension=".mp3",
            initialfile=output_filename,
            filetypes=[("Archivo MP3", "*.mp3")]
        )

        if not save_path:
            return

        try:
            final_audio = AudioSegment.empty()

            for file in self.files:
                audio = AudioSegment.from_mp3(file)
                final_audio += audio

            final_audio.export(save_path, format="mp3")
            messagebox.showinfo("Éxito", f"Archivo creado correctamente:\\n{save_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un problema:\\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MP3JoinerApp(root)
    root.mainloop()