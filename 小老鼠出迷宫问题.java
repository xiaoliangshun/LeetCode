import java.util.Scanner;

public class hello{
	//老鼠出迷宫的问题
	//试探性的递归（回溯）
	//前方的路一片未知，那就闯一闯试一试吧！！！

	public static void main(String[] args){
		int[][] map = new int[8][7];	//画地图
		//画墙
		for(int i=0; i<8; i++){
			map[i][0] = 1;
			map[i][6] = 1;
		}
		for(int i=0; i<7; i++){
			map[0][i] = 1;
			map[7][i] = 1;
		}
		map[3][1] = 1;
		map[3][2] = 1;

		show(map);
		solution(map,1,1);
		show(map);

	}

	public static boolean solution(int[][] map,int i,int j){
		//0表示未尝试，1表示障碍物，2表示可以通过，3表示死路
		// map[6][5]作为终点，进行回溯
		if(map[6][5]==2){ 		//递归出口
			return true;
		}else{
			if(map[i][j]==0){

				map[i][j] = 2;		//假设可以走【思想很重要->试探性的找出路(不试试就不知道能不能行)】
				//往上下左右四个方向走
				if(solution(map,i+1,j)){		
					return true;
				}else if(solution(map,i,j+1)){
					return true;
				}else if(solution(map,i-1,j)){
					return true;
				}else if(solution(map,i,j-1)){
					return true;
				}else{
					map[i][j] = 3;	 //走不通->死路（回溯
					return false;
				}
			}else{			//为1,3不能走，为2不用走了
				return false;
			}
		}
	}

	public static void show(int[][] map){
		for(int i=0; i<map.length; i++){
			for(int j=0; j<map[i].length; j++){
				System.out.print(map[i][j]);
			}
			System.out.println();
		}
	}


}

