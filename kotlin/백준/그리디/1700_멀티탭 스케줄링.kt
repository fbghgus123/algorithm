// 문제 : https://www.acmicpc.net/problem/1700

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val info = Array(101) { mutableListOf<Int>() }
var answer = 0

fun main() {
    val (n, k) = inputIntList()
    val plug = ArrayDeque(inputIntList())

    plug.forEachIndexed { index, i ->
        info[i].add(index)
    }

    val multitab = mutableListOf<Int>()

    while (plug.isNotEmpty()) {
        val target = plug.removeFirst()
        info[target].removeFirst()

        if (target in multitab) {
            continue
        }

        if (multitab.size < n) {
            multitab.add(target)
            continue
        }

        val recentFuture = multitab.map {
            if (info[it].isEmpty()) {
                101
            } else {
                info[it].first()
            }
        }

        val maxx = recentFuture.max()
        val changeTargetIndex = recentFuture.indexOfFirst { it == maxx }
        multitab.removeAt(changeTargetIndex)
        multitab.add(target)
        answer++
    }
    println(answer)
}