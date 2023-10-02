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
INT: 'Int';
BOOL: 'Bool';
STRING: 'String';
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
//BOOL: 'Bool';
OBJECT: 'Object'; // Fixed typo: changed OBJETCT to OBJECT
TRUE: 'true';
FALSE: 'false';
UNDERSCORE: '_';
FI: 'fi';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
INT_LITERAL: [0-9]+;
STRING_LITERAL: '"' (~["\r\n] | .)*? '"';
WS: [ \t\r\n]+ -> skip;
COMMENT
    : '(*' .*? '*)' -> skip
;

LINE_COMMENT
    : '--' ~[\r\n]* -> skip
;
ERROR: .;

fragment ESC: '\\' ["\\/bfnrt];

// Parser rules
program: classDeclaration+;
classDeclaration: CLASS className (INHERITS classNameParent)? LBRACE feature* RBRACE SEMICOLON;
className: IDENTIFIER;
classNameParent: IDENTIFIER;
methodName: IDENTIFIER;
type: INT {size = 32}
    | STRING {size = 64}
    | className {size = 64}
    | SELF {size = 64}
    | BOOL {size = 1}
    | OBJECT {size = 64};
variable:  LET ;


parameterCall: expression (COMMA expression)*;  
primaryExpression: boolDeclaration |INT_LITERAL | STRING_LITERAL | IDENTIFIER | NEW className | methodName LPAREN parameterCall? RPAREN | SELF;
boolDeclaration: TRUE | FALSE;
expression: primaryExpression | arithmeticExpression | methodCall | uniqueMethod;
arithmeticExpression: primaryExpression (MINUS | MULT | PLUS | DIV) primaryExpression;
boolExpression: primaryExpression (EQUALS | LESS_THAN | GREAT_THAN ) primaryExpression;
assignExpression: ASSIGN expression;
uniqueMethod: methodName LPAREN RPAREN; 
declaration: LET? IDENTIFIER COLON type ;
newVarDeclaration: declaration (assignExpression)? SEMICOLON?;
varDeclaration: IDENTIFIER assignExpression SEMICOLON?;
letDeclaration: LET declaration IN statementList; // Fixed letDeclaration rule
methodCall: IDENTIFIER DOT primaryExpression;
statement: (assignStatement | expression) SEMICOLON?; 
assignStatement: newVarDeclaration | varDeclaration ;
ifStatement: LET? IF boolExpression THEN statement (ELSE IF boolExpression THEN LBRACE? statement RBRACE?)* (ELSE  LBRACE? statement RBRACE?)? FI* SEMICOLON?; // Fixed ifStatement rule
statementList: statement | ifStatement |letExpression;
letExpression: LPAREN LET declaration IN (LBRACE statement RBRACE SEMICOLON)? RPAREN; 
defineStatements: LBRACE? statementList+ RBRACE?;



formalParameter: declaration;
parameterList:  formalParameter (COMMA formalParameter)*;
methodDeclaration: methodName LPAREN parameterList? RPAREN COLON type LBRACE defineStatements RBRACE SEMICOLON;

feature: statementList | methodDeclaration;

// Reglas para código de tres direcciones
threeAddressCode: statement*;

statement: assignment | output;

assignment: IDENTIFIER ASSIGN expression SEMICOLON;

output: OUT expression SEMICOLON;

expression: IDENTIFIER | INT_LITERAL | STRING_LITERAL | arithmeticExpr;

arithmeticExpr: IDENTIFIER ADD_OP expression | INT_LITERAL ADD_OP expression;

ADD_OP: '+' | '-';

//Agregamos reglas para el código de tres direcciones bajo threeAddressCode.
//assignment representa una asignación en el código de tres direcciones (ejemplo: a <- b + 2;).
//output representa una instrucción de salida (ejemplo: out a;).
//expression puede ser una variable, número o cadena en el código de tres direcciones.
//arithmeticExpr permite expresiones aritméticas (ejemplo: a + 3).
//ADD_OP define los operadores de suma y resta (+ y -).
