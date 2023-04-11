// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/132266
class Solution {
    fun solution(n: Int, roads: Array<IntArray>, sources: IntArray, destination: Int): IntArray {
        
        val path = Array(n+1) { mutableListOf<Int>() }
        val distance = IntArray(n+1) { -1 }
        
        for (road in roads) {
            path[road[0]].add(road[1])
            path[road[1]].add(road[0])
        }
        
        val queue = ArrayDeque<Int>()
        queue.add(destination)
        distance[destination] = 0
        
        while(!queue.isEmpty()) {
            val current = queue.removeFirst()
            
            for (next in path[current]) {
                if (distance[next] == -1 || distance[next] > distance[current] + 1) {
                    distance[next] = distance[current] + 1
                    queue.add(next)
                }
            }
        }
        
        return sources.map { distance[it] }.toIntArray()
    }
}