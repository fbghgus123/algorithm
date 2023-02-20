// 문제 : https://www.acmicpc.net/problem/2234

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Pos(val row: Int, val col: Int)

val castle = mutableListOf<List<Int>>()
val visited = Array(50) { IntArray(50) }
val sizeList = mutableListOf<Int>()

val dy = arrayOf(0, -1, 0, 1)
val dx = arrayOf(-1, 0, 1, 0)

fun main() {
    val (m, n) = inputIntList()
    var num = 1
    var maximum = 0
    repeat(n) {
        castle.add(inputIntList())
    }

    for (i in 0 until n) {
        for (j in 0 until m) {
            if (visited[i][j] == 0) {
                bfs(Pos(i, j), num, n, m)
                num += 1
            }
        }
    }

    for (i in 0 until n) {
        for (j in 0 until m) {
            for (k in 0 until 4) {
                val ny = i + dy[k]
                val nx = j + dx[k]

                if (ny in 0 until n && nx in 0 until m) {
                    if (visited[i][j] != visited[ny][nx]) {
                        val temp = sizeList[visited[i][j] - 1] + sizeList[visited[ny][nx] - 1]
                        maximum = maxOf(maximum, temp)
                    }
                }
            }
        }
    }

    println(num - 1)
    println(sizeList.max())
    println(maximum)
}

fun bfs(pos: Pos, num: Int, n: Int, m: Int) {
    var size = 1
    val queue = ArrayDeque<Pos>()
    queue.add(pos)
    visited[pos.row][pos.col] = num

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()
        for (i in 0 until 4) {
            if (castle[current.row][current.col] and (1 shl i) > 0) {
                continue
            }

            val ny = current.row + dy[i]
            val nx = current.col + dx[i]

            if (ny in 0 until n && nx in 0 until m) {
                if (visited[ny][nx] == 0) {
                    queue.add(Pos(ny, nx))
                    visited[ny][nx] = num
                    size += 1
                }
            }
        }
    }
    sizeList.add(size)
}