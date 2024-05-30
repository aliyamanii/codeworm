grammar nsc;

program: statements ;

statements: statement (statements statement)* ;

statement: 
    IDENTIFIER EQ expr SEMI
    | BEGIN statements END
    | IF expr THEN statement
    | IF expr THEN statement ELSE statement
    | WHILE expr DO statement
    | FOR IDENTIFIER OF NUMBER TO NUMBER DO statement
    | LOOP IDENTIFIER COLON NUMBER DO statement
    | PRINT IDENTIFIER SEMI
    | PRINT STRINGLITERAL COMMA IDENTIFIER SEMI
    ;

expr: 
    expr binop expr
    | NOT expr
    | LPAR expr RPAR
    | IDENTIFIER
    | NUMBER
    ;

binop: 
    PLUS | MINUS | MULT | DIV | LT | GT | LE | GE | EQEQ | NEQ | POW 
    ;


// Tokens
IDENTIFIER    : [a-zA-Z] [a-zA-Z0-9_]* ;
NUMBER        : [0-9]+ ('.' [0-9]+)? ;
STRINGLITERAL : '"' .*? '"' ;

// Keywords
BEGIN         : 'begin' ;
END           : 'end' ;
IF            : 'if' ;
THEN          : 'then' ;
ELSE          : 'else' ;
WHILE         : 'while' ;
DO            : 'do' ;
FOR           : 'for' ;
OF            : 'of' ;
TO            : 'to' ;
LOOP          : 'loop' ;
PRINT         : 'print' ;
EQ            : '=' ;

// Operators
PLUS          : '+' ;
MINUS         : '-' ;
MULT          : '*' ;
DIV           : '/' ;
LT            : '<' ;
GT            : '>' ;
LE            : '<=' ;
GE            : '>=' ;
EQEQ          : '==' ;
NEQ           : '!=' ;
POW           : '^' ;
NOT           : '!' ;

// Misc
LPAR          : '(' ;
RPAR          : ')' ;
SEMI          : ';' ;
COLON         : ':' ;
COMMA         : ',' ;

// Skip whitespaces and newlines
WS            : [ \t\r\n]+ -> skip ;