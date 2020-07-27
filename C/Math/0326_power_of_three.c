bool isPowerOfThree(int n) {
    // Division
    if (n < 1) {
        return false;
    }
              
    while (n % 3 == 0) {
        n /= 3;
    }
        
    return n == 1;
        
    /*
    // Recursion
    if (n < 1) {
        return false;
    }
    else if (n == 1) {
        return true;
    }
    else {
        // Recursion
        return n % 3 == 0 && isPowerOfThree(n / 3);
    }
    */
}
