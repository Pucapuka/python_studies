public class Main{
	public static void main (String[] args){
    	String name = "Paulo ";
        String surname = "Lima";
        String fullName = name + surname;
        
        System.out.println("My name is " + fullName+".");
    //I can also use concatenation this way:
        System.out.println("My full name is " + name.concat(surname) + ".");
        System.out.println("My full name has " + fullName.length() + " characters.");
        System.out.println("When it\'s written with uppercase latters: " + fullName.toUpperCase());
        System.out.println("When it\'s written with lowercase letters: " + fullName.toLowerCase());
        System.out.println("And where can I find this name\'s initials? Simple! They\'re found respectively on the indexes " + fullName.indexOf(name)+ " and " + fullName.indexOf(surname)+".");
    
    }
}
