class Solution:
    def countAndSay(self, n: int) -> str:
        # Base Case: 1
        # 2 = "11", 3 = "21", 4 = "1211", 5 = "111221"
        
        def countCon(num: str) -> str:
            i = 0
            cons = ''
            count = 0
            
            # Count number of consecutives
            while (i < len(num)):
                # Count number of consecutive 1s
                if (num[i] == '1'):
                    # If consecutive
                    if (count >= 0):
                        count += 1
                    else:
                        cons += str(count) + '1'
                        count = 0
                # Count number of consecutive 2s
                else:
                    # If consecutive
                    if (count <= 0):
                        count -= 1
                    else:
                        cons += str(abs(count)) + '2'
                        count = 0
                i += 1
                
            return cons
                    
        # None Case
        if (not n or n <= 0):
            return ''
        # Base Case
        if (n == 1):
            return '1'
        # Recursive Case
        else:
            # Count consecutives
            return countCon(self.countAndSay(n - 1))
            
