%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex();
%}

%token NUMBER

%%

input:
      NUMBER { printf("Number = %d\n", $1); }
    ;

%%

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}

int main() {
    printf("Enter a number: ");
    yyparse();
    return 0;
}