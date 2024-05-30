# Generated from nsc.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,34,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,
        1,1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,70,8,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,81,8,3,1,3,1,3,1,3,1,3,5,3,87,8,3,10,3,12,
        3,90,9,3,1,4,1,4,1,4,0,1,6,5,0,2,4,6,8,0,1,1,0,17,27,101,0,10,1,
        0,0,0,2,12,1,0,0,0,4,69,1,0,0,0,6,80,1,0,0,0,8,91,1,0,0,0,10,11,
        3,2,1,0,11,1,1,0,0,0,12,18,3,4,2,0,13,14,3,2,1,0,14,15,3,4,2,0,15,
        17,1,0,0,0,16,13,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,
        0,19,3,1,0,0,0,20,18,1,0,0,0,21,22,5,1,0,0,22,23,5,16,0,0,23,24,
        3,6,3,0,24,25,5,31,0,0,25,70,1,0,0,0,26,27,5,4,0,0,27,28,3,2,1,0,
        28,29,5,5,0,0,29,70,1,0,0,0,30,31,5,6,0,0,31,32,3,6,3,0,32,33,5,
        7,0,0,33,34,3,4,2,0,34,70,1,0,0,0,35,36,5,6,0,0,36,37,3,6,3,0,37,
        38,5,7,0,0,38,39,3,4,2,0,39,40,5,8,0,0,40,41,3,4,2,0,41,70,1,0,0,
        0,42,43,5,9,0,0,43,44,3,6,3,0,44,45,5,10,0,0,45,46,3,4,2,0,46,70,
        1,0,0,0,47,48,5,11,0,0,48,49,5,1,0,0,49,50,5,12,0,0,50,51,5,2,0,
        0,51,52,5,13,0,0,52,53,5,2,0,0,53,54,5,10,0,0,54,70,3,4,2,0,55,56,
        5,14,0,0,56,57,5,1,0,0,57,58,5,32,0,0,58,59,5,2,0,0,59,60,5,10,0,
        0,60,70,3,4,2,0,61,62,5,15,0,0,62,63,5,1,0,0,63,70,5,31,0,0,64,65,
        5,15,0,0,65,66,5,3,0,0,66,67,5,33,0,0,67,68,5,1,0,0,68,70,5,31,0,
        0,69,21,1,0,0,0,69,26,1,0,0,0,69,30,1,0,0,0,69,35,1,0,0,0,69,42,
        1,0,0,0,69,47,1,0,0,0,69,55,1,0,0,0,69,61,1,0,0,0,69,64,1,0,0,0,
        70,5,1,0,0,0,71,72,6,3,-1,0,72,73,5,28,0,0,73,81,3,6,3,4,74,75,5,
        29,0,0,75,76,3,6,3,0,76,77,5,30,0,0,77,81,1,0,0,0,78,81,5,1,0,0,
        79,81,5,2,0,0,80,71,1,0,0,0,80,74,1,0,0,0,80,78,1,0,0,0,80,79,1,
        0,0,0,81,88,1,0,0,0,82,83,10,5,0,0,83,84,3,8,4,0,84,85,3,6,3,6,85,
        87,1,0,0,0,86,82,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,
        0,89,7,1,0,0,0,90,88,1,0,0,0,91,92,7,0,0,0,92,9,1,0,0,0,4,18,69,
        80,88
    ]

class nscParser ( Parser ):

    grammarFileName = "nsc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'begin'", "'end'", "'if'", "'then'", "'else'", "'while'", 
                     "'do'", "'for'", "'of'", "'to'", "'loop'", "'print'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'<='", 
                     "'>='", "'=='", "'!='", "'^'", "'!'", "'('", "')'", 
                     "';'", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "NUMBER", "STRINGLITERAL", 
                      "BEGIN", "END", "IF", "THEN", "ELSE", "WHILE", "DO", 
                      "FOR", "OF", "TO", "LOOP", "PRINT", "EQ", "PLUS", 
                      "MINUS", "MULT", "DIV", "LT", "GT", "LE", "GE", "EQEQ", 
                      "NEQ", "POW", "NOT", "LPAR", "RPAR", "SEMI", "COLON", 
                      "COMMA", "WS" ]

    RULE_program = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_expr = 3
    RULE_binop = 4

    ruleNames =  [ "program", "statements", "statement", "expr", "binop" ]

    EOF = Token.EOF
    IDENTIFIER=1
    NUMBER=2
    STRINGLITERAL=3
    BEGIN=4
    END=5
    IF=6
    THEN=7
    ELSE=8
    WHILE=9
    DO=10
    FOR=11
    OF=12
    TO=13
    LOOP=14
    PRINT=15
    EQ=16
    PLUS=17
    MINUS=18
    MULT=19
    DIV=20
    LT=21
    GT=22
    LE=23
    GE=24
    EQEQ=25
    NEQ=26
    POW=27
    NOT=28
    LPAR=29
    RPAR=30
    SEMI=31
    COLON=32
    COMMA=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(nscParser.StatementsContext,0)


        def getRuleIndex(self):
            return nscParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = nscParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.StatementContext)
            else:
                return self.getTypedRuleContext(nscParser.StatementContext,i)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.StatementsContext)
            else:
                return self.getTypedRuleContext(nscParser.StatementsContext,i)


        def getRuleIndex(self):
            return nscParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = nscParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.statement()
            self.state = 18
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 13
                    self.statements()
                    self.state = 14
                    self.statement() 
                self.state = 20
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(nscParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(nscParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(nscParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(nscParser.SEMI, 0)

        def BEGIN(self):
            return self.getToken(nscParser.BEGIN, 0)

        def statements(self):
            return self.getTypedRuleContext(nscParser.StatementsContext,0)


        def END(self):
            return self.getToken(nscParser.END, 0)

        def IF(self):
            return self.getToken(nscParser.IF, 0)

        def THEN(self):
            return self.getToken(nscParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.StatementContext)
            else:
                return self.getTypedRuleContext(nscParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(nscParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(nscParser.WHILE, 0)

        def DO(self):
            return self.getToken(nscParser.DO, 0)

        def FOR(self):
            return self.getToken(nscParser.FOR, 0)

        def OF(self):
            return self.getToken(nscParser.OF, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(nscParser.NUMBER)
            else:
                return self.getToken(nscParser.NUMBER, i)

        def TO(self):
            return self.getToken(nscParser.TO, 0)

        def LOOP(self):
            return self.getToken(nscParser.LOOP, 0)

        def COLON(self):
            return self.getToken(nscParser.COLON, 0)

        def PRINT(self):
            return self.getToken(nscParser.PRINT, 0)

        def STRINGLITERAL(self):
            return self.getToken(nscParser.STRINGLITERAL, 0)

        def COMMA(self):
            return self.getToken(nscParser.COMMA, 0)

        def getRuleIndex(self):
            return nscParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = nscParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(nscParser.IDENTIFIER)
                self.state = 22
                self.match(nscParser.EQ)
                self.state = 23
                self.expr(0)
                self.state = 24
                self.match(nscParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(nscParser.BEGIN)
                self.state = 27
                self.statements()
                self.state = 28
                self.match(nscParser.END)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(nscParser.IF)
                self.state = 31
                self.expr(0)
                self.state = 32
                self.match(nscParser.THEN)
                self.state = 33
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(nscParser.IF)
                self.state = 36
                self.expr(0)
                self.state = 37
                self.match(nscParser.THEN)
                self.state = 38
                self.statement()
                self.state = 39
                self.match(nscParser.ELSE)
                self.state = 40
                self.statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.match(nscParser.WHILE)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(nscParser.DO)
                self.state = 45
                self.statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.match(nscParser.FOR)
                self.state = 48
                self.match(nscParser.IDENTIFIER)
                self.state = 49
                self.match(nscParser.OF)
                self.state = 50
                self.match(nscParser.NUMBER)
                self.state = 51
                self.match(nscParser.TO)
                self.state = 52
                self.match(nscParser.NUMBER)
                self.state = 53
                self.match(nscParser.DO)
                self.state = 54
                self.statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 55
                self.match(nscParser.LOOP)
                self.state = 56
                self.match(nscParser.IDENTIFIER)
                self.state = 57
                self.match(nscParser.COLON)
                self.state = 58
                self.match(nscParser.NUMBER)
                self.state = 59
                self.match(nscParser.DO)
                self.state = 60
                self.statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 61
                self.match(nscParser.PRINT)
                self.state = 62
                self.match(nscParser.IDENTIFIER)
                self.state = 63
                self.match(nscParser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 64
                self.match(nscParser.PRINT)
                self.state = 65
                self.match(nscParser.STRINGLITERAL)
                self.state = 66
                self.match(nscParser.COMMA)
                self.state = 67
                self.match(nscParser.IDENTIFIER)
                self.state = 68
                self.match(nscParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(nscParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.ExprContext)
            else:
                return self.getTypedRuleContext(nscParser.ExprContext,i)


        def LPAR(self):
            return self.getToken(nscParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(nscParser.RPAR, 0)

        def IDENTIFIER(self):
            return self.getToken(nscParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(nscParser.NUMBER, 0)

        def binop(self):
            return self.getTypedRuleContext(nscParser.BinopContext,0)


        def getRuleIndex(self):
            return nscParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = nscParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 72
                self.match(nscParser.NOT)
                self.state = 73
                self.expr(4)
                pass
            elif token in [29]:
                self.state = 74
                self.match(nscParser.LPAR)
                self.state = 75
                self.expr(0)
                self.state = 76
                self.match(nscParser.RPAR)
                pass
            elif token in [1]:
                self.state = 78
                self.match(nscParser.IDENTIFIER)
                pass
            elif token in [2]:
                self.state = 79
                self.match(nscParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = nscParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 82
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 83
                    self.binop()
                    self.state = 84
                    self.expr(6) 
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BinopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(nscParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(nscParser.MINUS, 0)

        def MULT(self):
            return self.getToken(nscParser.MULT, 0)

        def DIV(self):
            return self.getToken(nscParser.DIV, 0)

        def LT(self):
            return self.getToken(nscParser.LT, 0)

        def GT(self):
            return self.getToken(nscParser.GT, 0)

        def LE(self):
            return self.getToken(nscParser.LE, 0)

        def GE(self):
            return self.getToken(nscParser.GE, 0)

        def EQEQ(self):
            return self.getToken(nscParser.EQEQ, 0)

        def NEQ(self):
            return self.getToken(nscParser.NEQ, 0)

        def POW(self):
            return self.getToken(nscParser.POW, 0)

        def getRuleIndex(self):
            return nscParser.RULE_binop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinop" ):
                listener.enterBinop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinop" ):
                listener.exitBinop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinop" ):
                return visitor.visitBinop(self)
            else:
                return visitor.visitChildren(self)




    def binop(self):

        localctx = nscParser.BinopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_binop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 268304384) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




