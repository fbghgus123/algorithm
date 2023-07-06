// 문제: https://www.acmicpc.net/problem/12869

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }
val dp = Array(61) { Array(61) { IntArray(61) } }

fun dfs(a: Int, b: Int, c: Int, count: Int) {
    val a = maxOf(0, a)
    val b = maxOf(0, b)
    val c = maxOf(0, c)

    if (dp[a][b][c] in 1..count) return
    dp[a][b][c] = count

    if (a > 0) dfs(a-9, b-3, c-1, count + 1)
    if (a > 0) dfs(a-9, b-1, c-3, count + 1)
    if (b > 0) dfs(a-3, b-9, c-1, count + 1)
    if (b > 0) dfs(a-1, b-9, c-3, count + 1)
    if (c > 0) dfs(a-3, b-1, c-9, count + 1)
    if (c > 0) dfs(a-1, b-3, c-9, count + 1)
}

fun main() {
    val n = inputInt()
    val scv = inputIntList().toMutableList()

    for (i in 0 until 3 - n) {
        scv.add(0)
    }

    dfs(scv[0], scv[1], scv[2], 0)
    println(dp[0][0][0])
}