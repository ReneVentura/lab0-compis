# Generated from YAPLGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLGrammarParser import YAPLGrammarParser
else:
    from YAPLGrammarParser import YAPLGrammarParser

# This class defines a complete generic visitor for a parse tree produced by YAPLGrammarParser.

class YAPLGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YAPLGrammarParser#program.
    def visitProgram(self, ctx:YAPLGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#classDeclaration.
    def visitClassDeclaration(self, ctx:YAPLGrammarParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#className.
    def visitClassName(self, ctx:YAPLGrammarParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#classNameParent.
    def visitClassNameParent(self, ctx:YAPLGrammarParser.ClassNameParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#methodName.
    def visitMethodName(self, ctx:YAPLGrammarParser.MethodNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#type.
    def visitType(self, ctx:YAPLGrammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#variable.
    def visitVariable(self, ctx:YAPLGrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#arithmeticOperator.
    def visitArithmeticOperator(self, ctx:YAPLGrammarParser.ArithmeticOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#boolOperator.
    def visitBoolOperator(self, ctx:YAPLGrammarParser.BoolOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#parameterCall.
    def visitParameterCall(self, ctx:YAPLGrammarParser.ParameterCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:YAPLGrammarParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#boolDeclaration.
    def visitBoolDeclaration(self, ctx:YAPLGrammarParser.BoolDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#expression.
    def visitExpression(self, ctx:YAPLGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:YAPLGrammarParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#boolExpression.
    def visitBoolExpression(self, ctx:YAPLGrammarParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#assignExpression.
    def visitAssignExpression(self, ctx:YAPLGrammarParser.AssignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#uniqueMethod.
    def visitUniqueMethod(self, ctx:YAPLGrammarParser.UniqueMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#declaration.
    def visitDeclaration(self, ctx:YAPLGrammarParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#newVarDeclaration.
    def visitNewVarDeclaration(self, ctx:YAPLGrammarParser.NewVarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#varDeclaration.
    def visitVarDeclaration(self, ctx:YAPLGrammarParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#letDeclaration.
    def visitLetDeclaration(self, ctx:YAPLGrammarParser.LetDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#methodCall.
    def visitMethodCall(self, ctx:YAPLGrammarParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#statement.
    def visitStatement(self, ctx:YAPLGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#assignStatement.
    def visitAssignStatement(self, ctx:YAPLGrammarParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#ifStatement.
    def visitIfStatement(self, ctx:YAPLGrammarParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#statementList.
    def visitStatementList(self, ctx:YAPLGrammarParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#letExpression.
    def visitLetExpression(self, ctx:YAPLGrammarParser.LetExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#defineStatements.
    def visitDefineStatements(self, ctx:YAPLGrammarParser.DefineStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#formalParameter.
    def visitFormalParameter(self, ctx:YAPLGrammarParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#parameterList.
    def visitParameterList(self, ctx:YAPLGrammarParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:YAPLGrammarParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLGrammarParser#feature.
    def visitFeature(self, ctx:YAPLGrammarParser.FeatureContext):
        return self.visitChildren(ctx)



del YAPLGrammarParser