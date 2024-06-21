# expr_visitor.py

from nscParser import nscParser
from nscVisitor import nscVisitor


class NscVisitorImpl:
    def visitUnaryMinus(self, ctx):
        return -self.visit(ctx.expr())

    def visitFactor(self, ctx: nscParser.ExponentContext):
        exponents = ctx.exponent()

        values = list(map(self.visitExponent, exponents))
        while len(values) > 1:
            a = values.pop()
            b = values.pop()
            values.append(b ** a)
        return values[0]

    def visitTerm(self, ctx: nscParser.MultiplicativeContext):
        factors = ctx.factor()
        left = self.visitFactor(factors[0])
        if len(factors) < 2:
            return left
        
        for d, c in enumerate(ctx.multiplicative()):
            right = self.visitFactor(factors[d+1])
            if c.getText() == '*':
                left *= right
            else:
                left /= right
        return left

    def visitParenthesizedExpression(self, ctx: nscParser.ParenthesizedExpressionContext):
        return self.visit(ctx.expr())

    def visitNumber(self, ctx: nscParser.NumberContext):
        return float(ctx.NUMBER().getText())


    def visitExponent(self, ctx):
        if isinstance(ctx, nscParser.NumberContext):
            return self.visitNumber(ctx)
        elif isinstance(ctx, nscParser.IdentifierContext):
            return self.visitIdentifier(ctx)
        # elif isinstance(ctx, nscParser.UnaryMinusContext):
        #     return self.visitUnaryMinus(ctx)
        elif isinstance(ctx, nscParser.ParenthesizedExpressionContext):
            return self.visitParenthesizedExpression(ctx)

    def visitExpr(self, ctx):
        if ctx is None:
            return 0
        terms = ctx.term()
        left = self.visitTerm(terms[0])
        if len(terms) < 2:
            return left
        # right = self.visitTerm(terms[1])
        for d, c in enumerate(ctx.additive()):
            right = self.visitTerm(terms[d+1])
            if c.getText() == '+':
                left += right
            else:
                left -= right
        return left
