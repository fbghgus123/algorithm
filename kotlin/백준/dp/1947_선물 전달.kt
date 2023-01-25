// 문제 : https://www.acmicpc.net/problem/1947

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.abs

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val d = LongArray(1000001)

fun main() {
    val n = inputInt()
    d[2] = 1

    for (i in 3 .. n) {
        d[i] = (d[i-1] + d[i-2])  * (i-1)
        d[i] = d[i] % 1_000_000_000
    }
    println(d[n] % 1_000_000_000)
}