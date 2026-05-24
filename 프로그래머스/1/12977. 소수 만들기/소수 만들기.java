class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length;
        
        for(int i=0; i<n-2; i++){
            for(int j=i+1; j<n-1; j++){
                for(int k=j+1; k<n; k++){
                    if(isPrime(nums[i]+nums[j]+nums[k])){
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
    
    boolean isPrime(int n){
        if(n < 2) return false;
        for(int i=2; i<=Math.sqrt(n); i++){
            if(n % i == 0) return false;
        }
        return true;
    }
}