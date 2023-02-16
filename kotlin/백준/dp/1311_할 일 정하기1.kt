// 문제 : https://www.acmicpc.net/problem/1311

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val work = mutableListOf<List<Int>>()
val dp = IntArray(1 shl 20) { Int.MAX_VALUE }
var answer = 200001
var n = 0

class Working(val node: Int, val workerVisited: Int, val visited: Int, val amount: Int)

fun main() {
    n = inputInt()
    val queue = ArrayDeque<Working>()

    repeat(n) {
        work.add(inputIntList())
    }

    queue.add(Working(0, 0, 0, 0))
    dp[0] = 0

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()

        if (current.amount > dp[current.visited]) {
            continue
        }

        for (i in 0 until n) {

            if (current.visited and (1 shl i) > 0) {
                continue
            }

            val amount = dp[current.visited] + work[current.node][i]
            val nextWorkerVisited = current.workerVisited or (1 shl current.node)
            val nextVisited = current.visited or (1 shl i)

            if (dp[nextVisited] <= amount) {
                continue
            }

            dp[nextVisited] = amount

            if (nextVisited == (1 shl n) - 1) {
                answer = minOf(amount, answer)
                continue
            }

            var j = 0
            while (true) {
                if (nextWorkerVisited and (1 shl j) > 0) {
                    j += 1
                    continue
                }
                queue.add(Working(j, nextWorkerVisited, nextVisited, amount))
                break
            }
        }
    }

    println(answer)
}