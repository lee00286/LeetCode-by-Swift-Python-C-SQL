class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Input < (2^31) - 1
        # Input < 2,147,483,647
        
        # (a) Billion
        # (b) Million
        # (c) Thousand
        # (d) Hundred
        # (e) Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety
        # (f) Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen
        # (g) One Two Three Four Five Six Seven Eight Nine
        
        # Function that adds 1-9
        def oneToWord(num):
            if (num == 1):
                return "One"
            elif (num == 2):
                return "Two"
            elif (num == 3):
                return "Three"
            elif (num == 4):
                return "Four"
            elif (num == 5):
                return "Five"
            elif (num == 6):
                return "Six"
            elif (num == 7):
                return "Seven"
            elif (num == 8):
                return "Eight"
            elif (num == 9):
                return "Nine"
            return ""
        
        # Function that adds 1-99
        def tenToWord(num):
            if (num < 10):
                return oneToWord(num)
            if (num == 10):
                return "Ten"
            if (num > 19):
                if (num / 10 == 2):
                    return "Twenty " + oneToWord(num % 10) + " "
                elif (num / 10 == 3):
                    return "Thirty " + oneToWord(num % 10) + " "
                elif (num / 10 == 4):
                    return "Forty " + oneToWord(num % 10) + " "
                elif (num / 10 == 5):
                    return "Fifty " + oneToWord(num % 10) + " "
                elif (num / 10 == 8):
                    return "Eighty " + oneToWord(num % 10) + " "
                else:
                    return oneToWord(num / 10) + "ty " + oneToWord(num % 10) + " "
            if (num == 11):
                return "Eleven "
            if (num == 12):
                return "Twelve "
            if (num == 13):
                return "Thirteen "
            if (num == 15):
                return "Fifteen "
            if (num == 18):
                return "Eighteen "
            return oneToWord(num % 10) + "teen "
            
        # Function that adds 1-999
        def hundredToWord(num):
            if (num < 100):
                return tenToWord(num)
            return tenToWord(num / 100).rstrip() + " Hundred " + tenToWord(num % 100)
        
        # Function that adds 1-9999
        def thousandToWord(num):
            if (num < 1000):
                return hundredToWord(num)
            return hundredToWord(num / 1000).rstrip() + " Thousand " + hundredToWord(num % 1000)
        
        # Function that adds 1-9999999
        def millionToWord(num):
            if (num < 1000000):
                return thousandToWord(num)
            return hundredToWord(num / 1000000).rstrip() + " Million " + thousandToWord(num % 1000000)
        
        # Function that adds 1-9999999999
        def billionToWord(num):
            if (num < 1000000000):
                return millionToWord(num)
            return hundredToWord(num / 1000000000).rstrip() + " Billion " + millionToWord(num % 1000000000)
        
        # If zero
        if (num == 0):
            return "Zero"
        
        # Return the answer
        return billionToWord(num).rstrip()
