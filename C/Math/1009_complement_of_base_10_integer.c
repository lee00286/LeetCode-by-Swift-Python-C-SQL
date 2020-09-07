int bitwiseComplement(int N){
    int powerTwo(int two, int N) {
        // Nearest multiple of 2
        while (two <= N) {
            two *= 2;
        }
        return two;
    }
    
    return powerTwo(2, N) - N - 1;
}
