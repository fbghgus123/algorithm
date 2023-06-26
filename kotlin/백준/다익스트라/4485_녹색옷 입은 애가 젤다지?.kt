// 문제 : https://www.acmicpc.net/problem/4485

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Math.ceil
import java.util.PriorityQueue
import kotlin.collections.ArrayDeque

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val dy = intArrayOf(0, 1, 0, -1)
val dx = intArrayOf(1, 0, -1, 0)

class Pos(val row: Int, val col: Int, val value: Int)
var round = 0

fun main() {
    while (true) {
        round += 1

        val n = inputInt()
        if (n == 0) break

        val maze = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            maze[i] = inputIntList().toIntArray()
        }

        val dp = Array(n) { IntArray(n) { Int.MAX_VALUE } }
        val queue = ArrayDeque<Pos>()
        dp[0][0] = maze[0][0]
        queue.add(Pos(0, 0, maze[0][0]))

        while (queue.isNotEmpty()) {
            val current = queue.removeFirst()

            if (dp[current.row][current.col] < current.value) continue

            for (i in 0 until 4) {
                val ny = current.row + dy[i]
                val nx = current.col + dx[i]

                if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue
                if (dp[ny][nx] == Int.MAX_VALUE || dp[ny][nx] > dp[current.row][current.col] + maze[ny][nx]) {
                    dp[ny][nx] = dp[current.row][current.col] + maze[ny][nx]
                    queue.add(Pos(ny, nx, dp[ny][nx]))
                }
            }
        }

        println("Problem $round: ${dp[n-1][n-1]}")
    }
}