import java.util.*;
class Calculate
{
	public static void main(String args[])
	{
		double total=0.0;
		double Ritamswastik=0.0;
		double Nilarghadhritiman=0.0;
		double Sourjyadip=0.0;
		Scanner sc=new Scanner(System.in);

		System.out.println("Enter Total Units");
		total=sc.nextDouble();

		System.out.println("Enter Ritam & Swastik's Units");
		Ritamswastik=sc.nextDouble();

		System.out.println("Enter Nil & Dhriti's Units");
		Nilarghadhritiman=sc.nextDouble();

		System.out.println("Enter Sourjyadip's Units");
		Sourjyadip=sc.nextDouble();



		double roomwise=Ritamswastik+Sourjyadip+Nilarghadhritiman;


		double dining=total-roomwise;


		System.out.println("Enter Total Bill Amount");
		double bill=sc.nextDouble();

		double diningbill=(dining/total)*bill;//COMMON PAY


		double sourjyadippaid=((Sourjyadip)/total)*bill;


		double Nilarghadhritimanpaid=(Nilarghadhritiman/total)*bill;


		double Ritamswastikpaid=(Ritamswastik/total)*bill;


		System.out.println("Ritam : Rs "+((Ritamswastikpaid/2)+diningbill/5));
		System.out.println("Swastik: Rs "+((Ritamswastikpaid/2)+diningbill/5));
		System.out.println("Nilargha : Rs "+((Nilarghadhritimanpaid/2)+diningbill/5));
		System.out.println("Dhritiman : Rs "+((Nilarghadhritimanpaid/2)+diningbill/5));
		System.out.println("Sourjyadip : Rs "+((sourjyadippaid)+diningbill/5));

		//INCLUDES COMMON PAY

}
}
