import java.util.Scanner;

public class Main{
    public static int fatorial(int numero){
	int fator, multiplo, i;
        fator = numero;
        multiplo = 1;
        for (i = 1; i < numero; i++){
	        multiplo *= fator;
	        fator -= 1;
        }
        return multiplo;
    }
	
	public static void main (String[]args){
	    Scanner scan = new Scanner(System.in);
	    int valor;
	    System.out.print("Quer calcular o fatorial de qual número? ");  
	    valor = scan.nextInt();
	    System.out.println ("O fatorial de "+ valor + " é " + fatorial(valor) + ".");
	}
  }
