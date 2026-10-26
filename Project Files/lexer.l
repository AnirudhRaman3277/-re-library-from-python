%{
#include <stdio.h>
%}

%%
b[a-zA-Z]+    { printf("Matched: %s\n", yytext); }
.|\n            ;
%%

int yywrap()
{
return 1;
}

int main()
{
    yylex();
    return 0;
}