// 코드 : https://www.acmicpc.net/problem/2533

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.min

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val dp = Array(2) { IntArray(1_000_001) }
val visited = BooleanArray(1_000_001)
val graph = Array(1_000_001) { mutableListOf<Int>() }

fun main() {
    val n = inputInt()
    repeat(n-1) {
        val (u, v) = inputIntList()
        graph[u].add(v)
        graph[v].add(u)
    }
    postOrder(1)
    println(min(dp[0][1], dp[1][1]))
}

fun postOrder(a: Int) {
    visited[a] = true
    for (i in graph[a]) {
        if (visited[i]) {
            continue
        }
        postOrder(i)
    }
    dp[0][a] = graph[a].sumOf { dp[1][it] }
    dp[1][a] = graph[a].sumOf { min(dp[0][it], dp[1][it]) } + 1
}