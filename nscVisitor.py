# Generated from nsc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .nscParser import nscParser
else:
    from nscParser import nscParser

# This class defines a complete generic visitor for a parse tree produced by nscParser.

class nscVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by nscParser#program.
    def visitProgram(self, ctx:nscParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#statements.
    def visitStatements(self, ctx:nscParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#statement.
    def visitStatement(self, ctx:nscParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#expr.
    def visitExpr(self, ctx:nscParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#binop.
    def visitBinop(self, ctx:nscParser.BinopContext):
        return self.visitChildren(ctx)



del nscParser