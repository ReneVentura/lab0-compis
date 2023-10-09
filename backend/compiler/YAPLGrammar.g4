grammar YAPLGrammar;

// Lexer rules
CLASS: 'class';
INHERITS: 'inherits';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
COLON: ':';
SEMICOLON: ';';
ASSIGN: '<-';
INT: 'Int' SIZES?; // Define SIZES here for Int
BOOL: 'Bool' SIZES?; // Define SIZES here for Bool
STRING: 'String' SIZES?; // Define SIZES here for String
SELF: 'self';
IF: 'if';
THEN: 'then';
ELSE: 'else';
LESS_THAN: '<';
GREAT_THAN: '>';
EQUALS: '=';
MINUS: '-';
PLUS: '+';
MULT: '*';
DIV: '/';
NEW: 'new';
COMMA: ',';
IN: 'in';
DOT: '.';
LET: 'let';
OUT: 'out';
OBJECT: 'Object';
TRUE: 'true';
FALSE: 'false';
UNDERSCORE: '_';
FI: 'fi';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
INT_LITERAL: [0-9]+;
STRING_LITERAL: '"' (~["\r\n] | .)*? '"';
SIZES: 'SIZES'; // Define SIZES as a lexer rule
WS: [ \t\r\n]+ -> skip;
COMMENT: '(*' .*? '*)' -> skip;
LINE_COMMENT: '--' ~[\r\n]* -> skip;
ERROR: .;

fragment ESC: '\\' ["\\/bfnrt];

// Parser rules
program: classDeclaration+;
classDeclaration: CLASS className (INHERITS classNameParent)? LBRACE feature* RBRACE SEMICOLON;
className: IDENTIFIER;
classNameParent: IDENTIFIER;
methodName: IDENTIFIER;
type: INT | STRING | className | SELF | BOOL | OBJECT ;
variable: LET ;
operator:MINUS | MULT | PLUS | DIV;
parameterCall: expression (COMMA expression)*;
primaryExpression: boolDeclaration | INT_LITERAL | STRING_LITERAL | IDENTIFIER | NEW className | methodName LPAREN parameterCall? RPAREN | SELF ;
boolDeclaration: TRUE | FALSE;
expression: primaryExpression | arithmeticExpression | methodCall | uniqueMethod | assignStatement;
arithmeticExpression: primaryExpression (MINUS primaryExpression | MULT primaryExpression | PLUS primaryExpression | DIV primaryExpression)*;
boolExpression: primaryExpression (EQUALS | LESS_THAN | GREAT_THAN ) primaryExpression;
assignExpression: ASSIGN expression;
uniqueMethod: methodName LPAREN RPAREN;
declaration: LET? IDENTIFIER COLON type ;
newVarDeclaration: LET? IDENTIFIER COLON type (assignExpression)? SEMICOLON?;
varDeclaration: IDENTIFIER assignExpression SEMICOLON?;
letDeclaration: LET declaration IN statementList;
methodCall: IDENTIFIER DOT primaryExpression;
statement:  expression SEMICOLON?;
assignStatement: newVarDeclaration | varDeclaration ;
ifStatement: LET? IF boolExpression THEN statement (ELSE IF boolExpression THEN LBRACE? statement RBRACE?)* (ELSE  LBRACE? statement RBRACE?)? FI* SEMICOLON?;
statementList: statement | ifStatement |letExpression;
letExpression: LPAREN LET declaration IN (LBRACE statement RBRACE SEMICOLON)? RPAREN;
defineStatements: LBRACE? statementList+ RBRACE?;
formalParameter: declaration;
parameterList:  formalParameter (COMMA formalParameter)*;
methodDeclaration: methodName LPAREN parameterList? RPAREN COLON type LBRACE defineStatements RBRACE SEMICOLON;
feature: statementList | methodDeclaration;
