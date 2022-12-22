// 문제 : https://www.acmicpc.net/problem/15681

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }
fun inputInt() = br.readLine().toInt()

val nodeCountArray = IntArray(100001) { 1 }
val line = Array(100001) { mutableListOf<Int>() }

fun main() {
    val (n, r, q) = inputIntList()

    repeat(n - 1) {
        val (u, v) = inputIntList()
        line[u].add(v)
        line[v].add(u)
    }

    checkSubTree(r, 0)

    repeat(q) {
        val value = inputInt()
        println(nodeCountArray[value])
    }
}

fun checkSubTree(current: Int, parent: Int) {
    for (i in line[current]) {
        if (i == parent) {
            continue
        }

        checkSubTree(i, current)
        nodeCountArray[current] += nodeCountArray[i]
    }
}