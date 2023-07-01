import os
import tkinter as tk
from tkinter import filedialog, messagebox


class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer")
        self.root.geometry("500x300")

        self.file_listbox = tk.Listbox(self.root, width=60, height=15)
        self.file_listbox.pack(pady=10)

        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack()

        self.btn_open = tk.Button(self.btn_frame, text="Open", command=self.open_file)
        self.btn_open.grid(row=0, column=0, padx=5)

        self.btn_delete = tk.Button(self.btn_frame, text="Delete", command=self.delete_file)
        self.btn_delete.grid(row=0, column=1, padx=5)

        self.btn_refresh = tk.Button(self.btn_frame, text="Refresh", command=self.refresh_files)
        self.btn_refresh.grid(row=0, column=2, padx=5)

        self.refresh_files()

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            os.startfile(file_path)

    def delete_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            file_name = self.file_listbox.get(selected_index)
            confirm = messagebox.askyesno("Confirmation", f"Are you sure you want to delete {file_name}?")
            if confirm:
                file_path = os.path.join(os.getcwd(), file_name)
                os.remove(file_path)
                self.refresh_files()

    def refresh_files(self):
        self.file_listbox.delete(0, tk.END)
        files = os.listdir()
        for file_name in files:
            self.file_listbox.insert(tk.END, file_name)


root = tk.Tk()
app = FileExplorer(root)
root.mainloop()
