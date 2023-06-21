// 문제: https://www.acmicpc.net/problem/2240

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.collections.ArrayDeque

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun main() {
    val (t, w) = inputIntList()
    val dp = Array(w + 2) { IntArray(t + 1) }
    val zaDoo = mutableListOf(0)
    repeat(t) {
        zaDoo.add(inputInt())
    }
    var answer = 0

    for (i in 1 .. w + 1) {
        for (j in 1 .. t) {
            val match = if (minOf(j, i-1) % 2 + 1 == zaDoo[j]) 1 else 0
            dp[i][j] = maxOf(dp[i-1][j-1], dp[i][j-1]) + match
        }
        answer = maxOf(answer, dp[i][t])
    }
    println(answer)
}