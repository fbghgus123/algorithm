// 문제 : https://www.acmicpc.net/problem/3665

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun main() {
    val t = inputInt()
    repeat(t) {
        val n = inputInt()
        val origin = inputIntList()

        val degree = IntArray(n + 1)
        val rank = IntArray(n + 1)
        val graph = Array(n + 1) { BooleanArray(n+1) }
        val m = inputInt()

        origin.forEachIndexed { index, i ->
            rank[i] = index
            degree[i] = index
            origin.subList(index + 1, origin.size).forEach {
                graph[i][it] = true
            }
        }

        repeat(m) {
            val (a, b) = inputIntList()
            graph[a][b] = !graph[a][b]
            graph[b][a] = !graph[b][a]

            if (rank[a] > rank[b]) {
                degree[a] -= 1
                degree[b] += 1
            } else {
                degree[a] += 1
                degree[b] -= 1
            }
        }

        val queue = ArrayDeque<Int>()
        for (i in 1 .. n) {
            if (degree[i] == 0) {
                queue.add(i)
            }
        }

        val answer = mutableListOf<Int>()
        var flag = false
        if (queue.size == 0) {
            flag = true
        }

        while (queue.isNotEmpty()) {
            val current = queue.removeFirst()
            answer.add(current)

            for (i in 1..n) {
                if (graph[current][i]) {
                    degree[i] -= 1

                    if (degree[i] == 0) {
                        queue.add(i)
                    }

                    if (degree[i] < 0) {
                        flag = true
                    }
                }
            }
        }

        if (flag || answer.size != n) {
            println("IMPOSSIBLE")
        } else {
            println(answer.joinToString(" "))
        }
    }
}