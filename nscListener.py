# Generated from nsc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .nscParser import nscParser
else:
    from nscParser import nscParser

# This class defines a complete listener for a parse tree produced by nscParser.
class nscListener(ParseTreeListener):

    # Enter a parse tree produced by nscParser#program.
    def enterProgram(self, ctx:nscParser.ProgramContext):
        pass

    # Exit a parse tree produced by nscParser#program.
    def exitProgram(self, ctx:nscParser.ProgramContext):
        pass


    # Enter a parse tree produced by nscParser#statements.
    def enterStatements(self, ctx:nscParser.StatementsContext):
        pass

    # Exit a parse tree produced by nscParser#statements.
    def exitStatements(self, ctx:nscParser.StatementsContext):
        pass


    # Enter a parse tree produced by nscParser#statement.
    def enterStatement(self, ctx:nscParser.StatementContext):
        pass

    # Exit a parse tree produced by nscParser#statement.
    def exitStatement(self, ctx:nscParser.StatementContext):
        pass


    # Enter a parse tree produced by nscParser#expr.
    def enterExpr(self, ctx:nscParser.ExprContext):
        pass

    # Exit a parse tree produced by nscParser#expr.
    def exitExpr(self, ctx:nscParser.ExprContext):
        pass


    # Enter a parse tree produced by nscParser#binop.
    def enterBinop(self, ctx:nscParser.BinopContext):
        pass

    # Exit a parse tree produced by nscParser#binop.
    def exitBinop(self, ctx:nscParser.BinopContext):
        pass



del nscParser