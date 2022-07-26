import java.time.LocalTime;
import java.time.LocalDate;
public class test {

	int classvar;	
	public test(int x){
		classvar = x;
		System.out.println("This is constructor with value "+x);
	}

	public static void main(String[] args){
		System.out.println("This is the test class");
		test obj = new test(12);
		System.out.println("Class variable is "+obj.classvar);
		LocalTime myObj = LocalTime.now();
		LocalDate mydate = LocalDate.now();
		System.out.println("Current time is "+myObj);
		System.out.println("Current date is "+mydate);
	}

}
