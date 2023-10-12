// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181186

class Solution {
    fun solution(n: Int): Int {
        val dp = LongArray(100001)
        
        dp[0] = 1L
        dp[1] = 1L
        dp[2] = 3L
        dp[3] = 10L
        
        for (i in 4 .. n) {
            dp[i] = (dp[i-1] * 1 + dp[i-2] * 2 + dp[i-3] * 5) % 1_000_000_007
            
            for (j in 4 .. n step 3) {
                if (i - j < 0) break
                dp[i] += dp[i-j] * 2
            }
            
            for (j in 5 .. n step 3) {
                if (i - j < 0) break
                dp[i] += dp[i-j] * 2
            }
            
            for (j in 6 .. n step 3) {
                if (i - j < 0) break
                dp[i] += dp[i-j] * 4
            }
            
            dp[i] = dp[i] % 1_000_000_007
        }
        
        return (dp[n] % 1_000_000_007).toInt()
    }
}