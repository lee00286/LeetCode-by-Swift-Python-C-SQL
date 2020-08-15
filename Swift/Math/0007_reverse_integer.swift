class Solution {
    func reverse(_ x: Int) -> Int {
        reverse_x = 0
        neg = 1
        zero_middle = 0
        
        # Negative case
        if (x < 0):
            neg = -1
            x = -x

        while (x != 0):
            mod = x % 10
            if (zero_middle != 0):
                reverse_x = reverse_x * 100 + mod
                zero_middle = 0
            elif (mod != 0):
                reverse_x = reverse_x * 10 + mod
            else:
                zero_middle += 1
            x = x // 10
        
        if (reverse_x > 2147483649) or (reverse_x < -2147483649):
            return 0
        return neg * reverse_x
    }
}
