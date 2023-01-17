// 문제 : https://www.acmicpc.net/problem/2011

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))

const val num = 1000000

fun main() {
    val s = br.readLine()!!
    val length = s.length

    val dp = IntArray(length + 1)
    dp[0] = 1

    if (s[0] == '0') {
        println(0)
        return
    }

    for (i in 0 until length) {
        val char = s[i]

        if (!char.isDigit()) {
            println(0)
            return
        }

        if (char == '0') {
            if (s[i-1].digitToInt() in 1..2) {
                dp[i+1] = dp[i-1]
                continue
            }
            println(0)
            return
        }

        if (i > 0 && "${s[i-1]}${char}".toInt() <= 26 && s[i-1].digitToInt() != 0) {
            dp[i+1] = (dp[i] + dp[i-1]) % num
            continue
        }

        dp[i+1] = dp[i]
    }
    println(dp[length] % num)
}