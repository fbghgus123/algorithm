// 문제: https://school.programmers.co.kr/learn/courses/30/lessons/138475
import kotlin.math.*
import java.util.PriorityQueue

class Node(val number: Int, val count: Int)

class Solution {
    fun solution(e: Int, starts: IntArray): IntArray {
        val answer = IntArray(e+1)
        val counts = IntArray(e+1)
           

        for (i in 1 .. e) {
            var j = i
            while (j <= e) {
                counts[j] += 1
                j += i
            }
        }

        
        var target = Node(0, 0)
        
        for (i in e downTo 1) {
            if (target.count <= counts[i]) {
                target = Node(i, counts[i])
            }
            
            answer[i] = target.number
        }
        
        return starts.map { answer[it] }.toIntArray()
    }
}