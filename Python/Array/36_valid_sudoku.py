class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # Check validity of each row
        def isValidRow(board):
            for row in board:
                # Check validity
                if (not isValidCheck(row)):
                    return False
            return True
           
        # Check validity of each column
        def isValidCol(board):            
            for col in zip(*board):
                # Check validity
                if (not isValidCheck(col)):
                    return False
            return True
        
        # Check validity of 3 x 3 sub-boxes
        def isValidBox(board):
            for i in (0,3,6):
                for j in (0,3,6):
                    box = [
                        board[i][j], board[i + 1][j], board[i + 2][j],
                        board[i][j + 1], board[i + 1][j + 1], board[i + 2][j + 1],
                        board[i][j + 2], board[i + 1][j + 2], board[i + 2][j + 2]
                        ]
                    
                    # Check validity
                    if (not isValidCheck(box)):
                        return False
            return True
        
        # Check validity of an array
        def isValidCheck(sudokuArray):
            arrayCopyOne = []
            arrayCopyTwo = []
            
            # Remove all blanks in sudokuArray
            for i in range (9):
                if (sudokuArray[i] != '.'):
                    arrayCopyOne.append(sudokuArray[i])
                
            # Remove all duplicates in arrayCopyOne
            arrayCopyTwo = list(dict.fromkeys(arrayCopyOne))
            
            return (len(arrayCopyOne) == len(arrayCopyTwo))
        
        # Validity check
        return isValidRow(board) and isValidCol(board) and isValidBox(board)
    
