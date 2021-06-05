/*DESAFIO!!!
Implemente um algoritmo para inverter a ordem de uma string em sua
linguagem de programacao favorita. Nao use funcoes/metodos prontos.*/

#include <stdio.h>
#include <string.h>
int main (){

    char s1[30],s2[30];
    int i=0,j=0,t=0,t2=0;
    fgets(s1,30,stdin);
    t=strlen(s1);
    for(i=t-1;i>=0;i--){
        s2[j]=s1[i];
        j++;
    }
    s2[j]='\0';
    puts(s1);
    puts(s2);

return 0;
}