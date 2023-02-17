// 문제 : https://www.acmicpc.net/problem/1113

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split("").filter { it.isNotBlank() }.map { it.toInt() }

val pool = mutableListOf<List<Int>>()
var visited = Array(50) { BooleanArray(50) }
val depth = Array(50) { IntArray(50) }

val dy = arrayOf(0, 1, 0, -1)
val dx = arrayOf(1, 0, -1, 0)

var n = 0
var m = 0

class Pos(val row: Int, val col: Int)

fun main() {
    val (a ,b) = br.readLine().split(" ").map { it.toInt() }
    n = a
    m = b

    repeat(n) {
        pool.add(inputIntList())
    }

    for (water in 1 .. 9) {
        visited = Array(50) { BooleanArray(50) }
        checkBorder(water)
        checkWater(water)
    }

    var answer = 0
    depth.forEach {
        answer += it.sum()
    }
    println(answer)
}

fun checkWater(water: Int) {
    for (i in 1 until n-1) {
        for (j in 1 until m-1) {
            if (!visited[i][j] && pool[i][j] <= water) {
                bfs(water, Pos(i, j), true)
            }
        }
    }
}

fun checkBorder(water: Int) {
    for (i in 0 until n) {
        if (!visited[i][0] && pool[i][0] <= water) {
            bfs(water, Pos(i, 0))
        }

        if (!visited[i][m-1] && pool[i][m-1] <= water) {
            bfs(water, Pos(i, m-1))
        }
    }

    for (i in 1 until m-1) {
        if (!visited[0][i] && pool[0][i] <= water) {
            bfs(water, Pos(0, i))
        }

        if (!visited[n-1][i] && pool[n-1][i] <= water) {
            bfs(water, Pos(n-1, i))
        }
    }
}

fun bfs(water: Int, start: Pos, waterCheck: Boolean = false) {
    val queue = ArrayDeque<Pos>()
    visited[start.row][start.col] = true
    queue.add(start)

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()

        if (waterCheck) {
            depth[current.row][current.col] += 1
        }

        for (i in 0 until 4) {
            val ny = current.row + dy[i]
            val nx = current.col + dx[i]

            if (0 <= ny && 0 <= nx && ny < n && nx < m) {
                if (!visited[ny][nx] && pool[ny][nx] <= water) {
                    visited[ny][nx] = true
                    queue.add(Pos(ny, nx))
                }
            }
        }
    }
}