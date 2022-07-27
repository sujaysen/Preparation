import java.util.*;
public class sujay {
	static int factorial(String name,int num){
		System.out.println("Calculate factorial here with name "+name);
		int fact = 1;
		for(int i =1;i<num;i++){
			fact = fact*i;
		}
		return fact;
	}
	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		String str = scn.nextLine();
		System.out.println("Entered string is "+str);
		int inp = scn.nextInt();
		System.out.println("Entered integer is "+inp);
		System.out.println("Hello sujay!");
		sujay myobj = new sujay();
		int result = myobj.factorial("sujay",inp);
		System.out.println("Factorial = "+result);
		System.out.println("I'm learning java");
		// this is for comment
		String w = "welcome";
		System.out.println("sujay "+w);
		int res = Math.max(10,100);
		System.out.println("Maximum is "+res);
		int x = 1;
		if(x==0){
			System.out.println("If block executed");
		}else if(x==1){
			System.out.println("Else if block executed");
		}else{
			System.out.println("Else block executed");
		}

		int day = 4;
		switch (day){
			case 1:
				System.out.println("Monday");
				break;
			case 2:
				System.out.println("Tuesday");
				break;
			case 3:
				System.out.println("Wednesday");
				break;
			case 4:
				System.out.println("Thursday");
				break;
			case 5:
				System.out.println("Friday");
				break;
			case 6:
				System.out.println("Saturday");
				break;
			case 7:
				System.out.println("Sunday");
				break;
		}

		int i = 0;
		while(i<5){
			System.out.println(i);
			i++;
		}

		for(int j = 0;j<5;j++){
			System.out.println("For loop checking");
		}

		String[] cars = {"maruti","tata","hunday","honda","renault"};
		for (String car:cars){
			System.out.println("Car name is "+car);
		}

		int [] myint = {1,2,3,4,56,7,8};
		for (int k =0;k<myint.length;k++){
			System.out.println("Array num is "+myint[k]);
		}

		int [][] twodim = {{1,2,3},{11,22,33}};
		for(int ii = 0;ii<twodim.length;++ii){
			for(int jj=0;jj<twodim[ii].length;++jj){
				System.out.println("Two Dim "+twodim[ii][jj]);
			}
		}
	}
}
