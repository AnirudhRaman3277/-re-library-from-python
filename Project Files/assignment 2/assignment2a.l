%{
#include <stdio.h>
%}

%%

"int"|"float"|"char"|"double"|"if"|"else"|"for"|"while"|"return"|"void"
    { printf("KEYWORD       : %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]*
    { printf("IDENTIFIER    : %s\n", yytext); }

[0-9]+\.[0-9]+
    { printf("FLOAT         : %s\n", yytext); }

[0-9]+
    { printf("NUMBER        : %s\n", yytext); }

"=="|"!="|"<="|">="|"++"|"--"|"&&"|"||"
    { printf("OPERATOR      : %s\n", yytext); }

"+"|"-"|"*"|"/"|"="|"<"|">"|"%"
    { printf("OPERATOR      : %s\n", yytext); }

";"|","|"("|")"|"{"|"}"|"["|"]"
    { printf("SPECIAL SYMBOL: %s\n", yytext); }

[ \t\n]+
    { /* ignore whitespace */ }

.
    { printf("UNKNOWN       : %s\n", yytext); }

%%

int main()
{
    printf("Enter your program:\n");
    printf("Press Ctrl+Z and Enter when finished.\n\n");

    yylex();

    return 0;
}

int yywrap()
{
    return 1;
}