//DESAFIO!!!



//1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.

//Algoritmo feito em C
    
#include <stdio.h>

#include <string.h>

int main(){
    char x[30],y[30],z[30];

    fgets(x,30,stdin);

    fgets(y,30,stdin);

    for(int i=0;i<=30;i++){

        z[i] = x[i];

        x[i] = y[i];

        y[i] = z[i];

    }
    
    printf("variavel x: %s \nvariavel y: %s",x,y);
    



    return 0;

}
