# Generated from YAPLGrammar.g4 by ANTLR 4.13.1
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
        4,1,42,299,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,4,0,64,8,0,11,0,12,0,
        65,1,1,1,1,1,1,1,1,3,1,72,8,1,1,1,1,1,5,1,76,8,1,10,1,12,1,79,9,
        1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,3,
        5,96,8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,5,8,105,8,8,10,8,12,8,108,9,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,119,8,9,1,9,1,9,1,9,3,
        9,124,8,9,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,133,8,11,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,144,8,12,10,12,12,12,
        147,9,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,16,3,16,161,8,16,1,16,1,16,1,16,1,16,1,17,3,17,168,8,17,1,17,1,
        17,1,17,1,17,3,17,174,8,17,1,17,3,17,177,8,17,1,18,1,18,1,18,3,18,
        182,8,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,
        3,21,195,8,21,1,22,1,22,3,22,199,8,22,1,23,3,23,202,8,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,213,8,23,1,23,1,23,3,
        23,217,8,23,5,23,219,8,23,10,23,12,23,222,9,23,1,23,1,23,3,23,226,
        8,23,1,23,1,23,3,23,230,8,23,3,23,232,8,23,1,23,5,23,235,8,23,10,
        23,12,23,238,9,23,1,23,3,23,241,8,23,1,24,1,24,1,24,3,24,246,8,24,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,257,8,25,1,25,
        1,25,1,26,3,26,262,8,26,1,26,4,26,265,8,26,11,26,12,26,266,1,26,
        3,26,270,8,26,1,27,1,27,1,28,1,28,1,28,5,28,277,8,28,10,28,12,28,
        280,9,28,1,29,1,29,1,29,3,29,285,8,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,1,30,1,30,3,30,297,8,30,1,30,0,0,31,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,0,3,1,0,20,23,1,0,31,32,1,0,17,19,316,0,63,1,0,0,0,2,67,1,
        0,0,0,4,83,1,0,0,0,6,85,1,0,0,0,8,87,1,0,0,0,10,95,1,0,0,0,12,97,
        1,0,0,0,14,99,1,0,0,0,16,101,1,0,0,0,18,123,1,0,0,0,20,125,1,0,0,
        0,22,132,1,0,0,0,24,134,1,0,0,0,26,148,1,0,0,0,28,152,1,0,0,0,30,
        155,1,0,0,0,32,160,1,0,0,0,34,167,1,0,0,0,36,178,1,0,0,0,38,183,
        1,0,0,0,40,188,1,0,0,0,42,192,1,0,0,0,44,198,1,0,0,0,46,201,1,0,
        0,0,48,245,1,0,0,0,50,247,1,0,0,0,52,261,1,0,0,0,54,271,1,0,0,0,
        56,273,1,0,0,0,58,281,1,0,0,0,60,296,1,0,0,0,62,64,3,2,1,0,63,62,
        1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,1,1,0,0,0,67,
        68,5,1,0,0,68,71,3,4,2,0,69,70,5,2,0,0,70,72,3,6,3,0,71,69,1,0,0,
        0,71,72,1,0,0,0,72,73,1,0,0,0,73,77,5,5,0,0,74,76,3,60,30,0,75,74,
        1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,
        79,77,1,0,0,0,80,81,5,6,0,0,81,82,5,8,0,0,82,3,1,0,0,0,83,84,5,35,
        0,0,84,5,1,0,0,0,85,86,5,35,0,0,86,7,1,0,0,0,87,88,5,35,0,0,88,9,
        1,0,0,0,89,96,5,10,0,0,90,96,5,12,0,0,91,96,3,4,2,0,92,96,5,13,0,
        0,93,96,5,11,0,0,94,96,5,30,0,0,95,89,1,0,0,0,95,90,1,0,0,0,95,91,
        1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,11,1,0,0,0,
        97,98,5,28,0,0,98,13,1,0,0,0,99,100,7,0,0,0,100,15,1,0,0,0,101,106,
        3,22,11,0,102,103,5,25,0,0,103,105,3,22,11,0,104,102,1,0,0,0,105,
        108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,17,1,0,0,0,108,106,
        1,0,0,0,109,124,3,20,10,0,110,124,5,36,0,0,111,124,5,37,0,0,112,
        124,5,35,0,0,113,114,5,24,0,0,114,124,3,4,2,0,115,116,3,8,4,0,116,
        118,5,3,0,0,117,119,3,16,8,0,118,117,1,0,0,0,118,119,1,0,0,0,119,
        120,1,0,0,0,120,121,5,4,0,0,121,124,1,0,0,0,122,124,5,13,0,0,123,
        109,1,0,0,0,123,110,1,0,0,0,123,111,1,0,0,0,123,112,1,0,0,0,123,
        113,1,0,0,0,123,115,1,0,0,0,123,122,1,0,0,0,124,19,1,0,0,0,125,126,
        7,1,0,0,126,21,1,0,0,0,127,133,3,18,9,0,128,133,3,24,12,0,129,133,
        3,40,20,0,130,133,3,30,15,0,131,133,3,44,22,0,132,127,1,0,0,0,132,
        128,1,0,0,0,132,129,1,0,0,0,132,130,1,0,0,0,132,131,1,0,0,0,133,
        23,1,0,0,0,134,145,3,18,9,0,135,136,5,20,0,0,136,144,3,18,9,0,137,
        138,5,22,0,0,138,144,3,18,9,0,139,140,5,21,0,0,140,144,3,18,9,0,
        141,142,5,23,0,0,142,144,3,18,9,0,143,135,1,0,0,0,143,137,1,0,0,
        0,143,139,1,0,0,0,143,141,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,
        0,145,146,1,0,0,0,146,25,1,0,0,0,147,145,1,0,0,0,148,149,3,18,9,
        0,149,150,7,2,0,0,150,151,3,18,9,0,151,27,1,0,0,0,152,153,5,9,0,
        0,153,154,3,22,11,0,154,29,1,0,0,0,155,156,3,8,4,0,156,157,5,3,0,
        0,157,158,5,4,0,0,158,31,1,0,0,0,159,161,5,28,0,0,160,159,1,0,0,
        0,160,161,1,0,0,0,161,162,1,0,0,0,162,163,5,35,0,0,163,164,5,7,0,
        0,164,165,3,10,5,0,165,33,1,0,0,0,166,168,5,28,0,0,167,166,1,0,0,
        0,167,168,1,0,0,0,168,169,1,0,0,0,169,170,5,35,0,0,170,171,5,7,0,
        0,171,173,3,10,5,0,172,174,3,28,14,0,173,172,1,0,0,0,173,174,1,0,
        0,0,174,176,1,0,0,0,175,177,5,8,0,0,176,175,1,0,0,0,176,177,1,0,
        0,0,177,35,1,0,0,0,178,179,5,35,0,0,179,181,3,28,14,0,180,182,5,
        8,0,0,181,180,1,0,0,0,181,182,1,0,0,0,182,37,1,0,0,0,183,184,5,28,
        0,0,184,185,3,32,16,0,185,186,5,26,0,0,186,187,3,48,24,0,187,39,
        1,0,0,0,188,189,5,35,0,0,189,190,5,27,0,0,190,191,3,18,9,0,191,41,
        1,0,0,0,192,194,3,22,11,0,193,195,5,8,0,0,194,193,1,0,0,0,194,195,
        1,0,0,0,195,43,1,0,0,0,196,199,3,34,17,0,197,199,3,36,18,0,198,196,
        1,0,0,0,198,197,1,0,0,0,199,45,1,0,0,0,200,202,5,28,0,0,201,200,
        1,0,0,0,201,202,1,0,0,0,202,203,1,0,0,0,203,204,5,14,0,0,204,205,
        3,26,13,0,205,206,5,15,0,0,206,220,3,42,21,0,207,208,5,16,0,0,208,
        209,5,14,0,0,209,210,3,26,13,0,210,212,5,15,0,0,211,213,5,5,0,0,
        212,211,1,0,0,0,212,213,1,0,0,0,213,214,1,0,0,0,214,216,3,42,21,
        0,215,217,5,6,0,0,216,215,1,0,0,0,216,217,1,0,0,0,217,219,1,0,0,
        0,218,207,1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,
        0,221,231,1,0,0,0,222,220,1,0,0,0,223,225,5,16,0,0,224,226,5,5,0,
        0,225,224,1,0,0,0,225,226,1,0,0,0,226,227,1,0,0,0,227,229,3,42,21,
        0,228,230,5,6,0,0,229,228,1,0,0,0,229,230,1,0,0,0,230,232,1,0,0,
        0,231,223,1,0,0,0,231,232,1,0,0,0,232,236,1,0,0,0,233,235,5,34,0,
        0,234,233,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,
        0,237,240,1,0,0,0,238,236,1,0,0,0,239,241,5,8,0,0,240,239,1,0,0,
        0,240,241,1,0,0,0,241,47,1,0,0,0,242,246,3,42,21,0,243,246,3,46,
        23,0,244,246,3,50,25,0,245,242,1,0,0,0,245,243,1,0,0,0,245,244,1,
        0,0,0,246,49,1,0,0,0,247,248,5,3,0,0,248,249,5,28,0,0,249,250,3,
        32,16,0,250,256,5,26,0,0,251,252,5,5,0,0,252,253,3,42,21,0,253,254,
        5,6,0,0,254,255,5,8,0,0,255,257,1,0,0,0,256,251,1,0,0,0,256,257,
        1,0,0,0,257,258,1,0,0,0,258,259,5,4,0,0,259,51,1,0,0,0,260,262,5,
        5,0,0,261,260,1,0,0,0,261,262,1,0,0,0,262,264,1,0,0,0,263,265,3,
        48,24,0,264,263,1,0,0,0,265,266,1,0,0,0,266,264,1,0,0,0,266,267,
        1,0,0,0,267,269,1,0,0,0,268,270,5,6,0,0,269,268,1,0,0,0,269,270,
        1,0,0,0,270,53,1,0,0,0,271,272,3,32,16,0,272,55,1,0,0,0,273,278,
        3,54,27,0,274,275,5,25,0,0,275,277,3,54,27,0,276,274,1,0,0,0,277,
        280,1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,279,57,1,0,0,0,280,278,
        1,0,0,0,281,282,3,8,4,0,282,284,5,3,0,0,283,285,3,56,28,0,284,283,
        1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,287,5,4,0,0,287,288,
        5,7,0,0,288,289,3,10,5,0,289,290,5,5,0,0,290,291,3,52,26,0,291,292,
        5,6,0,0,292,293,5,8,0,0,293,59,1,0,0,0,294,297,3,48,24,0,295,297,
        3,58,29,0,296,294,1,0,0,0,296,295,1,0,0,0,297,61,1,0,0,0,34,65,71,
        77,95,106,118,123,132,143,145,160,167,173,176,181,194,198,201,212,
        216,220,225,229,231,236,240,245,256,261,266,269,278,284,296
    ]

class YAPLGrammarParser ( Parser ):

    grammarFileName = "YAPLGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'inherits'", "'('", "')'", 
                     "'{'", "'}'", "':'", "';'", "'<-'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'self'", "'if'", "'then'", "'else'", 
                     "'<'", "'>'", "'='", "'-'", "'+'", "'*'", "'/'", "'new'", 
                     "','", "'in'", "'.'", "'let'", "'out'", "'Object'", 
                     "'true'", "'false'", "'_'", "'fi'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'SIZES'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "INHERITS", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "COLON", "SEMICOLON", "ASSIGN", 
                      "INT", "BOOL", "STRING", "SELF", "IF", "THEN", "ELSE", 
                      "LESS_THAN", "GREAT_THAN", "EQUALS", "MINUS", "PLUS", 
                      "MULT", "DIV", "NEW", "COMMA", "IN", "DOT", "LET", 
                      "OUT", "OBJECT", "TRUE", "FALSE", "UNDERSCORE", "FI", 
                      "IDENTIFIER", "INT_LITERAL", "STRING_LITERAL", "SIZES", 
                      "WS", "COMMENT", "LINE_COMMENT", "ERROR" ]

    RULE_program = 0
    RULE_classDeclaration = 1
    RULE_className = 2
    RULE_classNameParent = 3
    RULE_methodName = 4
    RULE_type = 5
    RULE_variable = 6
    RULE_operator = 7
    RULE_parameterCall = 8
    RULE_primaryExpression = 9
    RULE_boolDeclaration = 10
    RULE_expression = 11
    RULE_arithmeticExpression = 12
    RULE_boolExpression = 13
    RULE_assignExpression = 14
    RULE_uniqueMethod = 15
    RULE_declaration = 16
    RULE_newVarDeclaration = 17
    RULE_varDeclaration = 18
    RULE_letDeclaration = 19
    RULE_methodCall = 20
    RULE_statement = 21
    RULE_assignStatement = 22
    RULE_ifStatement = 23
    RULE_statementList = 24
    RULE_letExpression = 25
    RULE_defineStatements = 26
    RULE_formalParameter = 27
    RULE_parameterList = 28
    RULE_methodDeclaration = 29
    RULE_feature = 30

    ruleNames =  [ "program", "classDeclaration", "className", "classNameParent", 
                   "methodName", "type", "variable", "operator", "parameterCall", 
                   "primaryExpression", "boolDeclaration", "expression", 
                   "arithmeticExpression", "boolExpression", "assignExpression", 
                   "uniqueMethod", "declaration", "newVarDeclaration", "varDeclaration", 
                   "letDeclaration", "methodCall", "statement", "assignStatement", 
                   "ifStatement", "statementList", "letExpression", "defineStatements", 
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
    OBJECT=30
    TRUE=31
    FALSE=32
    UNDERSCORE=33
    FI=34
    IDENTIFIER=35
    INT_LITERAL=36
    STRING_LITERAL=37
    SIZES=38
    WS=39
    COMMENT=40
    LINE_COMMENT=41
    ERROR=42

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
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.classDeclaration()
                self.state = 65 
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

        def className(self):
            return self.getTypedRuleContext(YAPLGrammarParser.ClassNameContext,0)


        def LBRACE(self):
            return self.getToken(YAPLGrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(YAPLGrammarParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(YAPLGrammarParser.SEMICOLON, 0)

        def INHERITS(self):
            return self.getToken(YAPLGrammarParser.INHERITS, 0)

        def classNameParent(self):
            return self.getTypedRuleContext(YAPLGrammarParser.ClassNameParentContext,0)


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
            self.state = 67
            self.match(YAPLGrammarParser.CLASS)
            self.state = 68
            self.className()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 69
                self.match(YAPLGrammarParser.INHERITS)
                self.state = 70
                self.classNameParent()


            self.state = 73
            self.match(YAPLGrammarParser.LBRACE)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 247245856776) != 0):
                self.state = 74
                self.feature()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(YAPLGrammarParser.RBRACE)
            self.state = 81
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
            self.state = 83
            self.match(YAPLGrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassNameParentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(YAPLGrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_classNameParent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassNameParent" ):
                listener.enterClassNameParent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassNameParent" ):
                listener.exitClassNameParent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassNameParent" ):
                return visitor.visitClassNameParent(self)
            else:
                return visitor.visitChildren(self)




    def classNameParent(self):

        localctx = YAPLGrammarParser.ClassNameParentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classNameParent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
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
        self.enterRule(localctx, 8, self.RULE_methodName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
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

        def className(self):
            return self.getTypedRuleContext(YAPLGrammarParser.ClassNameContext,0)


        def SELF(self):
            return self.getToken(YAPLGrammarParser.SELF, 0)

        def BOOL(self):
            return self.getToken(YAPLGrammarParser.BOOL, 0)

        def OBJECT(self):
            return self.getToken(YAPLGrammarParser.OBJECT, 0)

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
        self.enterRule(localctx, 10, self.RULE_type)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(YAPLGrammarParser.INT)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(YAPLGrammarParser.STRING)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.className()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.match(YAPLGrammarParser.SELF)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.match(YAPLGrammarParser.BOOL)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.match(YAPLGrammarParser.OBJECT)
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
        self.enterRule(localctx, 12, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(YAPLGrammarParser.LET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(YAPLGrammarParser.MINUS, 0)

        def MULT(self):
            return self.getToken(YAPLGrammarParser.MULT, 0)

        def PLUS(self):
            return self.getToken(YAPLGrammarParser.PLUS, 0)

        def DIV(self):
            return self.getToken(YAPLGrammarParser.DIV, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = YAPLGrammarParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_parameterCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.expression()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 102
                self.match(YAPLGrammarParser.COMMA)
                self.state = 103
                self.expression()
                self.state = 108
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

        def boolDeclaration(self):
            return self.getTypedRuleContext(YAPLGrammarParser.BoolDeclarationContext,0)


        def INT_LITERAL(self):
            return self.getToken(YAPLGrammarParser.INT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(YAPLGrammarParser.STRING_LITERAL, 0)

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


        def SELF(self):
            return self.getToken(YAPLGrammarParser.SELF, 0)

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
        self.enterRule(localctx, 18, self.RULE_primaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.boolDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(YAPLGrammarParser.INT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.match(YAPLGrammarParser.STRING_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.match(YAPLGrammarParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.match(YAPLGrammarParser.NEW)
                self.state = 114
                self.className()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 115
                self.methodName()
                self.state = 116
                self.match(YAPLGrammarParser.LPAREN)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 247245840384) != 0):
                    self.state = 117
                    self.parameterCall()


                self.state = 120
                self.match(YAPLGrammarParser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 122
                self.match(YAPLGrammarParser.SELF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(YAPLGrammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(YAPLGrammarParser.FALSE, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_boolDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolDeclaration" ):
                listener.enterBoolDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolDeclaration" ):
                listener.exitBoolDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolDeclaration" ):
                return visitor.visitBoolDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def boolDeclaration(self):

        localctx = YAPLGrammarParser.BoolDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_boolDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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


        def uniqueMethod(self):
            return self.getTypedRuleContext(YAPLGrammarParser.UniqueMethodContext,0)


        def assignStatement(self):
            return self.getTypedRuleContext(YAPLGrammarParser.AssignStatementContext,0)


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
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.primaryExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.arithmeticExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.methodCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.uniqueMethod()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 131
                self.assignStatement()
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


        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.MINUS)
            else:
                return self.getToken(YAPLGrammarParser.MINUS, i)

        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.MULT)
            else:
                return self.getToken(YAPLGrammarParser.MULT, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.PLUS)
            else:
                return self.getToken(YAPLGrammarParser.PLUS, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.DIV)
            else:
                return self.getToken(YAPLGrammarParser.DIV, i)

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
        self.enterRule(localctx, 24, self.RULE_arithmeticExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.primaryExpression()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0):
                self.state = 143
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20]:
                    self.state = 135
                    self.match(YAPLGrammarParser.MINUS)
                    self.state = 136
                    self.primaryExpression()
                    pass
                elif token in [22]:
                    self.state = 137
                    self.match(YAPLGrammarParser.MULT)
                    self.state = 138
                    self.primaryExpression()
                    pass
                elif token in [21]:
                    self.state = 139
                    self.match(YAPLGrammarParser.PLUS)
                    self.state = 140
                    self.primaryExpression()
                    pass
                elif token in [23]:
                    self.state = 141
                    self.match(YAPLGrammarParser.DIV)
                    self.state = 142
                    self.primaryExpression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 26, self.RULE_boolExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.primaryExpression()
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 150
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
        self.enterRule(localctx, 28, self.RULE_assignExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(YAPLGrammarParser.ASSIGN)
            self.state = 153
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UniqueMethodContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_uniqueMethod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniqueMethod" ):
                listener.enterUniqueMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniqueMethod" ):
                listener.exitUniqueMethod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniqueMethod" ):
                return visitor.visitUniqueMethod(self)
            else:
                return visitor.visitChildren(self)




    def uniqueMethod(self):

        localctx = YAPLGrammarParser.UniqueMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_uniqueMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.methodName()
            self.state = 156
            self.match(YAPLGrammarParser.LPAREN)
            self.state = 157
            self.match(YAPLGrammarParser.RPAREN)
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
        self.enterRule(localctx, 32, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 159
                self.match(YAPLGrammarParser.LET)


            self.state = 162
            self.match(YAPLGrammarParser.IDENTIFIER)
            self.state = 163
            self.match(YAPLGrammarParser.COLON)
            self.state = 164
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

        def IDENTIFIER(self):
            return self.getToken(YAPLGrammarParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(YAPLGrammarParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(YAPLGrammarParser.TypeContext,0)


        def LET(self):
            return self.getToken(YAPLGrammarParser.LET, 0)

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
        self.enterRule(localctx, 34, self.RULE_newVarDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 166
                self.match(YAPLGrammarParser.LET)


            self.state = 169
            self.match(YAPLGrammarParser.IDENTIFIER)
            self.state = 170
            self.match(YAPLGrammarParser.COLON)
            self.state = 171
            self.type_()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 172
                self.assignExpression()


            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 175
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
        self.enterRule(localctx, 36, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(YAPLGrammarParser.IDENTIFIER)
            self.state = 179
            self.assignExpression()
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 180
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

        def statementList(self):
            return self.getTypedRuleContext(YAPLGrammarParser.StatementListContext,0)


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
        self.enterRule(localctx, 38, self.RULE_letDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(YAPLGrammarParser.LET)
            self.state = 184
            self.declaration()
            self.state = 185
            self.match(YAPLGrammarParser.IN)
            self.state = 186
            self.statementList()
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
        self.enterRule(localctx, 40, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(YAPLGrammarParser.IDENTIFIER)
            self.state = 189
            self.match(YAPLGrammarParser.DOT)
            self.state = 190
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

        def expression(self):
            return self.getTypedRuleContext(YAPLGrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(YAPLGrammarParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.expression()
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 193
                self.match(YAPLGrammarParser.SEMICOLON)


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
        self.enterRule(localctx, 44, self.RULE_assignStatement)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.newVarDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
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


        def LET(self):
            return self.getToken(YAPLGrammarParser.LET, 0)

        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.ELSE)
            else:
                return self.getToken(YAPLGrammarParser.ELSE, i)

        def FI(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.FI)
            else:
                return self.getToken(YAPLGrammarParser.FI, i)

        def SEMICOLON(self):
            return self.getToken(YAPLGrammarParser.SEMICOLON, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.LBRACE)
            else:
                return self.getToken(YAPLGrammarParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLGrammarParser.RBRACE)
            else:
                return self.getToken(YAPLGrammarParser.RBRACE, i)

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
        self.enterRule(localctx, 46, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 200
                self.match(YAPLGrammarParser.LET)


            self.state = 203
            self.match(YAPLGrammarParser.IF)
            self.state = 204
            self.boolExpression()
            self.state = 205
            self.match(YAPLGrammarParser.THEN)
            self.state = 206
            self.statement()
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 207
                    self.match(YAPLGrammarParser.ELSE)
                    self.state = 208
                    self.match(YAPLGrammarParser.IF)
                    self.state = 209
                    self.boolExpression()
                    self.state = 210
                    self.match(YAPLGrammarParser.THEN)
                    self.state = 212
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 211
                        self.match(YAPLGrammarParser.LBRACE)


                    self.state = 214
                    self.statement()
                    self.state = 216
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        self.state = 215
                        self.match(YAPLGrammarParser.RBRACE)

             
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 223
                self.match(YAPLGrammarParser.ELSE)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 224
                    self.match(YAPLGrammarParser.LBRACE)


                self.state = 227
                self.statement()
                self.state = 229
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 228
                    self.match(YAPLGrammarParser.RBRACE)




            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 233
                self.match(YAPLGrammarParser.FI)
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 239
                self.match(YAPLGrammarParser.SEMICOLON)


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


        def letExpression(self):
            return self.getTypedRuleContext(YAPLGrammarParser.LetExpressionContext,0)


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
        self.enterRule(localctx, 48, self.RULE_statementList)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.letExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(YAPLGrammarParser.LPAREN, 0)

        def LET(self):
            return self.getToken(YAPLGrammarParser.LET, 0)

        def declaration(self):
            return self.getTypedRuleContext(YAPLGrammarParser.DeclarationContext,0)


        def IN(self):
            return self.getToken(YAPLGrammarParser.IN, 0)

        def RPAREN(self):
            return self.getToken(YAPLGrammarParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(YAPLGrammarParser.LBRACE, 0)

        def statement(self):
            return self.getTypedRuleContext(YAPLGrammarParser.StatementContext,0)


        def RBRACE(self):
            return self.getToken(YAPLGrammarParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(YAPLGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return YAPLGrammarParser.RULE_letExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetExpression" ):
                listener.enterLetExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetExpression" ):
                listener.exitLetExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetExpression" ):
                return visitor.visitLetExpression(self)
            else:
                return visitor.visitChildren(self)




    def letExpression(self):

        localctx = YAPLGrammarParser.LetExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_letExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(YAPLGrammarParser.LPAREN)
            self.state = 248
            self.match(YAPLGrammarParser.LET)
            self.state = 249
            self.declaration()
            self.state = 250
            self.match(YAPLGrammarParser.IN)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 251
                self.match(YAPLGrammarParser.LBRACE)
                self.state = 252
                self.statement()
                self.state = 253
                self.match(YAPLGrammarParser.RBRACE)
                self.state = 254
                self.match(YAPLGrammarParser.SEMICOLON)


            self.state = 258
            self.match(YAPLGrammarParser.RPAREN)
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

        def statementList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLGrammarParser.StatementListContext)
            else:
                return self.getTypedRuleContext(YAPLGrammarParser.StatementListContext,i)


        def RBRACE(self):
            return self.getToken(YAPLGrammarParser.RBRACE, 0)

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
        self.enterRule(localctx, 52, self.RULE_defineStatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 260
                self.match(YAPLGrammarParser.LBRACE)


            self.state = 264 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 263
                self.statementList()
                self.state = 266 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 247245856776) != 0)):
                    break

            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 268
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
        self.enterRule(localctx, 54, self.RULE_formalParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
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
        self.enterRule(localctx, 56, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.formalParameter()
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 274
                self.match(YAPLGrammarParser.COMMA)
                self.state = 275
                self.formalParameter()
                self.state = 280
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
        self.enterRule(localctx, 58, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.methodName()
            self.state = 282
            self.match(YAPLGrammarParser.LPAREN)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28 or _la==35:
                self.state = 283
                self.parameterList()


            self.state = 286
            self.match(YAPLGrammarParser.RPAREN)
            self.state = 287
            self.match(YAPLGrammarParser.COLON)
            self.state = 288
            self.type_()
            self.state = 289
            self.match(YAPLGrammarParser.LBRACE)
            self.state = 290
            self.defineStatements()
            self.state = 291
            self.match(YAPLGrammarParser.RBRACE)
            self.state = 292
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
        self.enterRule(localctx, 60, self.RULE_feature)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.methodDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





