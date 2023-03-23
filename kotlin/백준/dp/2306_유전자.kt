// 문제: https://www.acmicpc.net/problem/2306

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

var str = ""
val dp = Array(501) { IntArray(501) { -1 } }

fun recur(left: Int, right: Int): Int {
    if (left >= right) {
        return 0
    }

    if (dp[left][right] != -1) {
        return dp[left][right]
    }

    var result = -1
    for (k in left until right) {
        result = maxOf(result, recur(left, k) + recur(k+1, right))
    }

    if ((str[left] == 'g' && str[right] == 'c') || (str[left] == 'a' && str[right] == 't')) {
        result = maxOf(result, recur(left + 1, right - 1) + 2)
    }

    dp[left][right] = result
    return dp[left][right]
}

fun main() {
    str = br.readLine()!!
    println(recur(0, str.lastIndex))
}