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


    # Enter a parse tree produced by nscParser#term.
    def enterTerm(self, ctx:nscParser.TermContext):
        pass

    # Exit a parse tree produced by nscParser#term.
    def exitTerm(self, ctx:nscParser.TermContext):
        pass


    # Enter a parse tree produced by nscParser#factor.
    def enterFactor(self, ctx:nscParser.FactorContext):
        pass

    # Exit a parse tree produced by nscParser#factor.
    def exitFactor(self, ctx:nscParser.FactorContext):
        pass


    # Enter a parse tree produced by nscParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:nscParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by nscParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:nscParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by nscParser#Identifier.
    def enterIdentifier(self, ctx:nscParser.IdentifierContext):
        pass

    # Exit a parse tree produced by nscParser#Identifier.
    def exitIdentifier(self, ctx:nscParser.IdentifierContext):
        pass


    # Enter a parse tree produced by nscParser#Number.
    def enterNumber(self, ctx:nscParser.NumberContext):
        pass

    # Exit a parse tree produced by nscParser#Number.
    def exitNumber(self, ctx:nscParser.NumberContext):
        pass


    # Enter a parse tree produced by nscParser#assign_statement.
    def enterAssign_statement(self, ctx:nscParser.Assign_statementContext):
        pass

    # Exit a parse tree produced by nscParser#assign_statement.
    def exitAssign_statement(self, ctx:nscParser.Assign_statementContext):
        pass


    # Enter a parse tree produced by nscParser#begin_end_statement.
    def enterBegin_end_statement(self, ctx:nscParser.Begin_end_statementContext):
        pass

    # Exit a parse tree produced by nscParser#begin_end_statement.
    def exitBegin_end_statement(self, ctx:nscParser.Begin_end_statementContext):
        pass


    # Enter a parse tree produced by nscParser#print_simple.
    def enterPrint_simple(self, ctx:nscParser.Print_simpleContext):
        pass

    # Exit a parse tree produced by nscParser#print_simple.
    def exitPrint_simple(self, ctx:nscParser.Print_simpleContext):
        pass


    # Enter a parse tree produced by nscParser#print_literal.
    def enterPrint_literal(self, ctx:nscParser.Print_literalContext):
        pass

    # Exit a parse tree produced by nscParser#print_literal.
    def exitPrint_literal(self, ctx:nscParser.Print_literalContext):
        pass


    # Enter a parse tree produced by nscParser#if_else_statement.
    def enterIf_else_statement(self, ctx:nscParser.If_else_statementContext):
        pass

    # Exit a parse tree produced by nscParser#if_else_statement.
    def exitIf_else_statement(self, ctx:nscParser.If_else_statementContext):
        pass


    # Enter a parse tree produced by nscParser#while_statement.
    def enterWhile_statement(self, ctx:nscParser.While_statementContext):
        pass

    # Exit a parse tree produced by nscParser#while_statement.
    def exitWhile_statement(self, ctx:nscParser.While_statementContext):
        pass


    # Enter a parse tree produced by nscParser#for_statement.
    def enterFor_statement(self, ctx:nscParser.For_statementContext):
        pass

    # Exit a parse tree produced by nscParser#for_statement.
    def exitFor_statement(self, ctx:nscParser.For_statementContext):
        pass


    # Enter a parse tree produced by nscParser#loop_statement.
    def enterLoop_statement(self, ctx:nscParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by nscParser#loop_statement.
    def exitLoop_statement(self, ctx:nscParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by nscParser#cumopr.
    def enterCumopr(self, ctx:nscParser.CumoprContext):
        pass

    # Exit a parse tree produced by nscParser#cumopr.
    def exitCumopr(self, ctx:nscParser.CumoprContext):
        pass


    # Enter a parse tree produced by nscParser#multiplicative.
    def enterMultiplicative(self, ctx:nscParser.MultiplicativeContext):
        pass

    # Exit a parse tree produced by nscParser#multiplicative.
    def exitMultiplicative(self, ctx:nscParser.MultiplicativeContext):
        pass


    # Enter a parse tree produced by nscParser#additive.
    def enterAdditive(self, ctx:nscParser.AdditiveContext):
        pass

    # Exit a parse tree produced by nscParser#additive.
    def exitAdditive(self, ctx:nscParser.AdditiveContext):
        pass



del nscParser