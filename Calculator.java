class Solution {
  public static int add(int numberone, int numbertwo) {
    return numberone + numbertwo;
  }

  public static int subtract(int numberone, int numbertwo) {
    return numberone - numbertwo; 
  }
  public static int divide(int numberone, int numbertwo) {
    return numberone/numbertwo; 
    }
  public static int multiply(int numberone, int numbertwo) {
    return numberone*numbertwo; 
    }  
  public static void main(String[] args) { 
    while (true) {
System.out.println ("Please select operation(Press q to quit)");
    
    String operation = System.console().readLine();
      String minus_sub = "-";
      
      if (operation.equals(minus_sub)) {
      System.out.println("This is a subtraction operation");
      System.out.println("Please enter the first number");
      String number_one = System.console().readLine();
      System.out.println("Please enter the second number");
      String number_two = System.console().readLine();
      
      System.out.println("The answer is:");
      int result = subtract  (Integer.parseInt(number_one), Integer.parseInt(number_two));
      
      System.out.println(result);
        } else if  (operation.equals("q")) {
          System.exit(0);
        } else if (operation.equals("+")) {
      System.out.println("This is an addition operation");
      System.out.println("Please enter the first number");
      String number_one = System.console().readLine();
      System.out.println("Please enter the second number");
      String number_two = System.console().readLine();
      
      System.out.println("The answer is:");
      int result = add (Integer.parseInt(number_one), Integer.parseInt(number_two));
      
      System.out.println(result);
        } else if (operation.equals("/")) {
      System.out.println("This is a division operation");
      System.out.println("Please enter the first number");
      String number_one = System.console().readLine();
      System.out.println("Please enter the second number");
      String number_two = System.console().readLine();
      
      System.out.println("The answer is:");
      int result = divide(Integer.parseInt(number_one), Integer.parseInt(number_two));
      
      System.out.println(result);
        
      } else if (operation.equals("*")) {
      System.out.println("This is a multiplication operation");
      System.out.println("Please enter the first number");
      String number_one = System.console().readLine();
      System.out.println("Please enter the second number");
      String number_two = System.console().readLine();
      
      System.out.println("The answer is:");
      int result = multiply(Integer.parseInt(number_one), Integer.parseInt(number_two));
      System.out.println(result); 
      } else {
        System.exit(0);
      }     
        System.out.println("Would you like to continue? y or n");
      String desision = System.console().readLine();
        if (desision.equals("n")) {
          System.exit(0);
        }
        if (desision.equals("y")) {
      
        }
      }
     } 
  } 
  
