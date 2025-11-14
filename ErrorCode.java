import java.util.Scanner;
public class TaxCalculator{
   public static void main(String[] args){
   Scanner scanner = new Scanner(System.in);
   double taxRate1 = 0.15;
   double taxRate2 = 0.20;
   double incomeCeiling = 30000;

   for (int i = 1; i <= 3; i++) {

   System.out.print("Enter citizen " + i + "s name: ");
   String name = scanner.nextLine();

   System.out.print("Enter "+ name + "s income: $");
   double income = scanner.nextDouble();
   double tax;   
   if (income <= incomeCeiling); {
   tax = (incomeCeiling * taxRate1 ) + ((income - incomeCeiling) * taxRate2);
   }
   System.out.printf("%s's total tax is: $%,.2f%n%n", name, tax);

   }

  }
}
