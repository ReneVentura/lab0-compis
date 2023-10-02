grammar YAPLGrammar;

// Lexer rules
CLASS: 'class';
INHERITS: 'inherits';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
MINUS: '-';
RBRACE: '}';
COLON: ':';
SEMICOLON: ';';
ASSIGN: '<-';
INT: 'Int';
STRING: 'String';
SELF: 'self';
IF: 'if';
THEN: 'then';
ELSE: 'else';
LESS_THAN: '<';
GREAT_THAN: '>';
EQUALS: '=';
PLUS: '+';
MULT: '*';
DIV: '/';
NEW: 'new';
COMMA: ',';
IN: 'in';
DOT: '.';
LET: 'let';
OUT: 'out';
UNDERSCORE: '_';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
INT_LITERAL: [0-9]+;
STRING_LITERAL: '"' (~["\r\n] | .)*? {getText().length() <= 100000} '"';
WS: [ \t\r\n]+ -> skip;
COMMENT: '(*' .*? '*)' -> skip;
ERROR: .;

fragment ESC: '\\' ["\\/bfnrt];

// Parser rules
program: classDeclaration+;
classDeclaration: CLASS className (INHERITS className)? LBRACE feature* RBRACE SEMICOLON;
className: IDENTIFIER;
methodName: IDENTIFIER;

type: INT {size = 32}
    | STRING {size = 64}
    | className {size = 64}
    | SELF {size = 64};

functionDeclaration: methodName LPAREN parameterList? RPAREN COLON type LBRACE defineStatements RBRACE SEMICOLON;


variable:  LET ;

parameterCall: expression (COMMA expression)*;
primaryExpression: INT_LITERAL | STRING_LITERAL | IDENTIFIER | NEW className | methodName LPAREN parameterCall? RPAREN ;

expression: primaryExpression | arithmeticExpression | methodCall;
arithmeticExpression: primaryExpression (MINUS | MULT | PLUS | DIV) primaryExpression;
boolExpression: primaryExpression (EQUALS | LESS_THAN | GREAT_THAN) primaryExpression;
assignExpression: ASSIGN expression;

declaration: LET? IDENTIFIER COLON type;
newVarDeclaration: declaration (assignExpression)? SEMICOLON?;
varDeclaration: IDENTIFIER assignExpression SEMICOLON?;
letDeclaration: LET declaration IN;
methodCall: IDENTIFIER DOT primaryExpression;

statement: assignStatement | expression;
assignStatement: newVarDeclaration | varDeclaration ;
ifStatement: letDeclaration IF boolExpression THEN statement (ELSE IF boolExpression THEN statement)* (ELSE statement)?;
statementList: statement | ifStatement;
defineStatements: LBRACE statementList+ RBRACE;

formalParameter: declaration;
parameterList: formalParameter (COMMA formalParameter)*;
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