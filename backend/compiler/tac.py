from YAPLGrammarVisitor import YAPLGrammarVisitor
from YAPLGrammarParser import YAPLGrammarParser
from backend.compiler.YAPLGrammarParser import YAPLGrammarParser

class TACGeneratorVisitor:
    def __init__(self):
        self.tac = ""
        self.temp_counter = 0
        self.label_counter = 0

    def visitProgram(self, ctx:YAPLGrammarParser.ProgramContext):
        for cls in ctx.classDeclaration():
            self.visitClassDeclaration(cls)

    def visitClassDeclaration(self, ctx:YAPLGrammarParser.ClassDeclarationContext):
        ptac = ""
        classname = ctx.className.getText()
        if ctx.classNameParent != None:
            classname += ":" + ctx.classNameParent.getText()
        ptac += "class " + classname + ":\n beginClass;\n"
        for feature in ctx.feature():
            ptac += self.visitFeature(feature)
        ptac += "endClass;\n"
        self.tac += ptac
    
    def visitFeature(self, ctx:YAPLGrammarParser.FeatureContext):
        if ctx.methodDeclaration() != None:
            return self.visitMethodDeclaration(ctx.methodDeclaration())
        elif ctx.statementList() != None:
            return self.visitStatementList(ctx.statementList())
        
    def visitMethodDeclaration(self, ctx:YAPLGrammarParser.MethodDeclarationContext):
        ptac = ""
        methodname = ctx.methodName.getText()
        ptac += "method " + methodname + ":\n beginMethod;\n"
        if ctx.parameterList() != None:
            ptac += self.visitParameterList(ctx.parameterList())
        
        for stmnt in ctx.defineStatements():
            ptac += self.visitDefineStatements(stmnt)

        ptac += "endMethod;\n"
        return ptac

    def visitParameterList(self, ctx:YAPLGrammarParser.ParameterListContext):
        ptac = ""
        for param in ctx.formalParameter():
            ptac += self.visitFormalParameter(param)
        return ptac
    
    def visitFormalParameter(self, ctx:YAPLGrammarParser.FormalParameterContext):
        ptac = ""
        ptac += self.visitDeclaration(ctx.declaration())
        return ptac
    
    def visitDeclaration(self, ctx: YAPLGrammarParser.DeclarationContext):
        ptac = ""
        ptac += "var " + ctx.IDENTIFIER().getText() + ";\n"
        return ptac
    
    def visitDefineStatements(self, ctx:YAPLGrammarParser.DefineStatementsContext):
        ptac = ""
        for stmnt in ctx.statementList():
            ptac += self.visitStatementList(stmnt)
        return ptac
    
    def visitStatementList(self, ctx:YAPLGrammarParser.StatementListContext):
        ptac = ""
        if ctx.statement != None:
            ptac += self.visitStatement(ctx.state)
        elif ctx.ifStatement() != None:
            ptac += self.visitIfStatement(ctx.ifStatement())
        elif ctx.letExpression() != None:
            ptac += self.visitLetExpression(ctx.letExpression())
        return ptac
    
    def visitStatement(self, ctx:YAPLGrammarParser.StatementContext):
        if ctx.assignStatement() != None:
            return self.visitAssignStatement(ctx.assignStatement())
        elif ctx.expression() != None:
            return self.visitExpression(ctx.expression())
        
    def visitAssignStatement(self, ctx:YAPLGrammarParser.AssignStatementContext):
        if ctx.newVarDeclaration() != None:
            return self.visitNewVarDeclaration(ctx.newVarDeclaration())
        elif ctx.varDeclaration() != None:
            return self.visitVarDeclaration(ctx.varDeclaration())
        
    def visitNewVarDeclaration(self, ctx:YAPLGrammarParser.NewVarDeclarationContext):
        ptac = ""
        ptac += self.visitDeclaration(ctx.declaration())
        if ctx.assignExpression() != None:
            ptac += self.visitAssignExpression(ctx.assignExpression())
        return ptac
    
    def visitAssignExpression(self, ctx:YAPLGrammarParser.AssignExpressionContext):
        ptac = ""
        ptac += self.visitExpression(ctx.expression())
        return ptac
    
    def visitExpression(self, ctx:YAPLGrammarParser.ExpressionContext):
        if ctx.primaryExpression():
            return self.visitPrimaryExpression(ctx.primaryExpression())
        elif ctx.arithmeticExpression():
            return self.visitArithmeticExpression(ctx.arithmeticExpression())
        elif ctx.methodCall():
            return self.visitMethodCall(ctx.methodCall())
        elif ctx.uniqueMethod():
            return self.visitUniqueMethod(ctx.uniqueMethod())

    def visitPrimaryExpression(self, ctx:YAPLGrammarParser.PrimaryExpressionContext):
        if ctx.boolDeclaration():
            return self.visitBoolDeclaration(ctx.boolDeclaration())
        elif ctx.INT_LITERAL():
            return ctx.INT_LITERAL().getText()
        elif  ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.NEW():
            return self.visitNew(ctx.new())
        elif ctx.methodName():
            return self.visitMethodCall(ctx.methodCall())

    def visitArithmeticExpression(self, ctx:YAPLGrammarParser.ArithmeticExpressionContext):
        ptac = ""
        if ctx.primaryExpression(0).methodName():
            self.temp_counter += 1
            tempvarFunc = "t" + str(self.temp_counter)
            ptac += tempvarFunc + " = " + self.visitMethodCall(ctx.primaryExpression(0).methodCall())
        if ctx.primaryExpression(1).methodName():
            self.temp_counter += 1
            tempvarFunc = "t" + str(self.temp_counter)
            ptac += tempvarFunc + " = " + self.visitMethodCall(ctx.primaryExpression(0).methodCall())
        leftOperand = ctx.primaryExpression(0).getText()
        rightOperand = ctx.primaryExpression(1).getText()
        operator = ctx.arithmeticOperator().getText()
        temp = "t" + str(self.temp_counter)
        self.temp_counter += 1
        ptac += temp + " = " + leftOperand + " " + operator + " " + rightOperand + ";\n"
        return ptac
    
    def visitMethodCall(self, ctx):
        ptac = ""
        ptac += "goto L" + str(self.label_counter) + ";\n"
        ptac += "L" + str(self.label_counter) + ":\n"
        self.label_counter += 1
        for param in ctx.parameterCall():
            ptac += f"PushParams {self.visitParameterCall(param)};\n"
        ptac += "call " + ctx.methodName().getText() + ";\n"
        return ptac
    
    def visitParameterCall(self, ctx:YAPLGrammarParser.ParameterCallContext):
        for exp in ctx.expression():
            return self.visitExpression(exp)
    
    def visitUniqueMethod(self, ctx:YAPLGrammarParser.UniqueMethodContext):
        methodname = ctx.methodName().getText()
        ptac = ""
        ptac += f"call {methodname};\n"
        return ptac
    
    def visitVarDeclaration(self, ctx:YAPLGrammarParser.VarDeclarationContext):
        ptac = ""
        ptac += self.visitDeclaration(ctx.declaration())
        if ctx.assignExpression() != None:
            ptac += self.visitAssignExpression(ctx.assignExpression())
        return ptac
    
    def visitIfStatement(self, ctx:YAPLGrammarParser.IfStatementContext):
        ptac = ""
        label = f"L{self.label_counter}"
        self.label_counter += 1

        if ctx.boolExpression(0) != None:
            conditional = self.visitBoolExpression(ctx.boolExpression(0))
        
        ptac += f"ifz {conditional} goto {label};\n"
        ptac = f"{label}:\n"
        ptac += self.visitStatement(ctx.statement())

        if ctx.IF() != None:
            ptac += self.visitIfStatement(ctx.ifStatement())
        elif ctx.ELSE() != None:
            ptac += self.visitElseStatement(ctx.elseStatement())
        return ptac

    def visitElseStatement(self, ctx:YAPLGrammarParser.ElseStatementContext):
        ptac = ""
        ptac += self.visitStatement(ctx.statement())
        return ptac

    def visitBoolExpression(self, ctx:YAPLGrammarParser.BoolExpressionContext):
        leftOperand = ctx.primaryExpression(0).getText()
        rightOperand = ctx.primaryExpression(1).getText()
        operator = ctx.boolOperator().getText()
        temp = "t" + str(self.temp_counter)
        self.temp_counter += 1
        ptac = ""
        ptac += temp + " = " + leftOperand + " " + operator + " " + rightOperand + ";\n"
        return ptac
    
    def visitBoolDeclaration(self, ctx:YAPLGrammarParser.BoolDeclarationContext):
        ptac = ""
        ptac += ctx.getText()
        return ptac
    
    def visitArithmeticOperator(self, ctx:YAPLGrammarParser.ArithmeticOperatorContext):
        return ctx.getText()
    
    def visitBoolOperator(self, ctx:YAPLGrammarParser.BoolOperatorContext):
        return ctx.getText()
    
    def visitLetExpression(self, ctx:YAPLGrammarParser.LetExpressionContext):
        ptac = ""
        ptac += self.visitDeclaration(ctx.declaration())
        if ctx.statement() != None:
            ptac += self.visitStatement(ctx.state)
        return ptac