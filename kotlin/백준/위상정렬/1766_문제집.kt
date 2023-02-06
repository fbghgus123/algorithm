// 문제 : https://www.acmicpc.net/problem/1766

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val degree = IntArray(32001)
val graph = Array(32001) { mutableListOf<Int>() }

fun main() {
    val (n, m) = inputIntList()

    repeat(m) {
        val (b, a) = inputIntList()
        degree[a] += 1
        graph[b].add(a)
    }

    val queue = PriorityQueue<Int>()
    val answer = ArrayDeque<Int>()

    for (i in 1 .. n) {
        if (degree[i] == 0) {
            queue.add(i)
        }
    }

    while (queue.isNotEmpty()) {
        val current = queue.poll()
        answer.add(current)

        for (i in graph[current]) {
            degree[i] -= 1
            if (degree[i] == 0) {
                queue.add(i)
            }
        }
    }

    println(answer.joinToString(" "))
}