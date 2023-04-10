// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/131702

class Solution {
    
    fun solution(clockHands: Array<IntArray>): Int {
        var answer = 1000000000
        val n = clockHands.size
        var upCount = IntArray(n)
        var tmpClock = Array(n) { IntArray(n) }
        
        fun reset() {
            tmpClock = Array(n) { IntArray(n) }
            for (i in 0 until n) {
                for (j in 0 until n) {
                    tmpClock[i][j] = clockHands[i][j]
                }
            }
        }
        
        fun rotate(row: Int, col: Int, count: Int) {
            val rotatePos = arrayOf(
                intArrayOf(row, col),
                intArrayOf(row + 1, col),
                intArrayOf(row, col + 1),
                intArrayOf(row - 1, col),
                intArrayOf(row, col - 1),
            )
            
            rotatePos.forEach { pos ->
                if (pos[0] >= 0 && pos[1] >= 0 && pos[0] < n && pos[1] < n) {
                    tmpClock[pos[0]][pos[1]] += count
                }
            }
        }
        
        fun isOk(): Boolean {
            for (col in 0 until n) {
                if (tmpClock[n-1][col] % 4 != 0) {
                    return false
                }
            }
            return true
        }
        
        fun checkCase() {
            var tmpCount = 0
            
            // 맨 윗열 세팅
            for (col in 0 until n) {
                rotate(0, col, upCount[col])
                tmpCount += upCount[col]
            }
            
            // 아랫열들 세팅
            for (row in 1 until n) {
                for (col in 0 until n) {
                    if (tmpClock[row-1][col] % 4 != 0) {
                        val count = 4 - (tmpClock[row-1][col] % 4)
                        tmpCount += count
                        rotate(row, col, count)
                    }
                }
            }
            
            // 맨 아랫 열 확인
            if (isOk()) {
                answer = minOf(answer, tmpCount)                
            }
        }
        
        fun dfs(index: Int) {
            if (index == n) {
                reset()
                checkCase()
                return
            }
            
            for (i in 0 .. 3) {
                upCount[index] = i
                dfs(index + 1)
            }
        }
        
        dfs(0)
        
        return answer
    }
}