// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/178870

class Solution {
    fun solution(sequence: IntArray, k: Int): IntArray {
        var left = 0
        var total = 0
        var answer = intArrayOf(0, 1000001)
        
        for (right in sequence.indices) {
            total += sequence[right]
            
            while(total > k && left <= right) {
                total -= sequence[left]
                left += 1
            }
            
            if (total == k && answer[1] - answer[0] > right - left) {
                answer = intArrayOf(left, right)
            }
        }
        
        return answer
    }
}