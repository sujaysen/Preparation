import java.util.*;
import java.io.*;
public class test1{
	static void printArray(ArrayList<Integer> arr1){
		for(int i=0;i<arr1.size();i++){
			System.out.print(" "+arr1.get(i));
		}
	}
	public static void main(String[] args){
		System.out.println("Welcome to class test1");
		Scanner scn = new Scanner(System.in);
		ArrayList<Integer> arr1 = new ArrayList<Integer>(3);
		for(int i = 0;i<10;i++){
			int data = scn.nextInt();
			arr1.add(data);
		}
		// printing the array
		System.out.println(arr1);
		// remove an element at some index
		arr1.remove(0);
		printArray(arr1);
	}
}
