// https://www.acmicpc.net/problem/2098

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val w = mutableListOf<List<Int>>()
val dp = Array(1 shl 16) { IntArray(16) { Int.MAX_VALUE } }

class Traveler(val node: Int, val visited: Int, val cost: Int)

fun main() {
    val n = inputInt()
    repeat(n) {
        w.add(inputIntList())
    }

    val queue = ArrayDeque<Traveler>()
    queue.add(Traveler(0, 1, 0))
    var answer = Int.MAX_VALUE

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()

        if (dp[current.visited xor (1 shl current.node)][current.node] < current.cost) {
            continue
        }

        if (current.visited == (1 shl n) - 1 && w[current.node][0] != 0 ) {
            answer = minOf(current.cost + w[current.node][0], answer)
        }

        for (i in 0 until n) {
            if (w[current.node][i] == 0 || (current.visited and (1 shl i)) > 0) {
                continue
            }

            val nextVisited = current.visited or (1 shl i)
            val expectedCost = current.cost + w[current.node][i]

            if (dp[current.visited][i] <= expectedCost) {
                continue
            }

            dp[current.visited][i] = expectedCost
            queue.add(Traveler(i, nextVisited, expectedCost))
        }
    }

    println(answer)
}