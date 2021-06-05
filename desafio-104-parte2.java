//2) Agora faca sem utilizar uma terceira variavel temporaria.
//Algoritmo feito em Java porque não consegui achar uma solucao em C   

public class Main
{

    
	public static void main(String[] args) {

		int a=2,b=4;

		System.out.print("Antes da troca: A="+a+" B="+b);

		a = a^b;

	        b = b^a;

	        a = a^b;

	        System.out.print("\nDepois da troca: A="+a+" B="+b);

	}	

}