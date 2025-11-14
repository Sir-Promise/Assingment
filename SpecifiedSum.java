import java.util.Scanner;
public class SpecifiedSum{
   public static void main(String[] args) {
   Scanner input = new Scanner(System.in);   

   System.out.print("Enter a targetSum: ");
   int targetSum = input.nextInt();
   int sum = 0;

   while (sum < targetSum){
   System.out.print("Enter number: ");
   sum += input.nextInt();

   System.out.println("Sum: " + sum);
   }
 
   System.out.println("Targetsum reached or exceeded: " + sum);

   }

}
