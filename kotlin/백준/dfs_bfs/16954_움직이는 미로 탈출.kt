// 문제 : https://www.acmicpc.net/problem/16954

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.ArrayDeque

val br = BufferedReader(InputStreamReader(System.`in`))
fun getStringList() = br.readLine().toList()

val table = Array(8) { CharArray(8) { '.' } }
val visited = Array(8) { IntArray(8) }

fun main() {
    repeat(8) {
        table[it] = getStringList().toCharArray()
    }

    bfs()
    if (visited[0][7] == 1) {
        println(1)
    } else {
        println(0)
    }
}

class Pos(val x: Int, val y: Int)
val dx = arrayOf(-1, 0, 1, -1, 1, -1, 0, 1, 0)
val dy = arrayOf(-1, -1, -1, 0, 0, 1, 1, 1, 0)

fun bfs() {
    val queue = ArrayDeque<Pos>()
    queue.add(Pos(0, 7))

    while(queue.isNotEmpty()) {
        val current = queue.removeFirst()
        for (i in 0..8) {
            val cp = Pos(current.x + dx[i], current.y + dy[i])

            val np = if (cp.y == 0) {
                cp
            } else {
                Pos(cp.x, cp.y - 1)
            }

            if (cp.x < 0 || cp.y < 0 || cp.x >= 8 || cp.y >= 8) {
                continue
            }

            if (isEmpty(cp).not() || isVisited(cp)) {
                continue
            }

            checkVisited(cp)

            if (cp.y != 0 && isEmpty(np).not()) {
                continue
            }

            if (np.y == 0) {
                visited[0][7] = 1
                break
            }

            queue.add(np)
        }
    }
}

fun isEmpty(pos: Pos) = table[pos.y][pos.x] == '.'
fun isVisited(pos: Pos) = visited[pos.y][pos.x] == 1
fun checkVisited(pos: Pos) {
    visited[pos.y][pos.x] = 1
}