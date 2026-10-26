%{
#include<stdio.h>
int count = 0;
%}

%%
[0-9]+  			                 {printf("Integer Identified!\n");}
[0-9]+\.?[0-9]*[fF]?|\.[0-9]*[fF]?   {printf("Float Identified!\n");}
[a-zA-Z][a-zA-Z0-9]*    	         {printf("Identifier found!\n");}
\+|\*|\/|\-|\=|\=\=  	             {printf("Operator found!\n");}
.* ECHO;
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
