// 문제 : https://www.acmicpc.net/problem/10217

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Ticket(val v: Int, val c: Int, val d: Int)
data class Path(val destination: Int, val totalCost: Int, val totalTime: Int)

fun main() {
    val t = inputInt()

    repeat(t) {
        val (n, m, k) = inputIntList()
        val paths = Array(n + 1) { mutableListOf<Ticket>() }
        val dp = Array(n + 1) { IntArray(m + 1) { Int.MAX_VALUE } }
        dp[1][0] = 0

        repeat(k) {
            val (u, v, c, d) = inputIntList()
            paths[u].add(Ticket(v, c, d))
        }

        val queue = PriorityQueue<Path> { a, b -> a.totalTime - b.totalTime}
        queue.add(Path(1, 0, 0))

        while (queue.isNotEmpty()) {
            val current = queue.poll()
            if (current.totalTime > dp[current.destination][current.totalCost]) {
                continue
            }

            for (ticket in paths[current.destination]) {
                val nextCost = current.totalCost + ticket.c
                val nextTime = dp[current.destination][current.totalCost] + ticket.d

                if (nextCost <= m && dp[ticket.v][nextCost] > nextTime) {
                    dp[ticket.v][nextCost] = nextTime
                    queue.add(Path(ticket.v, nextCost, nextTime))
                }
            }
        }

        val answer = dp[n].min()
        if (answer == Int.MAX_VALUE) {
            println("Poor KCM")
        } else {
            println(answer)
        }
    }
}