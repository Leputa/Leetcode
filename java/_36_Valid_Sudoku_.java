import java.util.HashSet;

public class _36_Valid_Sudoku_ {
	//如果初始状态不违反规则，数读一定有解
    public boolean isValidSudoku(char[][] board) {
        //HashSet 键可以重复，但值不可以重复
    	//HashMap 键不可以重复，但值可以重复
    	for (int i=0;i<9;i++) {
	    	HashSet<Character>rows=new HashSet<>();
	    	HashSet<Character>cols=new HashSet<>();
	    	HashSet<Character>cube=new HashSet<>();
	    	int rowIndex=3*(i/3);
	    	int colIndex=3*(i%3);  //看了答案，这儿很巧妙，仅仅利用横坐标产生了9个格子的起点
	    	for (int j=0;j<9;j++) {
	    		if(board[i][j]!='.'&&!rows.add(board[i][j]))
	    			return false;
	    		if(board[j][i]!='.'&&!cols.add(board[j][i]))
	    			return false;
	    		if(board[rowIndex + j/3][colIndex + j%3]!='.' && !cube.add(board[rowIndex + j/3][colIndex + j%3]))
	                return false;
	    	}
    	}
    	return true;
    }	
}
