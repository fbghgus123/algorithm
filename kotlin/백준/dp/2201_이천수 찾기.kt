// 문제 : https://www.acmicpc.net/problem/2201

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

data class Info(val value: Long, val zero: Long, val one: Long, val count: Long)

fun main() {
    var k = br.readLine().toLong()
    val dp = mutableListOf(Info(1, 0, 0, 1), Info(2, 0, 1, 2))
    val answer = IntArray(87)

    while (dp.last().value <= 1_000_000_000_000_000_000) {
        val last = dp.last()

        val new = Info (
            last.value + (last.zero * 2) + last.one,
            last.zero + last.one,
            last.zero,
            last.count + 1
        )

        dp.add(new)
    }

    while (k > 0) {
        for (i in dp.indices) {
            if (dp[i].value > k) {
                k -= dp[i - 1].value
                answer[(87 - dp[i - 1].count).toInt()] = 1
                break
            }
        }
    }

    println(answer.joinToString("").trimStart('0'))
}