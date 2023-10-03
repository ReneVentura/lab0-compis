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
        4,1,42,282,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,4,0,62,8,0,11,0,12,0,63,1,1,1,
        1,1,1,1,1,3,1,70,8,1,1,1,1,1,5,1,74,8,1,10,1,12,1,77,9,1,1,1,1,1,
        1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,94,8,5,1,
        6,1,6,1,7,1,7,1,7,5,7,101,8,7,10,7,12,7,104,9,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,115,8,8,1,8,1,8,1,8,3,8,120,8,8,1,9,1,9,
        1,10,1,10,1,10,1,10,3,10,128,8,10,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,3,15,146,8,15,
        1,15,1,15,1,15,1,15,1,16,1,16,3,16,154,8,16,1,16,3,16,157,8,16,1,
        17,1,17,1,17,3,17,162,8,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,
        19,1,19,1,20,1,20,3,20,175,8,20,1,20,3,20,178,8,20,1,21,1,21,3,21,
        182,8,21,1,22,3,22,185,8,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,3,22,196,8,22,1,22,1,22,3,22,200,8,22,5,22,202,8,22,10,22,
        12,22,205,9,22,1,22,1,22,3,22,209,8,22,1,22,1,22,3,22,213,8,22,3,
        22,215,8,22,1,22,5,22,218,8,22,10,22,12,22,221,9,22,1,22,3,22,224,
        8,22,1,23,1,23,1,23,3,23,229,8,23,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,3,24,240,8,24,1,24,1,24,1,25,3,25,245,8,25,1,25,4,
        25,248,8,25,11,25,12,25,249,1,25,3,25,253,8,25,1,26,1,26,1,27,1,
        27,1,27,5,27,260,8,27,10,27,12,27,263,9,27,1,28,1,28,1,28,3,28,268,
        8,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,3,29,280,
        8,29,1,29,0,0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,0,3,1,0,31,32,1,0,20,23,1,0,
        17,19,295,0,61,1,0,0,0,2,65,1,0,0,0,4,81,1,0,0,0,6,83,1,0,0,0,8,
        85,1,0,0,0,10,93,1,0,0,0,12,95,1,0,0,0,14,97,1,0,0,0,16,119,1,0,
        0,0,18,121,1,0,0,0,20,127,1,0,0,0,22,129,1,0,0,0,24,133,1,0,0,0,
        26,137,1,0,0,0,28,140,1,0,0,0,30,145,1,0,0,0,32,151,1,0,0,0,34,158,
        1,0,0,0,36,163,1,0,0,0,38,168,1,0,0,0,40,174,1,0,0,0,42,181,1,0,
        0,0,44,184,1,0,0,0,46,228,1,0,0,0,48,230,1,0,0,0,50,244,1,0,0,0,
        52,254,1,0,0,0,54,256,1,0,0,0,56,264,1,0,0,0,58,279,1,0,0,0,60,62,
        3,2,1,0,61,60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,
        64,1,1,0,0,0,65,66,5,1,0,0,66,69,3,4,2,0,67,68,5,2,0,0,68,70,3,6,
        3,0,69,67,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,75,5,5,0,0,72,74,
        3,58,29,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,
        0,76,78,1,0,0,0,77,75,1,0,0,0,78,79,5,6,0,0,79,80,5,8,0,0,80,3,1,
        0,0,0,81,82,5,35,0,0,82,5,1,0,0,0,83,84,5,35,0,0,84,7,1,0,0,0,85,
        86,5,35,0,0,86,9,1,0,0,0,87,94,5,10,0,0,88,94,5,12,0,0,89,94,3,4,
        2,0,90,94,5,13,0,0,91,94,5,11,0,0,92,94,5,30,0,0,93,87,1,0,0,0,93,
        88,1,0,0,0,93,89,1,0,0,0,93,90,1,0,0,0,93,91,1,0,0,0,93,92,1,0,0,
        0,94,11,1,0,0,0,95,96,5,28,0,0,96,13,1,0,0,0,97,102,3,20,10,0,98,
        99,5,25,0,0,99,101,3,20,10,0,100,98,1,0,0,0,101,104,1,0,0,0,102,
        100,1,0,0,0,102,103,1,0,0,0,103,15,1,0,0,0,104,102,1,0,0,0,105,120,
        3,18,9,0,106,120,5,36,0,0,107,120,5,37,0,0,108,120,5,35,0,0,109,
        110,5,24,0,0,110,120,3,4,2,0,111,112,3,8,4,0,112,114,5,3,0,0,113,
        115,3,14,7,0,114,113,1,0,0,0,114,115,1,0,0,0,115,116,1,0,0,0,116,
        117,5,4,0,0,117,120,1,0,0,0,118,120,5,13,0,0,119,105,1,0,0,0,119,
        106,1,0,0,0,119,107,1,0,0,0,119,108,1,0,0,0,119,109,1,0,0,0,119,
        111,1,0,0,0,119,118,1,0,0,0,120,17,1,0,0,0,121,122,7,0,0,0,122,19,
        1,0,0,0,123,128,3,16,8,0,124,128,3,22,11,0,125,128,3,38,19,0,126,
        128,3,28,14,0,127,123,1,0,0,0,127,124,1,0,0,0,127,125,1,0,0,0,127,
        126,1,0,0,0,128,21,1,0,0,0,129,130,3,16,8,0,130,131,7,1,0,0,131,
        132,3,16,8,0,132,23,1,0,0,0,133,134,3,16,8,0,134,135,7,2,0,0,135,
        136,3,16,8,0,136,25,1,0,0,0,137,138,5,9,0,0,138,139,3,20,10,0,139,
        27,1,0,0,0,140,141,3,8,4,0,141,142,5,3,0,0,142,143,5,4,0,0,143,29,
        1,0,0,0,144,146,5,28,0,0,145,144,1,0,0,0,145,146,1,0,0,0,146,147,
        1,0,0,0,147,148,5,35,0,0,148,149,5,7,0,0,149,150,3,10,5,0,150,31,
        1,0,0,0,151,153,3,30,15,0,152,154,3,26,13,0,153,152,1,0,0,0,153,
        154,1,0,0,0,154,156,1,0,0,0,155,157,5,8,0,0,156,155,1,0,0,0,156,
        157,1,0,0,0,157,33,1,0,0,0,158,159,5,35,0,0,159,161,3,26,13,0,160,
        162,5,8,0,0,161,160,1,0,0,0,161,162,1,0,0,0,162,35,1,0,0,0,163,164,
        5,28,0,0,164,165,3,30,15,0,165,166,5,26,0,0,166,167,3,46,23,0,167,
        37,1,0,0,0,168,169,5,35,0,0,169,170,5,27,0,0,170,171,3,16,8,0,171,
        39,1,0,0,0,172,175,3,42,21,0,173,175,3,20,10,0,174,172,1,0,0,0,174,
        173,1,0,0,0,175,177,1,0,0,0,176,178,5,8,0,0,177,176,1,0,0,0,177,
        178,1,0,0,0,178,41,1,0,0,0,179,182,3,32,16,0,180,182,3,34,17,0,181,
        179,1,0,0,0,181,180,1,0,0,0,182,43,1,0,0,0,183,185,5,28,0,0,184,
        183,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,187,5,14,0,0,187,
        188,3,24,12,0,188,189,5,15,0,0,189,203,3,40,20,0,190,191,5,16,0,
        0,191,192,5,14,0,0,192,193,3,24,12,0,193,195,5,15,0,0,194,196,5,
        5,0,0,195,194,1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,197,199,3,
        40,20,0,198,200,5,6,0,0,199,198,1,0,0,0,199,200,1,0,0,0,200,202,
        1,0,0,0,201,190,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,
        1,0,0,0,204,214,1,0,0,0,205,203,1,0,0,0,206,208,5,16,0,0,207,209,
        5,5,0,0,208,207,1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,212,
        3,40,20,0,211,213,5,6,0,0,212,211,1,0,0,0,212,213,1,0,0,0,213,215,
        1,0,0,0,214,206,1,0,0,0,214,215,1,0,0,0,215,219,1,0,0,0,216,218,
        5,34,0,0,217,216,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,220,
        1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,222,224,5,8,0,0,223,222,
        1,0,0,0,223,224,1,0,0,0,224,45,1,0,0,0,225,229,3,40,20,0,226,229,
        3,44,22,0,227,229,3,48,24,0,228,225,1,0,0,0,228,226,1,0,0,0,228,
        227,1,0,0,0,229,47,1,0,0,0,230,231,5,3,0,0,231,232,5,28,0,0,232,
        233,3,30,15,0,233,239,5,26,0,0,234,235,5,5,0,0,235,236,3,40,20,0,
        236,237,5,6,0,0,237,238,5,8,0,0,238,240,1,0,0,0,239,234,1,0,0,0,
        239,240,1,0,0,0,240,241,1,0,0,0,241,242,5,4,0,0,242,49,1,0,0,0,243,
        245,5,5,0,0,244,243,1,0,0,0,244,245,1,0,0,0,245,247,1,0,0,0,246,
        248,3,46,23,0,247,246,1,0,0,0,248,249,1,0,0,0,249,247,1,0,0,0,249,
        250,1,0,0,0,250,252,1,0,0,0,251,253,5,6,0,0,252,251,1,0,0,0,252,
        253,1,0,0,0,253,51,1,0,0,0,254,255,3,30,15,0,255,53,1,0,0,0,256,
        261,3,52,26,0,257,258,5,25,0,0,258,260,3,52,26,0,259,257,1,0,0,0,
        260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,55,1,0,0,0,263,
        261,1,0,0,0,264,265,3,8,4,0,265,267,5,3,0,0,266,268,3,54,27,0,267,
        266,1,0,0,0,267,268,1,0,0,0,268,269,1,0,0,0,269,270,5,4,0,0,270,
        271,5,7,0,0,271,272,3,10,5,0,272,273,5,5,0,0,273,274,3,50,25,0,274,
        275,5,6,0,0,275,276,5,8,0,0,276,57,1,0,0,0,277,280,3,46,23,0,278,
        280,3,56,28,0,279,277,1,0,0,0,279,278,1,0,0,0,280,59,1,0,0,0,32,
        63,69,75,93,102,114,119,127,145,153,156,161,174,177,181,184,195,
        199,203,208,212,214,219,223,228,239,244,249,252,261,267,279
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
    RULE_parameterCall = 7
    RULE_primaryExpression = 8
    RULE_boolDeclaration = 9
    RULE_expression = 10
    RULE_arithmeticExpression = 11
    RULE_boolExpression = 12
    RULE_assignExpression = 13
    RULE_uniqueMethod = 14
    RULE_declaration = 15
    RULE_newVarDeclaration = 16
    RULE_varDeclaration = 17
    RULE_letDeclaration = 18
    RULE_methodCall = 19
    RULE_statement = 20
    RULE_assignStatement = 21
    RULE_ifStatement = 22
    RULE_statementList = 23
    RULE_letExpression = 24
    RULE_defineStatements = 25
    RULE_formalParameter = 26
    RULE_parameterList = 27
    RULE_methodDeclaration = 28
    RULE_feature = 29

    ruleNames =  [ "program", "classDeclaration", "className", "classNameParent", 
                   "methodName", "type", "variable", "parameterCall", "primaryExpression", 
                   "boolDeclaration", "expression", "arithmeticExpression", 
                   "boolExpression", "assignExpression", "uniqueMethod", 
                   "declaration", "newVarDeclaration", "varDeclaration", 
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
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.classDeclaration()
                self.state = 63 
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
            self.state = 65
            self.match(YAPLGrammarParser.CLASS)
            self.state = 66
            self.className()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 67
                self.match(YAPLGrammarParser.INHERITS)
                self.state = 68
                self.classNameParent()


            self.state = 71
            self.match(YAPLGrammarParser.LBRACE)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 247245856776) != 0):
                self.state = 72
                self.feature()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(YAPLGrammarParser.RBRACE)
            self.state = 79
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
            self.state = 81
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
            self.state = 83
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
            self.state = 85
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
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(YAPLGrammarParser.INT)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(YAPLGrammarParser.STRING)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.className()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.match(YAPLGrammarParser.SELF)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.match(YAPLGrammarParser.BOOL)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 6)
                self.state = 92
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
            self.state = 95
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
        self.enterRule(localctx, 14, self.RULE_parameterCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.expression()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 98
                self.match(YAPLGrammarParser.COMMA)
                self.state = 99
                self.expression()
                self.state = 104
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
        self.enterRule(localctx, 16, self.RULE_primaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.boolDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(YAPLGrammarParser.INT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.match(YAPLGrammarParser.STRING_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 108
                self.match(YAPLGrammarParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 109
                self.match(YAPLGrammarParser.NEW)
                self.state = 110
                self.className()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 111
                self.methodName()
                self.state = 112
                self.match(YAPLGrammarParser.LPAREN)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 246977404928) != 0):
                    self.state = 113
                    self.parameterCall()


                self.state = 116
                self.match(YAPLGrammarParser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 118
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
        self.enterRule(localctx, 18, self.RULE_boolDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
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
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.primaryExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.arithmeticExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.methodCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.uniqueMethod()
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
        self.enterRule(localctx, 22, self.RULE_arithmeticExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.primaryExpression()
            self.state = 130
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 131
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
        self.enterRule(localctx, 24, self.RULE_boolExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.primaryExpression()
            self.state = 134
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 135
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
        self.enterRule(localctx, 26, self.RULE_assignExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(YAPLGrammarParser.ASSIGN)
            self.state = 138
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
        self.enterRule(localctx, 28, self.RULE_uniqueMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.methodName()
            self.state = 141
            self.match(YAPLGrammarParser.LPAREN)
            self.state = 142
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
        self.enterRule(localctx, 30, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 144
                self.match(YAPLGrammarParser.LET)


            self.state = 147
            self.match(YAPLGrammarParser.IDENTIFIER)
            self.state = 148
            self.match(YAPLGrammarParser.COLON)
            self.state = 149
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
        self.enterRule(localctx, 32, self.RULE_newVarDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.declaration()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 152
                self.assignExpression()


            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 155
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
        self.enterRule(localctx, 34, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(YAPLGrammarParser.IDENTIFIER)
            self.state = 159
            self.assignExpression()
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 160
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
        self.enterRule(localctx, 36, self.RULE_letDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(YAPLGrammarParser.LET)
            self.state = 164
            self.declaration()
            self.state = 165
            self.match(YAPLGrammarParser.IN)
            self.state = 166
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
        self.enterRule(localctx, 38, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(YAPLGrammarParser.IDENTIFIER)
            self.state = 169
            self.match(YAPLGrammarParser.DOT)
            self.state = 170
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
        self.enterRule(localctx, 40, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 172
                self.assignStatement()
                pass

            elif la_ == 2:
                self.state = 173
                self.expression()
                pass


            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 176
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
        self.enterRule(localctx, 42, self.RULE_assignStatement)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.newVarDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
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
        self.enterRule(localctx, 44, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 183
                self.match(YAPLGrammarParser.LET)


            self.state = 186
            self.match(YAPLGrammarParser.IF)
            self.state = 187
            self.boolExpression()
            self.state = 188
            self.match(YAPLGrammarParser.THEN)
            self.state = 189
            self.statement()
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 190
                    self.match(YAPLGrammarParser.ELSE)
                    self.state = 191
                    self.match(YAPLGrammarParser.IF)
                    self.state = 192
                    self.boolExpression()
                    self.state = 193
                    self.match(YAPLGrammarParser.THEN)
                    self.state = 195
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 194
                        self.match(YAPLGrammarParser.LBRACE)


                    self.state = 197
                    self.statement()
                    self.state = 199
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        self.state = 198
                        self.match(YAPLGrammarParser.RBRACE)

             
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 206
                self.match(YAPLGrammarParser.ELSE)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 207
                    self.match(YAPLGrammarParser.LBRACE)


                self.state = 210
                self.statement()
                self.state = 212
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 211
                    self.match(YAPLGrammarParser.RBRACE)




            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 216
                self.match(YAPLGrammarParser.FI)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 222
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
        self.enterRule(localctx, 46, self.RULE_statementList)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
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
        self.enterRule(localctx, 48, self.RULE_letExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(YAPLGrammarParser.LPAREN)
            self.state = 231
            self.match(YAPLGrammarParser.LET)
            self.state = 232
            self.declaration()
            self.state = 233
            self.match(YAPLGrammarParser.IN)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 234
                self.match(YAPLGrammarParser.LBRACE)
                self.state = 235
                self.statement()
                self.state = 236
                self.match(YAPLGrammarParser.RBRACE)
                self.state = 237
                self.match(YAPLGrammarParser.SEMICOLON)


            self.state = 241
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
        self.enterRule(localctx, 50, self.RULE_defineStatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 243
                self.match(YAPLGrammarParser.LBRACE)


            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 246
                self.statementList()
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 247245856776) != 0)):
                    break

            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 251
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
        self.enterRule(localctx, 52, self.RULE_formalParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
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
        self.enterRule(localctx, 54, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.formalParameter()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 257
                self.match(YAPLGrammarParser.COMMA)
                self.state = 258
                self.formalParameter()
                self.state = 263
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
        self.enterRule(localctx, 56, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.methodName()
            self.state = 265
            self.match(YAPLGrammarParser.LPAREN)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28 or _la==35:
                self.state = 266
                self.parameterList()


            self.state = 269
            self.match(YAPLGrammarParser.RPAREN)
            self.state = 270
            self.match(YAPLGrammarParser.COLON)
            self.state = 271
            self.type_()
            self.state = 272
            self.match(YAPLGrammarParser.LBRACE)
            self.state = 273
            self.defineStatements()
            self.state = 274
            self.match(YAPLGrammarParser.RBRACE)
            self.state = 275
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
        self.enterRule(localctx, 58, self.RULE_feature)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.methodDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





