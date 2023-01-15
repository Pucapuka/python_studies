
//BINGO
import java.lang.Math;

//class
public class Main {
 
  public static void main(String[] args) {
  int a,b,c,d,e,f,g,h,i;
  
  //generating random numbers
   a = (int)(Math.random()*101);
   b = (int)(Math.random()*101);
   while (b==a){
   b = (int)(Math.random()*101);
   }
   c = (int)(Math.random()*101);
   while (c==a||c==b){
   c = (int)(Math.random()*101);
	}
    d = (int)(Math.random()*101);
    while(d==c||d==b||d==a){
    d = (int)(Math.random()*101);
    }
   e = (int)(Math.random()*101);
   while(e==d||d==c||d==b||d==a){
    e = (int)Math.random()*101;
    }
   f = (int)(Math.random()*101);
   while(f==e||f==d||f==c||f==b||f==a){
    f = (int)Math.random()*101;
    }
   g = (int)(Math.random()*101);
   while(g==f||g==e||g==d||g==c||g==b||g==a){
    g = (int)Math.random()*101;
    }
   h = (int)(Math.random()*101);
   while(h==g||h==f||h==e||h==d||h==c||h==b||h==a){
    e = (int)Math.random()*101;
    }
   i = (int)(Math.random()*101);
   while(i==h||i==g||i==f||i==e||i==d||i==c||i==b||i==a){
    i = (int)Math.random()*101;
    }
   
   //Generating list to assemble the bingos structure 
   int[][] bingoNumbers = {{a,b,c},{d,e,f},{g,h,i}};
   
   //Printing the bingo list with a loop
   
   for (int j=0; j<bingoNumbers.length;j++){
       System.out.println("");
   	for (int k=0; k<bingoNumbers[j].length; k++){
    	System.out.print(bingoNumbers[j][k]+" ");
    }
   }
  }
}
