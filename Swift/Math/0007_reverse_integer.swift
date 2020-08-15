class Solution {
    func reverse(_ x: Int) -> Int {
        var reverse_x = 0
        var neg = 1
        var zero_middle = 0
        
        // Negative case
        if (x < 0) {
            neg = -1
        }
        var y = abs(x)

        while (y != 0) {
            var mod = y % 10
            if (zero_middle != 0) {
                reverse_x = reverse_x * 100 + mod
                zero_middle = 0
            }
            else if (mod != 0) {
                reverse_x = reverse_x * 10 + mod
            }
            else {
                zero_middle += 1
            }
            y = y / 10
        }
        
        if ((reverse_x > 2147483649) || (reverse_x < -2147483649)) {
            return 0
        }
        
        return neg * reverse_x
    }
}
