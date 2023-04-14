// 문제 : https://www.acmicpc.net/problem/3687

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val nums = intArrayOf(6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
val dp = Array(101) { "" }

fun main() {
    dp[2] = "1"
    dp[3] = "7"
    dp[4] = "4"
    dp[5] = "2"
    dp[6] = "6"
    dp[7] = "8"

    for (i in 8 .. 100) {
        var minn =  Long.MAX_VALUE
        for (j in nums.indices) {
            val current = i-nums[j]
            if (current < 2) continue
            minn = minOf(minn, (dp[current] + j.toString()).toLong())
            if (j != 0) {
                minn = minOf(minn, (j.toString() + dp[current]).toLong())
            }
        }
        dp[i] = minn.toString()
    }

    val t = inputInt()
    repeat(t) {
        val num = inputInt()
        var a = num
        var maxx = if (num % 2 == 0) {
            a -= 2
            "1"
        } else {
            a -= 3
            "7"
        }

        repeat(a / 2) {
            maxx += "1"
        }

        println("${dp[num]} $maxx")
    }
}