import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog, Menu
import main as interpreter  # Assuming main.py exists and contains the necessary interpreter code

class InterpreterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NSC Interpreter")

        # Create the menu bar
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New File", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open File", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Bind shortcuts
        self.root.bind("<Control-n>", lambda event: self.new_file())
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-r>", lambda event: self.run_code())

        # Create the text area
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=20, width=80)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create the run button
        self.run_button = tk.Button(self.root, text="Run", command=self.run_code)
        self.run_button.pack(pady=5)

        # Create the output area
        self.output_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=10, width=80, state='disabled')
        self.output_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def new_file(self):
        if self.confirm_discard_changes():
            self.text_area.delete("1.0", tk.END)

    def open_file(self):
        if self.confirm_discard_changes():
            file_path = filedialog.askopenfilename(filetypes=[("NSC Files", "*.nsc"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, 'r') as file:
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert(tk.END, file.read())

    def confirm_discard_changes(self):
        if self.text_area.get("1.0", tk.END).strip():
            return messagebox.askokcancel("Confirm", "Unsaved changes will be lost. Continue?")
        return True

    def run_code(self, event=None):
        code = self.text_area.get("1.0", tk.END).strip()
        if code:
            self.output_area.config(state='normal')
            self.output_area.delete("1.0", tk.END)
            self.output_area.config(state='disabled')

            # Replace the print_output method in the interpreter to capture output in the GUI
            interpreter.nscInterpreter.print_output = self.display_output
            interpreter.nscInterpreter.run_code(code)

    def display_output(self, output):
        self.output_area.config(state='normal')
        self.output_area.insert(tk.END, output + "\n")
        self.output_area.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = InterpreterApp(root)
    root.mainloop()
