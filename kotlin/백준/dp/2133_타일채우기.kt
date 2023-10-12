// 문제 : https://www.acmicpc.net/problem/2133

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()

fun main() {
    val n = inputInt()

    val dp = IntArray(31)
    dp[0] = 1
    dp[2] = 3

    for (i in 4 .. 30 step 2) {
        dp[i] = dp[i-2] * 3

        for (j in 4 .. 30 step 2) {
            if (i - j < 0) break
            dp[i] += dp[i-j] * 2
        }
    }
    println(dp[n])
}