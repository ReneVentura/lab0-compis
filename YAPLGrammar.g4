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
STRING: 'String';
SELF: 'SELF_TYPE';
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
type : INT | STRING | className | SELF ; 
variable:  LET ;

parameterCall: expression (COMMA expression)*;  
primaryExpression: INT_LITERAL | STRING_LITERAL | IDENTIFIER | NEW className | methodName LPAREN parameterCall? RPAREN ;

expression: primaryExpression | arithmeticExpression | methodCall;
arithmeticExpression: primaryExpression (MINUS | MULT | PLUS | DIV) primaryExpression;
boolExpression: primaryExpression (EQUALS | LESS_THAN | GREAT_THAN) primaryExpression;
assignExpression: ASSIGN expression;

declaration: LET? IDENTIFIER COLON type;
newVarDeclaration: declaration (assignExpression)? SEMICOLON?;
varDeclaration:IDENTIFIER assignExpression SEMICOLON?;
letDeclaration: LET declaration IN;
methodCall: IDENTIFIER DOT primaryExpression;

statement: assignStatement | expression; 
assignStatement: newVarDeclaration | varDeclaration ;
ifStatement: letDeclaration IF boolExpression THEN statement (ELSE IF boolExpression THEN statement)* (ELSE statement)?; 
statementList: statement | ifStatement;
defineStatements: LBRACE statementList+ RBRACE;


formalParameter: declaration;
parameterList:  formalParameter (COMMA formalParameter)*;
methodDeclaration: methodName LPAREN parameterList? RPAREN COLON type LBRACE defineStatements RBRACE SEMICOLON;
feature: statementList | methodDeclaration;



