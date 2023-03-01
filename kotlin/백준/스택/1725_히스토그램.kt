// 문제 : https://www.acmicpc.net/problem/1725

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun main() {
    val stack = mutableListOf(0)
    val n = inputInt()
    val arr = IntArray(n+2)
    var answer = 0

    repeat(n) {
        arr[it+1] = inputInt()
    }

    for(i in 1 .. n + 1) {
        while (stack.isNotEmpty() && arr[stack.last()] > arr[i]) {
            val check = stack.removeLast()
            answer = maxOf(answer, arr[check] * (i - stack.last() - 1))
        }
        stack.add(i)
    }
    println(answer)
}