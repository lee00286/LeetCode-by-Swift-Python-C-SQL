class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        
        >> readBinaryWatch(0)
        ["0:00"]
        """
        
        # Hours (0-11), Minutes (0-59)
        if (num > 8 or num < 0):
            return []
        elif (num == 0):
            return ["0:00"]
        
        time = []
        
        # Hour
        for i in range(12):
            # Minute
            for j in range (60):
                # Count total '1's from bin(i) and bin(j)
                if (bin(i).count('1') + bin(j).count('1') == num):
                    # Add leading zero to the minute
                    if (j < 10):
                        time.append(str(i) + ":0" + str(j))
                    # No leading zero
                    else:
                        time.append(str(i) + ":" + str(j))
        
        return time
