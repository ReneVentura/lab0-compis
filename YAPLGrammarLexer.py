# Generated from YAPLGrammar.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,38,244,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,
        0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,
        1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,
        1,24,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,28,1,28,1,28,
        1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,31,1,31,5,31,187,8,31,10,31,
        12,31,190,9,31,1,32,4,32,193,8,32,11,32,12,32,194,1,33,4,33,198,
        8,33,11,33,12,33,199,1,33,1,33,4,33,204,8,33,11,33,12,33,205,1,34,
        1,34,1,34,5,34,211,8,34,10,34,12,34,214,9,34,1,34,1,34,1,34,1,35,
        4,35,220,8,35,11,35,12,35,221,1,35,1,35,1,36,1,36,1,36,1,36,5,36,
        230,8,36,10,36,12,36,233,9,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,
        1,38,1,38,1,38,2,212,231,0,39,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,
        17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,
        39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,
        61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,0,1,0,6,3,0,65,
        90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,1,0,48,57,3,0,10,10,
        13,13,34,34,3,0,9,10,13,13,32,32,8,0,34,34,47,47,92,92,98,98,102,
        102,110,110,114,114,116,116,250,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,
        0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,
        0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,
        0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,
        0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,
        0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,
        0,1,79,1,0,0,0,3,85,1,0,0,0,5,94,1,0,0,0,7,96,1,0,0,0,9,98,1,0,0,
        0,11,100,1,0,0,0,13,102,1,0,0,0,15,104,1,0,0,0,17,106,1,0,0,0,19,
        109,1,0,0,0,21,113,1,0,0,0,23,118,1,0,0,0,25,124,1,0,0,0,27,131,
        1,0,0,0,29,136,1,0,0,0,31,139,1,0,0,0,33,144,1,0,0,0,35,149,1,0,
        0,0,37,151,1,0,0,0,39,153,1,0,0,0,41,155,1,0,0,0,43,157,1,0,0,0,
        45,159,1,0,0,0,47,161,1,0,0,0,49,163,1,0,0,0,51,167,1,0,0,0,53,169,
        1,0,0,0,55,172,1,0,0,0,57,174,1,0,0,0,59,178,1,0,0,0,61,182,1,0,
        0,0,63,184,1,0,0,0,65,192,1,0,0,0,67,197,1,0,0,0,69,207,1,0,0,0,
        71,219,1,0,0,0,73,225,1,0,0,0,75,239,1,0,0,0,77,241,1,0,0,0,79,80,
        5,99,0,0,80,81,5,108,0,0,81,82,5,97,0,0,82,83,5,115,0,0,83,84,5,
        115,0,0,84,2,1,0,0,0,85,86,5,105,0,0,86,87,5,110,0,0,87,88,5,104,
        0,0,88,89,5,101,0,0,89,90,5,114,0,0,90,91,5,105,0,0,91,92,5,116,
        0,0,92,93,5,115,0,0,93,4,1,0,0,0,94,95,5,40,0,0,95,6,1,0,0,0,96,
        97,5,41,0,0,97,8,1,0,0,0,98,99,5,123,0,0,99,10,1,0,0,0,100,101,5,
        125,0,0,101,12,1,0,0,0,102,103,5,58,0,0,103,14,1,0,0,0,104,105,5,
        59,0,0,105,16,1,0,0,0,106,107,5,60,0,0,107,108,5,45,0,0,108,18,1,
        0,0,0,109,110,5,73,0,0,110,111,5,110,0,0,111,112,5,116,0,0,112,20,
        1,0,0,0,113,114,5,66,0,0,114,115,5,111,0,0,115,116,5,111,0,0,116,
        117,5,108,0,0,117,22,1,0,0,0,118,119,5,70,0,0,119,120,5,108,0,0,
        120,121,5,111,0,0,121,122,5,97,0,0,122,123,5,116,0,0,123,24,1,0,
        0,0,124,125,5,83,0,0,125,126,5,116,0,0,126,127,5,114,0,0,127,128,
        5,105,0,0,128,129,5,110,0,0,129,130,5,103,0,0,130,26,1,0,0,0,131,
        132,5,115,0,0,132,133,5,101,0,0,133,134,5,108,0,0,134,135,5,102,
        0,0,135,28,1,0,0,0,136,137,5,105,0,0,137,138,5,102,0,0,138,30,1,
        0,0,0,139,140,5,116,0,0,140,141,5,104,0,0,141,142,5,101,0,0,142,
        143,5,110,0,0,143,32,1,0,0,0,144,145,5,101,0,0,145,146,5,108,0,0,
        146,147,5,115,0,0,147,148,5,101,0,0,148,34,1,0,0,0,149,150,5,60,
        0,0,150,36,1,0,0,0,151,152,5,62,0,0,152,38,1,0,0,0,153,154,5,61,
        0,0,154,40,1,0,0,0,155,156,5,45,0,0,156,42,1,0,0,0,157,158,5,43,
        0,0,158,44,1,0,0,0,159,160,5,42,0,0,160,46,1,0,0,0,161,162,5,47,
        0,0,162,48,1,0,0,0,163,164,5,110,0,0,164,165,5,101,0,0,165,166,5,
        119,0,0,166,50,1,0,0,0,167,168,5,44,0,0,168,52,1,0,0,0,169,170,5,
        105,0,0,170,171,5,110,0,0,171,54,1,0,0,0,172,173,5,46,0,0,173,56,
        1,0,0,0,174,175,5,108,0,0,175,176,5,101,0,0,176,177,5,116,0,0,177,
        58,1,0,0,0,178,179,5,111,0,0,179,180,5,117,0,0,180,181,5,116,0,0,
        181,60,1,0,0,0,182,183,5,95,0,0,183,62,1,0,0,0,184,188,7,0,0,0,185,
        187,7,1,0,0,186,185,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,
        189,1,0,0,0,189,64,1,0,0,0,190,188,1,0,0,0,191,193,7,2,0,0,192,191,
        1,0,0,0,193,194,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,66,1,
        0,0,0,196,198,7,2,0,0,197,196,1,0,0,0,198,199,1,0,0,0,199,197,1,
        0,0,0,199,200,1,0,0,0,200,201,1,0,0,0,201,203,5,46,0,0,202,204,7,
        2,0,0,203,202,1,0,0,0,204,205,1,0,0,0,205,203,1,0,0,0,205,206,1,
        0,0,0,206,68,1,0,0,0,207,212,5,34,0,0,208,211,8,3,0,0,209,211,9,
        0,0,0,210,208,1,0,0,0,210,209,1,0,0,0,211,214,1,0,0,0,212,213,1,
        0,0,0,212,210,1,0,0,0,213,215,1,0,0,0,214,212,1,0,0,0,215,216,6,
        34,0,0,216,217,5,34,0,0,217,70,1,0,0,0,218,220,7,4,0,0,219,218,1,
        0,0,0,220,221,1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,223,1,
        0,0,0,223,224,6,35,1,0,224,72,1,0,0,0,225,226,5,40,0,0,226,227,5,
        42,0,0,227,231,1,0,0,0,228,230,9,0,0,0,229,228,1,0,0,0,230,233,1,
        0,0,0,231,232,1,0,0,0,231,229,1,0,0,0,232,234,1,0,0,0,233,231,1,
        0,0,0,234,235,5,42,0,0,235,236,5,41,0,0,236,237,1,0,0,0,237,238,
        6,36,1,0,238,74,1,0,0,0,239,240,9,0,0,0,240,76,1,0,0,0,241,242,5,
        92,0,0,242,243,7,5,0,0,243,78,1,0,0,0,9,0,188,194,199,205,210,212,
        221,231,2,1,34,0,6,0,0
    ]

class YAPLGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CLASS = 1
    INHERITS = 2
    LPAREN = 3
    RPAREN = 4
    LBRACE = 5
    RBRACE = 6
    COLON = 7
    SEMICOLON = 8
    ASSIGN = 9
    INT = 10
    BOOL = 11
    FLOAT = 12
    STRING = 13
    SELF = 14
    IF = 15
    THEN = 16
    ELSE = 17
    LESS_THAN = 18
    GREAT_THAN = 19
    EQUALS = 20
    MINUS = 21
    PLUS = 22
    MULT = 23
    DIV = 24
    NEW = 25
    COMMA = 26
    IN = 27
    DOT = 28
    LET = 29
    OUT = 30
    UNDERSCORE = 31
    IDENTIFIER = 32
    INT_LITERAL = 33
    FLOAT_LITERAL = 34
    STRING_LITERAL = 35
    WS = 36
    COMMENT = 37
    ERROR = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'inherits'", "'('", "')'", "'{'", "'}'", "':'", 
            "';'", "'<-'", "'Int'", "'Bool'", "'Float'", "'String'", "'self'", 
            "'if'", "'then'", "'else'", "'<'", "'>'", "'='", "'-'", "'+'", 
            "'*'", "'/'", "'new'", "','", "'in'", "'.'", "'let'", "'out'", 
            "'_'" ]

    symbolicNames = [ "<INVALID>",
            "CLASS", "INHERITS", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
            "COLON", "SEMICOLON", "ASSIGN", "INT", "BOOL", "FLOAT", "STRING", 
            "SELF", "IF", "THEN", "ELSE", "LESS_THAN", "GREAT_THAN", "EQUALS", 
            "MINUS", "PLUS", "MULT", "DIV", "NEW", "COMMA", "IN", "DOT", 
            "LET", "OUT", "UNDERSCORE", "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", 
            "STRING_LITERAL", "WS", "COMMENT", "ERROR" ]

    ruleNames = [ "CLASS", "INHERITS", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "COLON", "SEMICOLON", "ASSIGN", "INT", "BOOL", "FLOAT", 
                  "STRING", "SELF", "IF", "THEN", "ELSE", "LESS_THAN", "GREAT_THAN", 
                  "EQUALS", "MINUS", "PLUS", "MULT", "DIV", "NEW", "COMMA", 
                  "IN", "DOT", "LET", "OUT", "UNDERSCORE", "IDENTIFIER", 
                  "INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", "WS", 
                  "COMMENT", "ERROR", "ESC" ]

    grammarFileName = "YAPLGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[34] = self.STRING_LITERAL_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            getText().length() <= 100000
     


