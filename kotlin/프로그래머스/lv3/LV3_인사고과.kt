// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/152995

data class Person(val att: Int, val est: Int, val isInho: Boolean = false) {
    fun summ() = att + est
}

class Solution {
    fun solution(scores: Array<IntArray>): Int {
        val people = scores.mapIndexed { index, score -> 
            if (index == 0) {
                Person(score[0], score[1], true)
            } else {
                Person(score[0], score[1])
            }
        }
        
        val attOrder = people.sortedWith { a, b ->
            if (a.att == b.att) {
                b.est - a.est
            } else {
                b.att - a.att
            }
        }
        
        
        val stack = mutableListOf<Person>()
        stack.add(attOrder[0])
        
        var prevMaxx = attOrder[0]
        var maxx = attOrder[0]
        
        for (i in 1 .. attOrder.lastIndex) {
            if (maxx.est < attOrder[i].est) {
                prevMaxx = maxx
                maxx = attOrder[i]
            }
            
            if (attOrder[i].att < maxx.att && attOrder[i].est < maxx.est) {
                continue
            }
            
            if (attOrder[i].att < prevMaxx.att && attOrder[i].est < prevMaxx.est) { 
                continue
            }
            
            stack.add(attOrder[i])
        }
        
        val rank = stack.sortedBy { it.att + it.est }.reversed()
        
        var current = 1
        var accumulate = 0
        
        for (i in rank.indices) {
            if (i > 0 && rank[i].summ() != rank[i-1].summ()) {
                current += accumulate
                accumulate = 0
            }
            
            if (rank[i].isInho) {
                return current
            }
            accumulate += 1
        }
    
        return -1
    }
}