/*
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido
e continue pedindo
até que o usuário informe um valor válido.
*/

import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		float nota;
	    System.out.println("Digite a nota do aluno: ");
	    nota = scan.nextFloat();
	    
	    while (nota > 10 || nota < 0){
		    System.out.println("Digite uma nota válida");
	        nota = scan.nextFloat();
	        
	    }
	}
}
