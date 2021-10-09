import java.util.Scanner;

public class hello{
  //关键在于问题的分解，将一个问题转化为一样的小问题
  //找到出口，和转化为小问题的方法

	public static void main(String[] args){
		solution(2,'A','B','C');
	}

	public static void solution(int num,char a,char b, char c){
		//汉诺塔：现有num个盘子，三根柱子：要将盘子从a柱移动到c柱，通过b柱
		if(num==1){		//出口
			System.out.println(a+"->"+c);
		}else if(num<1){
			System.out.println("num不对");
		}else{		//递归
			//1.将上边的num-1个盘子看成一个,将他们从a柱->b柱
			solution(num-1,a,c,b);
			//2.再将剩余的一个盘子移动到c柱
			System.out.println(a+"->"+c);
			//3.再将num-1个盘子从b柱->c柱
			solution(num-1,b,a,c);
		}
	}

}

