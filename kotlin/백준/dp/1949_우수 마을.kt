// 문제 : https://www.acmicpc.net/problem/1949

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.max

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val graph = Array(10001) { mutableListOf<Int>() }
val dp = Array(2) { IntArray(10001) }
val visited = BooleanArray(10001)

lateinit var people: List<Int>

fun main() {
    val n = inputInt()
    people = listOf(0) + inputIntList()

    repeat(n-1) {
        val (a, b) = inputIntList()
        graph[a].add(b)
        graph[b].add(a)
    }
    postOrder(1)
    println(max(dp[1][1], dp[0][1]))
}

fun postOrder(a: Int) {
    visited[a] = true
    for (i in graph[a]) {
        if (visited[i]) {
            continue
        }
        postOrder(i)
    }

    dp[1][a] = graph[a].sumOf { dp[0][it] } + people[a]
    dp[0][a] = graph[a].sumOf { max(dp[0][it], dp[1][it]) }
}