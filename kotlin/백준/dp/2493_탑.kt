// 문제 : https://www.acmicpc.net/problem/2493

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

lateinit var top: List<Int>
val answer = IntArray(500001)

fun main() {
    val n = inputInt()
    top = listOf(0) + inputIntList()

    for (i in 1 .. n) {
        checkTop(i, i-1)
    }

    println(answer.slice(1 .. n).joinToString(" "))
}

fun checkTop(current: Int, target: Int) {
    if (top[current] < top[target] || target == 0) {
        answer[current] = target
        return
    }

    checkTop(current, answer[target])
}