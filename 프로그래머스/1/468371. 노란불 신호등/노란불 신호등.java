class Solution {
    public int solution(int[][] signals) {
        int n = signals.length;
        int[] cycles = new int[n];
        
        for (int i = 0; i < n; i++) {
            cycles[i] = signals[i][0] + signals[i][1] + signals[i][2];
        }
        
        long lcm = 1;
        for (int i = 0; i < n; i++) {
            lcm = lcm(lcm, cycles[i]);
        }
        
        for (long t = 1; t <= lcm; t++) {
            boolean allYellow = true;
            for (int i = 0; i < n; i++) {
                int pos = (int)((t - 1) % cycles[i]) + 1; // 현재 주기 내 위치 (1부터 시작)
                int G = signals[i][0];
                int Y = signals[i][1];
                if (pos <= G || pos > G + Y) {  // 노란불 구간: G+1 ~ G+Y
                    allYellow = false;
                    break;
                }
            }
            if (allYellow) return (int)t;
        }
        
        return -1;
    }
    
    private long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }
    
    private long lcm(long a, long b) {
        return a / gcd(a, b) * b;
    }
}