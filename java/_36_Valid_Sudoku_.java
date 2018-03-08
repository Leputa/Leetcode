import java.util.HashSet;

public class _36_Valid_Sudoku_ {
	//�����ʼ״̬��Υ����������һ���н�
    public boolean isValidSudoku(char[][] board) {
        //HashSet �������ظ�����ֵ�������ظ�
    	//HashMap ���������ظ�����ֵ�����ظ�
    	for (int i=0;i<9;i++) {
	    	HashSet<Character>rows=new HashSet<>();
	    	HashSet<Character>cols=new HashSet<>();
	    	HashSet<Character>cube=new HashSet<>();
	    	int rowIndex=3*(i/3);
	    	int colIndex=3*(i%3);  //���˴𰸣����������������ú����������9�����ӵ����
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
