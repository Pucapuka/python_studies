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
	  System.out.println (fatorial(4));
	}
  }
