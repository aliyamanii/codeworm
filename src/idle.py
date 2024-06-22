import tkinter as tk
from tkinter import scrolledtext, messagebox
import src.interpreter.interpreter as interpreter

class InterpreterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NSC Interpreter")

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=20, width=50)
        self.text_area.pack(padx=10, pady=10)

        self.run_button = tk.Button(self.root, text="Run", command=self.run_code)
        self.run_button.pack(pady=5)

        self.output_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=10, width=50, state='disabled')
        self.output_area.pack(padx=10, pady=10)

    def run_code(self):
        code = self.text_area.get("1.0", tk.END).strip()
        if code:
            self.output_area.config(state='normal')
            self.output_area.delete("1.0", tk.END)
            self.output_area.config(state='disabled')

            # Replace the print_output method in the interpreter to capture output in the GUI
            interpreter.nscInterpreter.print_output = self.display_output
            interpreter.run_code(code)

    def display_output(self, output):
        self.output_area.config(state='normal')
        self.output_area.insert(tk.END, output + "\n")
        self.output_area.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = InterpreterApp(root)
    root.mainloop()
