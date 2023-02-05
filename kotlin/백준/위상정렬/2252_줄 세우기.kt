// 문제 : https://www.acmicpc.net/problem/2252

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val degree = IntArray(32001)
val graph = Array(32001) { mutableListOf<Int>() }

fun main() {
    val (n, m) = inputIntList()
    repeat(m) {
        val (a, b) = inputIntList()

        degree[a] += 1
        graph[b].add(a)
    }

    val queue = ArrayDeque<Int>()
    val answer = mutableListOf<Int>()

    for (i in 1 .. n) {
        if (degree[i] == 0) {
            queue.add(i)
        }
    }

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()
        answer.add(current)

        for (next in graph[current]) {
            degree[next] -= 1
            if (degree[next] == 0) {
                queue.add(next)
            }
        }
    }

    println(answer.reversed().joinToString(" "))
}