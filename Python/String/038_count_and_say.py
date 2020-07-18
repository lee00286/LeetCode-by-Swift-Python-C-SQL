class Solution:
    def countAndSay(self, n: int) -> str:
        # Base Case: 1
        # 2 = "11", 3 = "21", 4 = "1211", 5 = "111221"
        
        def countCon(num: str) -> str:
            i = 0
            cons = ""
            latest = ""
            count = 0
            
            # Count number of consecutives
            for char in num:
                # First consecutive
                if (latest == ""):
                    latest = char
                    count += 1
                else:
                    # If consecutive
                    if (latest == char):
                        count += 1
                    # If not consecutive
                    else:
                        cons += str(count) + latest
                        latest = ""
                        count = 0
            
            cons += str(count) + latest
            
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
            
