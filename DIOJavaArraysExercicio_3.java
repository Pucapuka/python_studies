/*
Faça um Programa que leia 20 números inteiros aleatórios (entre 0 e 100) armazene-os num vetor.
Ao final mostre os números e seus sucessores.
*/

import java.util.Random;

public class DIOJavaArraysExercicio_3{
    
	public static void main(String[] args) {
            Random aleatorio = new Random();
            
            int[] numeroAleatorio = new int[20];
            
            for (int i=0; i<numeroAleatorio.length; i++){
                int numero = aleatorio.nextInt(100);
                numeroAleatorio[i] = numero;
            }
            System.out.print("Numeros Aleatórios: " );
            for (int i=0; i<numeroAleatorio.length; i++){
                System.out.print(numeroAleatorio[i]+", ");
            }
            System.out.print("\nAntecessores: ");
            for (int numero : numeroAleatorio){
                System.out.print(numero-1 + ", ");
            }
            System.out.print("\nSucessores: ");
               for (int numero : numeroAleatorio){
                System.out.print(numero+1+ ", ");
            }
	}
}
