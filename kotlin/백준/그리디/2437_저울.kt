// 문제 : https://www.acmicpc.net/problem/2437

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }
fun inputInt() = br.readLine().toInt()

fun main() {
    val n = inputInt()
    val weights = inputIntList().sorted()
    var sum = 0

    for (i in 0 until n) {
        val weigh = weights[i]

        if (sum + 1 < weigh) {
            break
        }

        sum += weigh
    }
    println(sum + 1)
}