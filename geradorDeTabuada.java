/*Calculadora de Multiplicação*/
import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
	
	Scanner scan = new Scanner(System.in);
	int casa, operacao;
	
	System.out.print("Tabuada. Escolha qual casa você quer consultar.\nDigite o número da casa >> ");
	casa = scan.nextInt();
	System.out.print("Agora escolha a operação:\n1.Adição\n2.Subtração\n3.Multiplicação\n4.Divisão\nEscolha a operação>>");
	operacao = scan.nextInt();
	
	switch (operacao){
	    case 1:
	        for (int i=1; i<=10; i++){
	            System.out.println(casa+" + "+i+" = "+ (casa+i));
	        }
	        break;
	    case 2:
	        for (int i=casa; i<=casa+10; i++){
	            System.out.println(i+" - "+casa+" = "+ (i-casa));
	        }
	        break;
	    case 3:
	        for (int i=1; i<=10; i++){
	            System.out.println(casa+" x "+i+" = "+ (casa*i));
	        }
	        break;
	    case 4:
	        for (int i=casa; i<=casa*10; i+=casa){
	            System.out.println(i+" : "+casa+" = "+ (i/casa));
	        }
	        break;
	}
 }
}
