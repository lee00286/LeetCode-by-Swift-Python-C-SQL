class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        frequencies = [0] * 26
        count = 0
        for letter in s:
            index = ord(letter) - ord('a')
            frequencies[index] += 1
            count += 1
        
        for letter in t:
            index = ord(letter) - ord('a')
            if frequencies[index] == 0:
                return False
            frequencies[index] -= 1
            count -= 1
        return count == 0
        
        """ 
        # Method 1: While Loop
        flag = True
        i = 0
        
        # Check length of the string
        if len(s) != len(t):
            flag = False
        
        # Check letters
        while (flag == True) and (i < len(t)):
            # Check t[i] is in s
            if t[i] not in s:
                flag = False
            else:
                a = s.find(t[i])
                if a == 0:
                    s = s[a + 1:]
                else:
                    s = s[:a] + s[a + 1:]
            i += 1
            
        return flag
        """
        
        """ 
        # Method 2: Array Quick Sort
        def quick_sort(array):

            less = []
            equal = []
            greater = []

            if len(array) > 1:
                pivot = array[0]
                for x in array:
                    if x < pivot:
                        less.append(x)
                    elif x == pivot:
                        equal.append(x)
                    elif x > pivot:
                        greater.append(x)
                return quick_sort(less) + equal + quick_sort(greater)
            else:
                return array
        
        array_s = []
        array_t = []
        
        # Check length of the string
        if len(s) != len(t):
            return False
        
        # Make string into array with characters
        for i in range(len(s)):
            array_s.append(s[i])
            array_t.append(t[i])
        
        # Quick Sort
        array_s = quick_sort(array_s)
        array_t = quick_sort(array_t)
        
        return array_s == array_t
        """
