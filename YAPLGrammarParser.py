# Generated from YAPLGrammar.g4 by ANTLR 4.13.0
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
        4,1,37,220,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,4,0,54,
        8,0,11,0,12,0,55,1,1,1,1,1,1,1,1,3,1,62,8,1,1,1,1,1,5,1,66,8,1,10,
        1,12,1,69,9,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,
        4,83,8,4,1,5,1,5,1,6,1,6,1,6,5,6,90,8,6,10,6,12,6,93,9,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,104,8,7,1,7,1,7,3,7,108,8,7,1,8,
        1,8,1,8,3,8,113,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,12,3,12,127,8,12,1,12,1,12,1,12,1,12,1,13,1,13,3,13,135,8,
        13,1,13,3,13,138,8,13,1,14,1,14,1,14,3,14,143,8,14,1,15,1,15,1,15,
        1,15,1,16,1,16,1,16,1,16,1,17,1,17,3,17,155,8,17,1,18,1,18,3,18,
        159,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        5,19,172,8,19,10,19,12,19,175,9,19,1,19,1,19,3,19,179,8,19,1,20,
        1,20,3,20,183,8,20,1,21,1,21,4,21,187,8,21,11,21,12,21,188,1,21,
        1,21,1,22,1,22,1,23,1,23,1,23,5,23,198,8,23,10,23,12,23,201,9,23,
        1,24,1,24,1,24,3,24,206,8,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,25,1,25,3,25,218,8,25,1,25,0,0,26,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,2,1,0,20,23,1,
        0,17,19,222,0,53,1,0,0,0,2,57,1,0,0,0,4,73,1,0,0,0,6,75,1,0,0,0,
        8,82,1,0,0,0,10,84,1,0,0,0,12,86,1,0,0,0,14,107,1,0,0,0,16,112,1,
        0,0,0,18,114,1,0,0,0,20,118,1,0,0,0,22,122,1,0,0,0,24,126,1,0,0,
        0,26,132,1,0,0,0,28,139,1,0,0,0,30,144,1,0,0,0,32,148,1,0,0,0,34,
        154,1,0,0,0,36,158,1,0,0,0,38,160,1,0,0,0,40,182,1,0,0,0,42,184,
        1,0,0,0,44,192,1,0,0,0,46,194,1,0,0,0,48,202,1,0,0,0,50,217,1,0,
        0,0,52,54,3,2,1,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,
        1,0,0,0,56,1,1,0,0,0,57,58,5,1,0,0,58,61,3,4,2,0,59,60,5,2,0,0,60,
        62,3,4,2,0,61,59,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,67,5,5,0,
        0,64,66,3,50,25,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,
        1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,5,6,0,0,71,72,5,8,0,0,
        72,3,1,0,0,0,73,74,5,32,0,0,74,5,1,0,0,0,75,76,5,32,0,0,76,7,1,0,
        0,0,77,83,5,10,0,0,78,83,5,12,0,0,79,83,5,11,0,0,80,83,3,4,2,0,81,
        83,5,13,0,0,82,77,1,0,0,0,82,78,1,0,0,0,82,79,1,0,0,0,82,80,1,0,
        0,0,82,81,1,0,0,0,83,9,1,0,0,0,84,85,5,28,0,0,85,11,1,0,0,0,86,91,
        3,16,8,0,87,88,5,25,0,0,88,90,3,16,8,0,89,87,1,0,0,0,90,93,1,0,0,
        0,91,89,1,0,0,0,91,92,1,0,0,0,92,13,1,0,0,0,93,91,1,0,0,0,94,108,
        5,33,0,0,95,108,5,34,0,0,96,108,5,31,0,0,97,108,5,32,0,0,98,99,5,
        24,0,0,99,108,3,4,2,0,100,101,3,6,3,0,101,103,5,3,0,0,102,104,3,
        12,6,0,103,102,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,106,5,
        4,0,0,106,108,1,0,0,0,107,94,1,0,0,0,107,95,1,0,0,0,107,96,1,0,0,
        0,107,97,1,0,0,0,107,98,1,0,0,0,107,100,1,0,0,0,108,15,1,0,0,0,109,
        113,3,14,7,0,110,113,3,18,9,0,111,113,3,32,16,0,112,109,1,0,0,0,
        112,110,1,0,0,0,112,111,1,0,0,0,113,17,1,0,0,0,114,115,3,14,7,0,
        115,116,7,0,0,0,116,117,3,14,7,0,117,19,1,0,0,0,118,119,3,14,7,0,
        119,120,7,1,0,0,120,121,3,14,7,0,121,21,1,0,0,0,122,123,5,9,0,0,
        123,124,3,16,8,0,124,23,1,0,0,0,125,127,5,28,0,0,126,125,1,0,0,0,
        126,127,1,0,0,0,127,128,1,0,0,0,128,129,5,32,0,0,129,130,5,7,0,0,
        130,131,3,8,4,0,131,25,1,0,0,0,132,134,3,24,12,0,133,135,3,22,11,
        0,134,133,1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,138,5,8,0,
        0,137,136,1,0,0,0,137,138,1,0,0,0,138,27,1,0,0,0,139,140,5,32,0,
        0,140,142,3,22,11,0,141,143,5,8,0,0,142,141,1,0,0,0,142,143,1,0,
        0,0,143,29,1,0,0,0,144,145,5,28,0,0,145,146,3,24,12,0,146,147,5,
        26,0,0,147,31,1,0,0,0,148,149,5,32,0,0,149,150,5,27,0,0,150,151,
        3,14,7,0,151,33,1,0,0,0,152,155,3,36,18,0,153,155,3,16,8,0,154,152,
        1,0,0,0,154,153,1,0,0,0,155,35,1,0,0,0,156,159,3,26,13,0,157,159,
        3,28,14,0,158,156,1,0,0,0,158,157,1,0,0,0,159,37,1,0,0,0,160,161,
        3,30,15,0,161,162,5,14,0,0,162,163,3,20,10,0,163,164,5,15,0,0,164,
        173,3,34,17,0,165,166,5,16,0,0,166,167,5,14,0,0,167,168,3,20,10,
        0,168,169,5,15,0,0,169,170,3,34,17,0,170,172,1,0,0,0,171,165,1,0,
        0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,178,1,0,
        0,0,175,173,1,0,0,0,176,177,5,16,0,0,177,179,3,34,17,0,178,176,1,
        0,0,0,178,179,1,0,0,0,179,39,1,0,0,0,180,183,3,34,17,0,181,183,3,
        38,19,0,182,180,1,0,0,0,182,181,1,0,0,0,183,41,1,0,0,0,184,186,5,
        5,0,0,185,187,3,40,20,0,186,185,1,0,0,0,187,188,1,0,0,0,188,186,
        1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,191,5,6,0,0,191,43,1,
        0,0,0,192,193,3,24,12,0,193,45,1,0,0,0,194,199,3,44,22,0,195,196,
        5,25,0,0,196,198,3,44,22,0,197,195,1,0,0,0,198,201,1,0,0,0,199,197,
        1,0,0,0,199,200,1,0,0,0,200,47,1,0,0,0,201,199,1,0,0,0,202,203,3,
        6,3,0,203,205,5,3,0,0,204,206,3,46,23,0,205,204,1,0,0,0,205,206,
        1,0,0,0,206,207,1,0,0,0,207,208,5,4,0,0,208,209,5,7,0,0,209,210,
        3,8,4,0,210,211,5,5,0,0,211,212,3,42,21,0,212,213,5,6,0,0,213,214,
        5,8,0,0,214,49,1,0,0,0,215,218,3,40,20,0,216,218,3,48,24,0,217,215,
        1,0,0,0,217,216,1,0,0,0,218,51,1,0,0,0,21,55,61,67,82,91,103,107,
        112,126,134,137,142,154,158,173,178,182,188,199,205,217
    ]

class YAPLGrammarParser ( Parser ):

    grammarFileName = "YAPLGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'inherits'", "'('", "')'", 
                     "'{'", "'}'", "':'", "';'", "'<-'", "'Int'", "'Bool'", 
                     "'String'", "'self'", "'if'", "'then'", "'else'", "'<'", 
                     "'>'", "'='", "'-'", "'+'", "'*'", "'/'", "'new'", 
                     "','", "'in'", "'.'", "'let'", "'out'", "'_'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "INHERITS", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "COLON", "SEMICOLON", "ASSIGN", 
                      "INT", "BOOL", "STRING", "SELF", "IF", "THEN", "ELSE", 
                      "LESS_THAN", "GREAT_THAN", "EQUALS", "MINUS", "PLUS", 
                      "MULT", "DIV", "NEW", "COMMA", "IN", "DOT", "LET", 
                      "OUT", "UNDERSCORE", "BOOL_LITERAL", "IDENTIFIER", 
                      "INT_LITERAL", "STRING_LITERAL", "WS", "COMMENT", 
                      "ERROR" ]

    RULE_program = 0
    RULE_classDeclaration = 1
    RULE_className = 2
    RULE_methodName = 3
    RULE_type = 4
    RULE_variable = 5
    RULE_parameterCall = 6
    RULE_primaryExpression = 7
    RULE_expression = 8
    RULE_arithmeticExpression = 9
    RULE_boolExpression = 10
    RULE_assignExpression = 11
    RULE_declaration = 12
    RULE_newVarDeclaration = 13
    RULE_varDeclaration = 14
    RULE_letDeclaration = 15
    RULE_methodCall = 16
    RULE_statement = 17
    RULE_assignStatement = 18
    RULE_ifStatement = 19
    RULE_statementList = 20
    RULE_defineStatements = 21
    RULE_formalParameter = 22
    RULE_parameterList = 23
    RULE_methodDeclaration = 24
    RULE_feature = 25

    ruleNames =  [ "program", "classDeclaration", "className", "methodName", 
                   "type", "variable", "parameterCall", "primaryExpression", 
                   "expression", "arithmeticExpression", "boolExpression", 
                   "assignExpression", "declaration", "newVarDeclaration", 
                   "varDeclaration", "letDeclaration", "methodCall", "statement", 
                   "assignStatement", "ifStatement", "statementList", "defineStatements", 
                   "formalParameter", "parameterList", "methodDeclaration", 
                   "feature" ]

    EOF = Token.EOF
    CLASS=1
    INHERITS=2
    LPAREN=3
    RPAREN=4
    LBRACE=5
    RBRACE=6
    COLON=7
    SEMICOLON=8
    ASSIGN=9
    INT=10
    BOOL=11
    STRING=12
    SELF=13
    IF=14
    THEN=15
    ELSE=16
    LESS_THAN=17
    GREAT_THAN=18
    EQUALS=19
    MINUS=20
    PLUS=21
    MULT=22
    DIV=23
    NEW=24
    COMMA=25
    IN=26
    DOT=27
    LET=28
    OUT=29
    UNDERSCORE=30
    BOOL_LITERAL=31
    IDENTIFIER=32
    INT_LITERAL=33
    STRING_LITERAL=34
    WS=35
    COMMENT=36
    ERROR=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLGrammarParser.ClassDeclarationContext)
            else:
                return self.getTypedRuleContext(YAPLGrammarParser.ClassDeclarationContext,i)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_program

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

        localctx = YAPLGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self.classDeclaration()
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(YAPLGrammarParser.CLASS, 0)

        def className(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLGrammarParser.ClassNameContext)
            else:
                return self.getTypedRuleContext(YAPLGrammarParser.ClassNameContext,i)


        def LBRACE(self):
            return self.getToken(YAPLGrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(YAPLGrammarParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(YAPLGrammarParser.SEMICOLON, 0)

        def INHERITS(self):
            return self.getToken(YAPLGrammarParser.INHERITS, 0)

        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLGrammarParser.FeatureContext)
            else:
                return self.getTypedRuleContext(YAPLGrammarParser.FeatureContext,i)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = YAPLGrammarParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(YAPLGrammarParser.CLASS)
            self.state = 58
            self.className()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 59
                self.match(YAPLGrammarParser.INHERITS)
                self.state = 60
                self.className()


            self.state = 63
            self.match(YAPLGrammarParser.LBRACE)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32497467392) != 0):
                self.state = 64
                self.feature()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(YAPLGrammarParser.RBRACE)
            self.state = 71
            self.match(YAPLGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(YAPLGrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_className

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassName" ):
                listener.enterClassName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassName" ):
                listener.exitClassName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassName" ):
                return visitor.visitClassName(self)
            else:
                return visitor.visitChildren(self)




    def className(self):

        localctx = YAPLGrammarParser.ClassNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_className)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(YAPLGrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(YAPLGrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_methodName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodName" ):
                listener.enterMethodName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodName" ):
                listener.exitMethodName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodName" ):
                return visitor.visitMethodName(self)
            else:
                return visitor.visitChildren(self)




    def methodName(self):

        localctx = YAPLGrammarParser.MethodNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_methodName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(YAPLGrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(YAPLGrammarParser.INT, 0)

        def STRING(self):
            return self.getToken(YAPLGrammarParser.STRING, 0)

        def BOOL(self):
            return self.getToken(YAPLGrammarParser.BOOL, 0)

        def className(self):
            return self.getTypedRuleContext(YAPLGrammarParser.ClassNameContext,0)


        def SELF(self):
            return self.getToken(YAPLGrammarParser.SELF, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = YAPLGrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(YAPLGrammarParser.INT)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(YAPLGrammarParser.STRING)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.match(YAPLGrammarParser.BOOL)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                self.className()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 81
                self.match(YAPLGrammarParser.SELF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(YAPLGrammarParser.LET, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = YAPLGrammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(YAPLGrammarParser.LET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(YAPLGrammarParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.COMMA)
            else:
                return self.getToken(YAPLGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_parameterCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterCall" ):
                listener.enterParameterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterCall" ):
                listener.exitParameterCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterCall" ):
                return visitor.visitParameterCall(self)
            else:
                return visitor.visitChildren(self)




    def parameterCall(self):

        localctx = YAPLGrammarParser.ParameterCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameterCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.expression()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 87
                self.match(YAPLGrammarParser.COMMA)
                self.state = 88
                self.expression()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(YAPLGrammarParser.INT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(YAPLGrammarParser.STRING_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(YAPLGrammarParser.BOOL_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(YAPLGrammarParser.IDENTIFIER, 0)

        def NEW(self):
            return self.getToken(YAPLGrammarParser.NEW, 0)

        def className(self):
            return self.getTypedRuleContext(YAPLGrammarParser.ClassNameContext,0)


        def methodName(self):
            return self.getTypedRuleContext(YAPLGrammarParser.MethodNameContext,0)


        def LPAREN(self):
            return self.getToken(YAPLGrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(YAPLGrammarParser.RPAREN, 0)

        def parameterCall(self):
            return self.getTypedRuleContext(YAPLGrammarParser.ParameterCallContext,0)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = YAPLGrammarParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(YAPLGrammarParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(YAPLGrammarParser.STRING_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.match(YAPLGrammarParser.BOOL_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.match(YAPLGrammarParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 98
                self.match(YAPLGrammarParser.NEW)
                self.state = 99
                self.className()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 100
                self.methodName()
                self.state = 101
                self.match(YAPLGrammarParser.LPAREN)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32229031936) != 0):
                    self.state = 102
                    self.parameterCall()


                self.state = 105
                self.match(YAPLGrammarParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(YAPLGrammarParser.PrimaryExpressionContext,0)


        def arithmeticExpression(self):
            return self.getTypedRuleContext(YAPLGrammarParser.ArithmeticExpressionContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(YAPLGrammarParser.MethodCallContext,0)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = YAPLGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.primaryExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.arithmeticExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.methodCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLGrammarParser.PrimaryExpressionContext)
            else:
                return self.getTypedRuleContext(YAPLGrammarParser.PrimaryExpressionContext,i)


        def MINUS(self):
            return self.getToken(YAPLGrammarParser.MINUS, 0)

        def MULT(self):
            return self.getToken(YAPLGrammarParser.MULT, 0)

        def PLUS(self):
            return self.getToken(YAPLGrammarParser.PLUS, 0)

        def DIV(self):
            return self.getToken(YAPLGrammarParser.DIV, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_arithmeticExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpression" ):
                listener.enterArithmeticExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpression" ):
                listener.exitArithmeticExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpression" ):
                return visitor.visitArithmeticExpression(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticExpression(self):

        localctx = YAPLGrammarParser.ArithmeticExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arithmeticExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.primaryExpression()
            self.state = 115
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 116
            self.primaryExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLGrammarParser.PrimaryExpressionContext)
            else:
                return self.getTypedRuleContext(YAPLGrammarParser.PrimaryExpressionContext,i)


        def EQUALS(self):
            return self.getToken(YAPLGrammarParser.EQUALS, 0)

        def LESS_THAN(self):
            return self.getToken(YAPLGrammarParser.LESS_THAN, 0)

        def GREAT_THAN(self):
            return self.getToken(YAPLGrammarParser.GREAT_THAN, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_boolExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpression" ):
                listener.enterBoolExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpression" ):
                listener.exitBoolExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpression" ):
                return visitor.visitBoolExpression(self)
            else:
                return visitor.visitChildren(self)




    def boolExpression(self):

        localctx = YAPLGrammarParser.BoolExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_boolExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.primaryExpression()
            self.state = 119
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 120
            self.primaryExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(YAPLGrammarParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(YAPLGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_assignExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpression" ):
                listener.enterAssignExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpression" ):
                listener.exitAssignExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpression" ):
                return visitor.visitAssignExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignExpression(self):

        localctx = YAPLGrammarParser.AssignExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(YAPLGrammarParser.ASSIGN)
            self.state = 123
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(YAPLGrammarParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(YAPLGrammarParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(YAPLGrammarParser.TypeContext,0)


        def LET(self):
            return self.getToken(YAPLGrammarParser.LET, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = YAPLGrammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 125
                self.match(YAPLGrammarParser.LET)


            self.state = 128
            self.match(YAPLGrammarParser.IDENTIFIER)
            self.state = 129
            self.match(YAPLGrammarParser.COLON)
            self.state = 130
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewVarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(YAPLGrammarParser.DeclarationContext,0)


        def assignExpression(self):
            return self.getTypedRuleContext(YAPLGrammarParser.AssignExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(YAPLGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_newVarDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewVarDeclaration" ):
                listener.enterNewVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewVarDeclaration" ):
                listener.exitNewVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewVarDeclaration" ):
                return visitor.visitNewVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def newVarDeclaration(self):

        localctx = YAPLGrammarParser.NewVarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_newVarDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.declaration()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 133
                self.assignExpression()


            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 136
                self.match(YAPLGrammarParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(YAPLGrammarParser.IDENTIFIER, 0)

        def assignExpression(self):
            return self.getTypedRuleContext(YAPLGrammarParser.AssignExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(YAPLGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = YAPLGrammarParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(YAPLGrammarParser.IDENTIFIER)
            self.state = 140
            self.assignExpression()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 141
                self.match(YAPLGrammarParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(YAPLGrammarParser.LET, 0)

        def declaration(self):
            return self.getTypedRuleContext(YAPLGrammarParser.DeclarationContext,0)


        def IN(self):
            return self.getToken(YAPLGrammarParser.IN, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_letDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetDeclaration" ):
                listener.enterLetDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetDeclaration" ):
                listener.exitLetDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetDeclaration" ):
                return visitor.visitLetDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def letDeclaration(self):

        localctx = YAPLGrammarParser.LetDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_letDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(YAPLGrammarParser.LET)
            self.state = 145
            self.declaration()
            self.state = 146
            self.match(YAPLGrammarParser.IN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(YAPLGrammarParser.IDENTIFIER, 0)

        def DOT(self):
            return self.getToken(YAPLGrammarParser.DOT, 0)

        def primaryExpression(self):
            return self.getTypedRuleContext(YAPLGrammarParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_methodCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = YAPLGrammarParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(YAPLGrammarParser.IDENTIFIER)
            self.state = 149
            self.match(YAPLGrammarParser.DOT)
            self.state = 150
            self.primaryExpression()
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

        def assignStatement(self):
            return self.getTypedRuleContext(YAPLGrammarParser.AssignStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(YAPLGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_statement

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

        localctx = YAPLGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.assignStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newVarDeclaration(self):
            return self.getTypedRuleContext(YAPLGrammarParser.NewVarDeclarationContext,0)


        def varDeclaration(self):
            return self.getTypedRuleContext(YAPLGrammarParser.VarDeclarationContext,0)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_assignStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatement" ):
                listener.enterAssignStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatement" ):
                listener.exitAssignStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = YAPLGrammarParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignStatement)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.newVarDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.varDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def letDeclaration(self):
            return self.getTypedRuleContext(YAPLGrammarParser.LetDeclarationContext,0)


        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.IF)
            else:
                return self.getToken(YAPLGrammarParser.IF, i)

        def boolExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLGrammarParser.BoolExpressionContext)
            else:
                return self.getTypedRuleContext(YAPLGrammarParser.BoolExpressionContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.THEN)
            else:
                return self.getToken(YAPLGrammarParser.THEN, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(YAPLGrammarParser.StatementContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.ELSE)
            else:
                return self.getToken(YAPLGrammarParser.ELSE, i)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = YAPLGrammarParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.letDeclaration()
            self.state = 161
            self.match(YAPLGrammarParser.IF)
            self.state = 162
            self.boolExpression()
            self.state = 163
            self.match(YAPLGrammarParser.THEN)
            self.state = 164
            self.statement()
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 165
                    self.match(YAPLGrammarParser.ELSE)
                    self.state = 166
                    self.match(YAPLGrammarParser.IF)
                    self.state = 167
                    self.boolExpression()
                    self.state = 168
                    self.match(YAPLGrammarParser.THEN)
                    self.state = 169
                    self.statement() 
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 176
                self.match(YAPLGrammarParser.ELSE)
                self.state = 177
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(YAPLGrammarParser.StatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(YAPLGrammarParser.IfStatementContext,0)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = YAPLGrammarParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statementList)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.ifStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineStatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(YAPLGrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(YAPLGrammarParser.RBRACE, 0)

        def statementList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLGrammarParser.StatementListContext)
            else:
                return self.getTypedRuleContext(YAPLGrammarParser.StatementListContext,i)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_defineStatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefineStatements" ):
                listener.enterDefineStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefineStatements" ):
                listener.exitDefineStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefineStatements" ):
                return visitor.visitDefineStatements(self)
            else:
                return visitor.visitChildren(self)




    def defineStatements(self):

        localctx = YAPLGrammarParser.DefineStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_defineStatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(YAPLGrammarParser.LBRACE)
            self.state = 186 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 185
                self.statementList()
                self.state = 188 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 32497467392) != 0)):
                    break

            self.state = 190
            self.match(YAPLGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(YAPLGrammarParser.DeclarationContext,0)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_formalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameter" ):
                listener.enterFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameter" ):
                listener.exitFormalParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameter" ):
                return visitor.visitFormalParameter(self)
            else:
                return visitor.visitChildren(self)




    def formalParameter(self):

        localctx = YAPLGrammarParser.FormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_formalParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formalParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLGrammarParser.FormalParameterContext)
            else:
                return self.getTypedRuleContext(YAPLGrammarParser.FormalParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.COMMA)
            else:
                return self.getToken(YAPLGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = YAPLGrammarParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.formalParameter()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 195
                self.match(YAPLGrammarParser.COMMA)
                self.state = 196
                self.formalParameter()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodName(self):
            return self.getTypedRuleContext(YAPLGrammarParser.MethodNameContext,0)


        def LPAREN(self):
            return self.getToken(YAPLGrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(YAPLGrammarParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(YAPLGrammarParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(YAPLGrammarParser.TypeContext,0)


        def LBRACE(self):
            return self.getToken(YAPLGrammarParser.LBRACE, 0)

        def defineStatements(self):
            return self.getTypedRuleContext(YAPLGrammarParser.DefineStatementsContext,0)


        def RBRACE(self):
            return self.getToken(YAPLGrammarParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(YAPLGrammarParser.SEMICOLON, 0)

        def parameterList(self):
            return self.getTypedRuleContext(YAPLGrammarParser.ParameterListContext,0)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = YAPLGrammarParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.methodName()
            self.state = 203
            self.match(YAPLGrammarParser.LPAREN)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28 or _la==32:
                self.state = 204
                self.parameterList()


            self.state = 207
            self.match(YAPLGrammarParser.RPAREN)
            self.state = 208
            self.match(YAPLGrammarParser.COLON)
            self.state = 209
            self.type_()
            self.state = 210
            self.match(YAPLGrammarParser.LBRACE)
            self.state = 211
            self.defineStatements()
            self.state = 212
            self.match(YAPLGrammarParser.RBRACE)
            self.state = 213
            self.match(YAPLGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(YAPLGrammarParser.StatementListContext,0)


        def methodDeclaration(self):
            return self.getTypedRuleContext(YAPLGrammarParser.MethodDeclarationContext,0)


        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_feature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature" ):
                listener.enterFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature" ):
                listener.exitFeature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeature" ):
                return visitor.visitFeature(self)
            else:
                return visitor.visitChildren(self)




    def feature(self):

        localctx = YAPLGrammarParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_feature)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.methodDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





