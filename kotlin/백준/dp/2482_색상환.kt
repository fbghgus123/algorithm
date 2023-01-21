// 문제 : https://www.acmicpc.net/problem/2482

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

const val num = 1000000003

fun main() {
    val n = inputInt()
    val k = inputInt()

    val dp = Array(k + 1) { IntArray(n + 1) }
    dp[0][0] = 1
    dp[1][1] = 1

    for (i in 0 .. k) {
        for (j in 1 .. n) {
            dp[i][j] += dp[i][j-1]
            if (j >= 2 && i >= 1) {
                dp[i][j] += dp[i-1][j-2]
            }
            dp[i][j] %= num
        }
    }
    println((dp[k-1][n-3] + dp[k][n-1]) % num)
}