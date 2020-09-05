class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        Ex) "PAYPALISHIRING", 4
        >>> "PIN ALSIG YAH RPI"
             PAYP A L ISHI R I NG
        
        len = 14
        PIN ALSIG YAHR PI
        0 6 12, 1 5 7 11 13, 2 4 8 10, 3 9
        Number of Col = len(s) div (numRows + numRows - 2)
                      = 14 div (4 + 4 - 2)
                      = 14 div 6
                      = 2
        if len(s) mod (numRows + numRows - 2) > numRows - 2
           then Number of Col += 1
        
        P     I    N  ||  0     6       12
        A   L S  I G  ||  1   5 7    11 13
        Y A   H R     ||  2 4   8 10
        P     I       ||  3     9
        '''
        
        zigzag = ""
        # Dictionary of number of characters in each row
        numRowDic = {}
        
        for i in range(numRows):
            # Count number of characters in each row
            mod = 2 * numRows - 2
            # First Row
            if (i == 0):
                colNum = len(s) // mod
                if (len(s) % mod >= numRows - 2):
                    colNum += 1
                
                # Use mod to get the ith row
                for j in range(colNum):
                    zigzag += s[j * mod]
            # Last Row
            elif (i == numRows - 1):
                colNum = 2 * numRowDic[0]
                if (len(s) % mod < i + 1):
                    colNum -= 1
                    
                # Use mod to get the ith row
                for j in range(colNum):
                    zigzag += s[j * mod + i]
            # Middle Row
            else:
                colNum = 2 * numRowDic[0] - 1
                if (len(s) % mod > i + 1):
                    colNum += mod // i
                
                # Use mod to get the ith row
                for j in range(colNum // 2):
                    zigzag += s[j * mod + i]
                    if (j < colNum - 1 or colNum % 2 == 0):
                        zigzag += s[mod - i]
            
            # Add colNum in dictionary
            numRowDic[i] = colNum
            
        return zigzag
