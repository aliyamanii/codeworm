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


    # Visit a parse tree produced by nscParser#term.
    def visitTerm(self, ctx:nscParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#factor.
    def visitFactor(self, ctx:nscParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:nscParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#Identifier.
    def visitIdentifier(self, ctx:nscParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#Number.
    def visitNumber(self, ctx:nscParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#assign_statement.
    def visitAssign_statement(self, ctx:nscParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#begin_end_statement.
    def visitBegin_end_statement(self, ctx:nscParser.Begin_end_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#print_simple.
    def visitPrint_simple(self, ctx:nscParser.Print_simpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#print_literal.
    def visitPrint_literal(self, ctx:nscParser.Print_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#if_else_statement.
    def visitIf_else_statement(self, ctx:nscParser.If_else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#while_statement.
    def visitWhile_statement(self, ctx:nscParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#for_statement.
    def visitFor_statement(self, ctx:nscParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#loop_statement.
    def visitLoop_statement(self, ctx:nscParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#cumopr.
    def visitCumopr(self, ctx:nscParser.CumoprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#multiplicative.
    def visitMultiplicative(self, ctx:nscParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#additive.
    def visitAdditive(self, ctx:nscParser.AdditiveContext):
        return self.visitChildren(ctx)



del nscParser