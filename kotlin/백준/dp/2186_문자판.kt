// 문제 : https://www.acmicpc.net/problem/2186

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

var string = ""
val board = mutableListOf<String>()

val visited = Array(81) { Array(101) { IntArray(101) } }

class Position(val r: Int, val c: Int, val findIndex: Int)

val dy = arrayOf(0, 1, 0, -1)
val dx = arrayOf(1, 0, -1, 0)

fun main() {
    val (n, m, k) = inputIntList()
    repeat(n) {
        board.add(br.readLine())
    }

    string = br.readLine()

    bfs(n, m, k)
}

fun bfs(n: Int, m: Int, k: Int) {
    val queue = ArrayDeque<Position>()
    var answer = 0

    for (i in 0 until n) {
        for (j in 0 until m) {

            if (board[i][j] == string[0]) {
                queue.add(Position(i, j, 1))
                visited[0][i][j] = 1
            }

        }
    }

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()

        for (amount in 1..k) {
            for (i in 0..3) {
                val cy = current.r + dy[i] * amount
                val cx = current.c + dx[i] * amount

                if (0 <= cy && 0 <= cx && cy < n && cx < m) {
                    if (board[cy][cx] == string[current.findIndex]) {
                        if (visited[current.findIndex][cy][cx] == 0 && current.findIndex != string.lastIndex) {
                            queue.add(Position(cy, cx, current.findIndex + 1))
                        }
                        visited[current.findIndex][cy][cx] += visited[current.findIndex - 1][current.r][current.c]
                    }
                }
            }
        }
    }

    for (i in 0 until n) {
        for (j in 0 until m) {

            if (board[i][j] == string.last()) {
                answer += visited[string.lastIndex][i][j]
            }

        }
    }

    println(answer)
}