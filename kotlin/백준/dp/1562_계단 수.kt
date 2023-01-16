// 문제 : https://www.acmicpc.net/problem/1562

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val num = 1_000_000_000
val dp = Array(101) { Array(10) { IntArray(1024) } }

fun main() {
    val n = inputInt()

    for (j in 1 .. 9) {
        dp[1][j][1 shl j] = 1
    }

    for (i in 1 .. 99) {
        for (j in 0 .. 9) {
            for (k in 1 .. 1023) {
                val mask = k or (1 shl j)
                if (j > 0) {
                    dp[i+1][j][mask] += dp[i][j-1][k] % num
                }
                if (j < 9) {
                    dp[i+1][j][mask] += dp[i][j+1][k] % num
                }

                dp[i+1][j][mask] %= num
            }
        }
    }

    var answer = 0
    dp[n].forEach {
        answer += it[1023]
        answer %= num
    }

    println(answer % num)
}