%{
#include<stdio.h>
int count = 0;
%}

%%
[a-zA-Z][a-zA-Z0-9]* {count++; printf("valid %d", count);}
.* ECHO;
%%

int yywrap()
{
return 1;
}

int main()
{
yylex();
printf("%d", count);
return 0;
}
