// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/92343

class SW(val sheep: Int, val wolf: Int) {
    fun avail() = sheep - wolf > 1
}

class Solution {
    val graph = Array(18) { mutableListOf<Int>() }
    
    fun getStatus(visited: Int, info: IntArray): SW {
        var sheep = 0
        var wolf = 0
        
        for (i in 0 .. 17) {
            if (visited and (1 shl i) > 0) {
                if (info[i] == 0) {
                    sheep += 1
                } else {
                    wolf += 1
                }
            }
        }
        return SW(sheep, wolf)
    }
    
    fun getAvailSearch(visited: Int): List<Int> {
        var visited = visited
        var avail = mutableListOf<Int>()
        
        for (i in 0 .. 17) {
            if (visited and (1 shl i) > 0) {
                for (edge in graph[i]) {
                    if (visited and (1 shl edge) == 0) {
                        avail.add(edge)
                    }
                }
                
            }
        }
        return avail
    }
    
    fun solution(info: IntArray, edges: Array<IntArray>): Int {
        var answer = 1
        
        edges.forEach {
            graph[it[0]].add(it[1])
        }
        
        val queue = ArrayDeque<Int>()
        queue.add(1)
        
        while (queue.isNotEmpty()) {
            val current = queue.removeFirst()
            val availSearch = getAvailSearch(current)
            val currentStatus = getStatus(current, info)
            
            for (edge in availSearch) {
                if (info[edge] == 1 && !currentStatus.avail()) {
                    continue
                }
                val next = current or (1 shl edge)
                queue.add(next)
                answer = maxOf(answer, getStatus(next, info).sheep)
            }
        }
        
        return answer
    }
}