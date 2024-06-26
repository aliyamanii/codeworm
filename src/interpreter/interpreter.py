# interpreter.py

from antlr4 import *
from grammar.nscLexer import nscLexer
from grammar.nscParser import nscParser
from grammar.nscVisitor import nscVisitor
from .expr_visitor import NscVisitorImpl
import logging

logging.basicConfig(level=logging.DEBUG)

class nscInterpreter(NscVisitorImpl, nscVisitor):
    def __init__(self):
        self.variables = {}

    # Visit method for identifiers
    def visitIdentifier(self, ctx):
        if ctx.ID():
            return self.variables.get(ctx.ID().getText(), None)
        raise TypeError("Not Implemented Error")

    # Visit method for the program (entry point)
    def visitProgram(self, ctx):
        return self.visitStatements(ctx.statements())

    # Visit method for a list of statements
    def visitStatements(self, ctx):
        for statement in ctx.statement():
            self.visitStatement(statement)

    # Visit method for a single statement
    def visitStatement(self, ctx):
        # Handle assignment statements
        if c := ctx.assign_statement():
            var_name = c.ID().getText()
            value = self.visitExpr(c.expr())
            self.variables[var_name] = value

        # Handle block statements
        elif c := ctx.begin_end_statement():
            self.visitStatements(c.statements())

        # Handle if-else statements
        elif c := ctx.if_else_statement():
            statements = c.statement()
            if self.visitExpr(c.expr()):
                self.visitStatement(c.statement(0))
            elif len(statements) > 1:
                self.visitStatement(c.statement(1))

        # Handle while loop statements
        elif c := ctx.while_statement():
            while self.visitExpr(c.expr()):
                self.visitStatement(c.statement())

        # Handle for loop statements
        elif c := ctx.for_statement():
            var_name = c.ID().getText()
            start = int(c.NUMBER(0).getText())
            end = int(c.NUMBER(1).getText())
            for i in range(start, end + 1):
                self.variables[var_name] = i
                self.visitStatement(c.statement())

        # Handle custom loop statements
        elif c := ctx.loop_statement():
            var_name = c.ID().getText()
            count = int(c.NUMBER().getText())
            for i in range(1, count + 1):
                self.variables[var_name] = i
                self.visitStatement(c.statement())

        # Handle simple print statements
        elif c := ctx.print_simple():
            output = []
            if c.ID():
                var_name = c.ID().getText()
                if var_name in self.variables:
                    output.append(str(self.variables[var_name]))
                else:
                    output.append("undefined")
            self.print_output(" ".join(output))

        # Handle print statements with literals
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

    # Visit method for IDs (another form)
    def visitID(self, ctx):
        var_name = ctx.getText()
        if var_name in self.variables:
            return self.variables[var_name]
        raise NameError(f"Variable '{var_name}' is not defined")

    # Helper method to convert strings to numbers
    def strToNumber(self, s):
        try:
            return int(s)
        except ValueError:
            return float(s)
        
    # Helper method to print output
    def print_output(self, output):
        print(output)  # Placeholder for GUI output function
    
    # Static method to run the interpreter with given code
    @staticmethod
    def run_code(code):
        input_stream = InputStream(code)
        lexer = nscLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = nscParser(stream)
        tree = parser.program()

        interpreter = nscInterpreter()

        try:
            interpreter.visit(tree)
        except Exception as e:
            logging.error(e.with_traceback())
