# Generated from YAPLGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLGrammarParser import YAPLGrammarParser
else:
    from YAPLGrammarParser import YAPLGrammarParser

# This class defines a complete listener for a parse tree produced by YAPLGrammarParser.
class YAPLGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLGrammarParser#program.
    def enterProgram(self, ctx:YAPLGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#program.
    def exitProgram(self, ctx:YAPLGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#classDeclaration.
    def enterClassDeclaration(self, ctx:YAPLGrammarParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#classDeclaration.
    def exitClassDeclaration(self, ctx:YAPLGrammarParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#className.
    def enterClassName(self, ctx:YAPLGrammarParser.ClassNameContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#className.
    def exitClassName(self, ctx:YAPLGrammarParser.ClassNameContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#classNameParent.
    def enterClassNameParent(self, ctx:YAPLGrammarParser.ClassNameParentContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#classNameParent.
    def exitClassNameParent(self, ctx:YAPLGrammarParser.ClassNameParentContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#methodName.
    def enterMethodName(self, ctx:YAPLGrammarParser.MethodNameContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#methodName.
    def exitMethodName(self, ctx:YAPLGrammarParser.MethodNameContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#type.
    def enterType(self, ctx:YAPLGrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#type.
    def exitType(self, ctx:YAPLGrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#variable.
    def enterVariable(self, ctx:YAPLGrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#variable.
    def exitVariable(self, ctx:YAPLGrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#arithmeticOperator.
    def enterArithmeticOperator(self, ctx:YAPLGrammarParser.ArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#arithmeticOperator.
    def exitArithmeticOperator(self, ctx:YAPLGrammarParser.ArithmeticOperatorContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#boolOperator.
    def enterBoolOperator(self, ctx:YAPLGrammarParser.BoolOperatorContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#boolOperator.
    def exitBoolOperator(self, ctx:YAPLGrammarParser.BoolOperatorContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#parameterCall.
    def enterParameterCall(self, ctx:YAPLGrammarParser.ParameterCallContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#parameterCall.
    def exitParameterCall(self, ctx:YAPLGrammarParser.ParameterCallContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:YAPLGrammarParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:YAPLGrammarParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#boolDeclaration.
    def enterBoolDeclaration(self, ctx:YAPLGrammarParser.BoolDeclarationContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#boolDeclaration.
    def exitBoolDeclaration(self, ctx:YAPLGrammarParser.BoolDeclarationContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#expression.
    def enterExpression(self, ctx:YAPLGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#expression.
    def exitExpression(self, ctx:YAPLGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:YAPLGrammarParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:YAPLGrammarParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#boolExpression.
    def enterBoolExpression(self, ctx:YAPLGrammarParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#boolExpression.
    def exitBoolExpression(self, ctx:YAPLGrammarParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#assignExpression.
    def enterAssignExpression(self, ctx:YAPLGrammarParser.AssignExpressionContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#assignExpression.
    def exitAssignExpression(self, ctx:YAPLGrammarParser.AssignExpressionContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#uniqueMethod.
    def enterUniqueMethod(self, ctx:YAPLGrammarParser.UniqueMethodContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#uniqueMethod.
    def exitUniqueMethod(self, ctx:YAPLGrammarParser.UniqueMethodContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#declaration.
    def enterDeclaration(self, ctx:YAPLGrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#declaration.
    def exitDeclaration(self, ctx:YAPLGrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#newVarDeclaration.
    def enterNewVarDeclaration(self, ctx:YAPLGrammarParser.NewVarDeclarationContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#newVarDeclaration.
    def exitNewVarDeclaration(self, ctx:YAPLGrammarParser.NewVarDeclarationContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#varDeclaration.
    def enterVarDeclaration(self, ctx:YAPLGrammarParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#varDeclaration.
    def exitVarDeclaration(self, ctx:YAPLGrammarParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#letDeclaration.
    def enterLetDeclaration(self, ctx:YAPLGrammarParser.LetDeclarationContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#letDeclaration.
    def exitLetDeclaration(self, ctx:YAPLGrammarParser.LetDeclarationContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#methodCall.
    def enterMethodCall(self, ctx:YAPLGrammarParser.MethodCallContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#methodCall.
    def exitMethodCall(self, ctx:YAPLGrammarParser.MethodCallContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#statement.
    def enterStatement(self, ctx:YAPLGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#statement.
    def exitStatement(self, ctx:YAPLGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#assignStatement.
    def enterAssignStatement(self, ctx:YAPLGrammarParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#assignStatement.
    def exitAssignStatement(self, ctx:YAPLGrammarParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#ifStatement.
    def enterIfStatement(self, ctx:YAPLGrammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#ifStatement.
    def exitIfStatement(self, ctx:YAPLGrammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#statementList.
    def enterStatementList(self, ctx:YAPLGrammarParser.StatementListContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#statementList.
    def exitStatementList(self, ctx:YAPLGrammarParser.StatementListContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#letExpression.
    def enterLetExpression(self, ctx:YAPLGrammarParser.LetExpressionContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#letExpression.
    def exitLetExpression(self, ctx:YAPLGrammarParser.LetExpressionContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#defineStatements.
    def enterDefineStatements(self, ctx:YAPLGrammarParser.DefineStatementsContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#defineStatements.
    def exitDefineStatements(self, ctx:YAPLGrammarParser.DefineStatementsContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#formalParameter.
    def enterFormalParameter(self, ctx:YAPLGrammarParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#formalParameter.
    def exitFormalParameter(self, ctx:YAPLGrammarParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#parameterList.
    def enterParameterList(self, ctx:YAPLGrammarParser.ParameterListContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#parameterList.
    def exitParameterList(self, ctx:YAPLGrammarParser.ParameterListContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:YAPLGrammarParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:YAPLGrammarParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by YAPLGrammarParser#feature.
    def enterFeature(self, ctx:YAPLGrammarParser.FeatureContext):
        pass

    # Exit a parse tree produced by YAPLGrammarParser#feature.
    def exitFeature(self, ctx:YAPLGrammarParser.FeatureContext):
        pass


