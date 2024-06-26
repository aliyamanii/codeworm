import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog, Menu, colorchooser
import main as interpreter

class InterpreterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NSC Interpreter")

        # Initialize file path for Save functionality
        self.current_file_path = None

        # Create the menu bar
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New File", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open File", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        self.file_menu.add_command(label="Run", command=self.run_code, accelerator="F5")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit menu
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")

        # Theme menu
        self.theme_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)
        self.theme_menu.add_command(label="Change background", command=self.change_background)

        # Create the frame for text area and line numbers
        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(5, 10))

        # Create the line number area for text area
        self.line_numbers = tk.Text(self.text_frame, width=4, padx=5, takefocus=0, border=0,
                                    background='lightgrey', state='disabled', wrap=tk.NONE)
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Create the text area
        self.text_area = scrolledtext.ScrolledText(self.text_frame, wrap=tk.WORD, undo=True)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Bind events to update line numbers for text area
        self.text_area.bind("<KeyRelease>", self.update_text_line_numbers)
        self.text_area.bind("<MouseWheel>", self.update_text_line_numbers)
        self.text_area.bind("<Button-1>", self.update_text_line_numbers)
        self.text_area.bind("<ButtonRelease-1>", self.update_text_line_numbers)

        # Create the frame for output area and line numbers
        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create the line number area for output area
        self.output_line_numbers = tk.Text(self.output_frame, width=4, padx=5, takefocus=0, border=0,
                                           background='lightgrey', state='disabled', wrap=tk.NONE)
        self.output_line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Create the output area
        self.output_area = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD, height=5, state='disabled')
        self.output_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Bind events to update line numbers for output area
        self.output_area.bind("<MouseWheel>", self.update_output_line_numbers)
        self.output_area.bind("<Button-1>", self.update_output_line_numbers)
        self.output_area.bind("<ButtonRelease-1>", self.update_output_line_numbers)

        # Key bindings for menu accelerators and additional functionality
        self.root.bind_all("<Control-n>", self.new_file)
        self.root.bind_all("<Control-o>", self.open_file)
        self.root.bind_all("<Control-s>", self.save_file)
        self.root.bind_all("<Control-Shift-s>", self.save_as_file)
        self.root.bind_all("<Control-r>", self.run_code)
        self.root.bind_all("<F5>", self.run_code)
        self.root.bind_all("<Control-a>", self.select_all)

        # Update line numbers initially
        self.update_text_line_numbers()
        self.update_output_line_numbers()

    def new_file(self, event=None):
        if self.confirm_discard_changes():
            self.text_area.delete("1.0", tk.END)
            self.current_file_path = None
            self.root.title("NSC Interpreter - Untitled")
            self.update_text_line_numbers()

    def open_file(self, event=None):
        if self.confirm_discard_changes():
            file_path = filedialog.askopenfilename(filetypes=[("NSC Files", "*.nsc"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, 'r') as file:
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.current_file_path = file_path
                self.root.title(f"NSC Interpreter - {file_path}")
                self.update_text_line_numbers()

    def save_file(self, event=None):
        if self.current_file_path:
            try:
                with open(self.current_file_path, 'w') as file:
                    file.write(self.text_area.get("1.0", tk.END))
                messagebox.showinfo("Save", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Save Error", str(e))
        else:
            self.save_as_file()

    def save_as_file(self, event=None):
        file_path = filedialog.asksaveasfilename(defaultextension=".nsc", filetypes=[("NSC Files", "*.nsc"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_area.get("1.0", tk.END))
                self.current_file_path = file_path
                self.root.title(f"NSC Interpreter - {file_path}")
                messagebox.showinfo("Save As", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Save As Error", str(e))

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

            interpreter.nscInterpreter.print_output = self.display_output
            interpreter.nscInterpreter.run_code(code)
            self.update_output_line_numbers()

    def display_output(self, output):
        self.output_area.config(state='normal')
        self.output_area.insert(tk.END, output + "\n")
        self.output_area.config(state='disabled')
        self.update_output_line_numbers()

    def select_all(self, event=None):
        self.text_area.tag_add("sel", "1.0", "end")
        return "break"

    def update_text_line_numbers(self, event=None):
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', tk.END)

        line_count = self.text_area.index('end-1c').split('.')[0]
        line_numbers_string = "\n".join(str(i + 1) for i in range(int(line_count)))
        self.line_numbers.insert('1.0', line_numbers_string + '\n')

        self.line_numbers.config(state='disabled')

    def update_output_line_numbers(self, event=None):
        self.output_line_numbers.config(state='normal')
        self.output_line_numbers.delete('1.0', tk.END)

        line_count = self.output_area.index('end-1c').split('.')[0]
        line_numbers_string = "\n".join(str(i + 1) for i in range(int(line_count)))
        self.output_line_numbers.insert('1.0', line_numbers_string + '\n')

        self.output_line_numbers.config(state='disabled')

    def change_background(self):
         bg_color = colorchooser.askcolor()
         self.text_area.config(bg=bg_color[1])
         self.output_area.config(bg=bg_color[1])
         self.line_numbers.config(bg=bg_color[1])
         self.output_line_numbers.config(bg=bg_color[1])

if __name__ == "__main__":
    root = tk.Tk()
    app = InterpreterApp(root)
    root.mainloop()
