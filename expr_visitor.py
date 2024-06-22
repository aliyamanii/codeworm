# expr_visitor.py

from nscParser import nscParser


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
            opr = c.getText()
            if opr == '*':
                left *= right
            elif opr == '/':
                left /= right
            else:
                left %= right
        return left

    def visitParenthesizedExpression(self, ctx: nscParser.ParenthesizedExpressionContext):
        return self.visit(ctx.expr())

    def visitNumber(self, ctx: nscParser.NumberContext):
        return self.strToNumber(ctx.NUMBER().getText())


    def visitExponent(self, ctx):
        if isinstance(ctx, nscParser.NumberContext):
            return self.visitNumber(ctx)
        elif isinstance(ctx, nscParser.IdentifierContext):
            return self.visitIdentifier(ctx)
        # elif isinstance(ctx, nscParser.UnaryMinusContext):
        #     return self.visitUnaryMinus(ctx)
        elif isinstance(ctx, nscParser.ParenthesizedExpressionContext):
            return self.visitParenthesizedExpression(ctx)

    def getBool(self, left, right, op):
        if op == '<':
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
        
    def visitExpr(self, ctx):
        cumterms = list(map(self.visitCumTerm, ctx.cumTerm()))
        left = cumterms[0]
        if len(cumterms) < 2:
            return left
        for d, c in enumerate(ctx.cumopr()):
            left = self.getBool(left, cumterms[d+1], c.getText())
        return left

    def visitCumTerm(self, ctx):
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
