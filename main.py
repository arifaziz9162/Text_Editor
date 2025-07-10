import tkinter as tk
from tkinter import filedialog, messagebox
import logging

# File handler and stream handler setup
logger = logging.getLogger("Text_Editor_Logger")
logger.setLevel(logging.DEBUG)

if logger.hasHandlers():
    logger.handlers.clear()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)  
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler("text_editor.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

class TextEditoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.root.geometry("800x600")

        self.text = tk.Text(self.root, wrap=tk.WORD, font=("Helvetica", 12))
        self.text.pack(expand=True, fill=tk.BOTH)

        self.create_menu()
        logger.info("Text editor started successfully.")
    
    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

    def new_file(self):
        try:

            self.text.delete(1.0, tk.END)
            logger.info("Created new file successfully.")
        except Exception as e:
            logger.error("Error creating file", exc_info=True)

    def open_file(self):
        try:

            file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])
            if file_path:
                with open(file_path,'r') as file:
                    self.text.delete(1.0, tk.END)
                    self.text.insert(tk.END, file.read())
                    logger.info(f"Opened file: {file_path}")

        except Exception as e:
            logger.error("Error opening file", exc_info=True)
            messagebox.showerror("Error","Failed to open file.")

    def save_file(self):
        try:

            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])
            if file_path:
                with open(file_path,'w') as file:
                    file.write(self.text.get(1.0, tk.END))
                    logger.info(f"Saved file: {file_path}")
                    messagebox.showinfo("Info", "File saved successfully.")

        except Exception as e:
            logger.error("Error saving file", exc_info=True)
            messagebox.showerror("Error","Failed to save file.")

def main():
    try:
        root = tk.Tk()
        app = TextEditoApp(root)
        root.mainloop()
    except Exception as e:
        logger.error("Failed to launch text editor", exc_info=True)

if __name__== "__main__":
    main()