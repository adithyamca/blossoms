import java.util.*;
import java.io.*;
 public class sum
{
public static void main (String args[])
{
int num1,num2,sum;
Scanner input=new Scanner (System.in);
System.out.print("enter the first number");
 num1=input.nextInt();
System.out.print("enter the second number");
 num2=input.nextInt();
System.out.println();
 sum=num1+num2;
System.out.println("sum="+sum);
}
}