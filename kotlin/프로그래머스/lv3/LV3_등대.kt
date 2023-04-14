// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/133500?language=kotlin

class Solution {
    val graph = Array(100_001) { mutableListOf<Int>() }
    val lightOn = BooleanArray(100_001)
    
    fun preOrder(parent: Int, node: Int) {
        for (child in graph[node]) {
            if (child == parent) continue
            preOrder(node, child)
            
            if (!lightOn[child]) {
                lightOn[node] = true
            }
        }
    }
    
    fun solution(n: Int, lighthouse: Array<IntArray>): Int {
        for ((s, e) in lighthouse) {
            graph[s].add(e)
            graph[e].add(s)
        }
        
        preOrder(0, 1)
        return lightOn.count { it }
    }
}