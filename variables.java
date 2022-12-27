/*Variable types in Java are the same as in python, C or JS. One detail that you need to pay attention to is that they are
declared as in C language, and "string" has its first letter capitalized --> "String" and flot needs an 'f' after the number --> float weight = 61,8f*/

public class Main{
	public static void main(String[]args){

//Working with String
    
    String name = "Paulo";
    System.out.println(name);
 
//Working with integer (int)
    
    int number = 10;
    System.out.println(number);
    
    // assigning a new value to a previously assigned variable:
    
    number = 20;
    System.out.print("New Value: ");
    System.out.print(number);

    //I can also declare the variable and assign a value later:
    
    int myNum;
    myNum = 15;
    System.out.println(myNum);
    
    //if I want to make an unchangeable variable, I put 'final' before it:
    
    final int myNumber = 15;
    myNumber = 20; // will generate an error
    System.out.println(myNumber);
    
    //I can also display two informations concatenated using "+" between them. e.g.:
    
    String name = "Paulo ";  //notice that I left a space before after the name so it could work when putting it together with the surname
    String surname = "Lima";
    String fullName = name + surname;
    System.out.println("Hello, " + name + surname);   //can typed this way
                                                        //or
    System.out.println("Hello, " + fullName);       //this way
    
    
    //Declaring multiple variables: I can separate them in different lines using ";" 
    
    int x = 5;
    int y = 6;
    int z = 50;
    System.out.println(x + y + z);
    
    //or on the same line using ","
   
    int a = 5, b = 6, c= 50;
    System.out.println(a + b + c);



    }

}
