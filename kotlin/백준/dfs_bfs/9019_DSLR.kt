// 문제 : https://www.acmicpc.net/problem/9019

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.collections.ArrayDeque

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun d(value: Int) = value * 2 % 10000
fun s(value: Int) = if (value != 0 ) value - 1 else 9999
fun l(value: Int) = (value % 1000) * 10 + (value / 1000)
fun r(value: Int) = (value % 10) * 1000 + (value / 10)

class Log(val value: Int, val prev: Int)
val strings = listOf("D", "S", "L", "R")

fun main() {
    val t = inputInt()
    repeat(t) {
        val (s, e) = inputIntList()
        val visited = Array(10000) { "뀨" }

        val queue = ArrayDeque<Log>()
        visited[s] = ""
        queue.add(Log(s, 0))

        while (queue.isNotEmpty()) {
            if (visited[e] != "뀨") {
                println(visited[e])
                break
            }

            val current = queue.removeFirst()

            if (visited[current.value] != "뀨" && current.prev > visited[current.value].length) {
                continue
            }

            val d = d(current.value)
            val s = s(current.value)
            val l = l(current.value)
            val r = r(current.value)

            val result = listOf(d, s, l, r)

            for (i in 0 .. 3) {
                val target = result[i]
                if (visited[target] == "뀨" || visited[target].length > current.prev + 1) {
                    if (visited[target] == "뀨") visited[target] = ""
                    visited[target] = visited[current.value] + strings[i]
                    queue.add(Log(target, visited[target].length))
                }
            }
        }
    }
}