//DESAFIO!!!
//As duas não consegui achar uma solução pra resolver
//1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!

//2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.

import java.util.List;

import java.util.ArrayList;

public class Main
{

    
	public static void main(String[] args) {

		int i=0,cont=0;

		List<Integer> lista = new ArrayList<Integer>();

       	 	for(i = 0; i < 10; i++){

            		lista.add(i);

        	}
        
		for(i=0;i<lista.size();i++){

	        	if(lista.get(i)%5 == 0){

                        	System.out.printf("acabo");

	                	break;
            
		    	}
    	
		}
	
	}	

}
