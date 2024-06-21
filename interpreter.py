from antlr4 import *
from nscLexer import nscLexer
from nscParser import nscParser
from nscVisitor import nscVisitor
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from expr_visitor import NscVisitorImpl

class nscInterpreter(NscVisitorImpl, nscVisitor):
    def __init__(self):
        self.variables = {}
        self.output_widget = None

    def visitIdentifier(self, ctx: nscParser.IdentifierContext):
        if ctx.ID():
            if (x := self.variables.get(ctx.ID().getText(), None)) is not None:
                return x
        raise TypeError("Not Implemented Error")

    def visitProgram(self, ctx: nscParser.ProgramContext):
        return self.visitStatements(ctx.statements())

    def visitStatements(self, ctx: nscParser.StatementsContext):
        for statement in ctx.statement():
            self.visitStatement(statement)

    def visitStatement(self, ctx: nscParser.StatementContext):
        # breakpoint()
        if c := ctx.assign_statement():
            var_name = c.ID().getText()
            value = self.visitExpr(c.expr())
            self.variables[var_name] = value

        elif c := ctx.begin_end_statement():
            self.visitStatements(c.statements())

        elif c := ctx.if_else_statement():
            statements = c.statement()
            if self.visitExpr(c.expr()):
                self.visitStatement(c.statement(0))
            elif len(statements) > 1:
                self.visitStatement(c.statement(1))
                
        elif c := ctx.while_statement():
            while self.visitExpr(c.expr()):
                self.visitStatement(c.statement())

        elif c := ctx.for_statement():
            var_name = c.ID().getText()
            start = int(c.NUMBER(0).getText())
            end = int(c.NUMBER(1).getText())
            for i in range(start, end + 1):
                self.variables[var_name] = i
                self.visitStatement(c.statement())

        elif c := ctx.loop_statement():
            var_name = c.ID().getText()
            count = int(c.NUMBER().getText())
            for i in range(1, count + 1):
                self.variables[var_name] = i
                self.visitStatement(c.statement())

        elif c := ctx.print_simple():
            output = []
            # if c.STRINGLITERAL():
            #     output.append(c.STRINGLITERAL().getText()[1:-1])
            if c.ID():
                var_name = c.ID().getText()
                if var_name in self.variables:
                    output.append(str(self.variables[var_name]))
                else:
                    output.append("undefined")
            self.print_output(" ".join(output))
        
        elif c := ctx.print_literal():
            output = []
            if c.STRING():
                output.append(c.STRING().getText()[1:-1])
            if c.ID():
                var_name = c.ID().getText()
                if var_name in self.variables:
                    output.append(str(self.variables[var_name]))
                else:
                    output.append("undefined")

            self.print_output(" ".join(output))

    def visitID(self, ctx):
        var_name = ctx.getText()
        if var_name in self.variables:
            return self.variables[var_name]
        return NameError('not found')


    def strToNumber(self, s):
        try:
            return int(s)
        except ValueError:
            return float(s)
        
    def visitExpra(self, ctx: nscParser.ExprContext):
        breakpoint()
        if ctx.NUMBER():
            return self.strToNumber(ctx.NUMBER().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise Exception(f"Variable '{var_name}' is not defined")
        if ctx.MultiplicationOrDivision():
            breakpoint()
        elif ctx.cumopr():
            left = self.visitExpr(ctx.expr(0))
            right = self.visitExpr(ctx.expr(1))
            op = ctx.binop().getText()
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '^':
                return left ** right
            elif op == '<':
                return left < right
            elif op == '>':
               return left > right
            elif op == '<=':
                return left <= right
            elif op == '>=':
                return left >= right
            elif op == '==':
                return left == right
            elif op == '!=':
                return left != right
        elif ctx.NOT():
            return not self.visitExpr(ctx.expr(0))
        elif ctx.LPAR():
            return self.visitExpr(ctx.expr(0))
        return None

    def print_output(self, output):
        print(output)
        self.output_widget.config(state='normal')
        self.output_widget.insert(tk.END, output + "\n")
        self.output_widget.see(tk.END)
        self.output_widget.config(state='disabled')

def run_code():
    gui_output.config(state='normal')
    gui_output.delete(1.0, tk.END)
    gui_output.config(state='disabled')

    code = gui_code.get("1.0", tk.END)
    input_stream = InputStream(code)
    lexer = nscLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = nscParser(stream)
    tree = parser.program()

    interpreter = nscInterpreter()
    interpreter.output_widget = gui_output
    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    try:
        interpreter.visit(tree)
        print(interpreter.variables)
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("NSC Interpreter")

frame = tk.Frame(app)
frame.pack(fill=tk.BOTH, expand=True)

gui_code = scrolledtext.ScrolledText(frame, wrap=tk.WORD, height=20)
gui_code.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

run_button = tk.Button(app, text="RUN", command=run_code)
run_button.pack(pady=10)

gui_output = scrolledtext.ScrolledText(app, wrap=tk.WORD, height=10, state='disabled')
gui_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

app.mainloop()

