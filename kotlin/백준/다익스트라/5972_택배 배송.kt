// 문제 : https://www.acmicpc.net/problem/5972

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.collections.ArrayDeque

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Pos(val place: Int, val cost: Int)

fun main() {
    val (n, m) = inputIntList()
    val graph = Array<MutableList<Pos>>(n + 1) { mutableListOf() }

    repeat(m) {
        val (a, b, c) = inputIntList()
        graph[a].add(Pos(b, c))
        graph[b].add(Pos(a, c))
    }

    val cost = IntArray(n + 1) { -1 }
    cost[1] = 0
    val queue = ArrayDeque<Pos>()
    queue.add(Pos(1, 0))

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()
        for (next in graph[current.place]) {
            if (cost[current.place] < current.cost) {
                continue
            }

            if (cost[next.place] == -1 || cost[current.place] + next.cost < cost[next.place]) {
                cost[next.place] = cost[current.place] + next.cost
                queue.add(Pos(next.place, cost[next.place]))
            }
        }
    }

    println(cost[n])
}