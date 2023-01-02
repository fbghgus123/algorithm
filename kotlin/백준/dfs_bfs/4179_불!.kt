// 문제 : https://www.acmicpc.net/problem/4179

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }
fun inputStringList() = br.readLine().split("")

val dy = arrayOf(1, 0, -1, 0)
val dx = arrayOf(0, 1, 0, -1)

val maze = mutableListOf<List<String>>()
val fireMaze = Array(1001) { IntArray(1001) { 100000 } }
val visited = Array(1001) { IntArray(1001) }
val fireQueue = ArrayDeque<Position>()
val queue = ArrayDeque<JiHoon>()

class Position(val r: Int, val c: Int)
class JiHoon(val pos: Position, val count: Int)

fun main() {
    val (row, col) = inputIntList()

    repeat(row) { r ->
        val line = inputStringList().filter { it != "" }
        line.forEachIndexed { c, s ->
            if (s == "J") {
                visited[r][c] = 1
                queue.add(JiHoon(Position(r, c), 0))
            }
            if (s == "F") {
                fireQueue.add(Position(r, c))
                fireMaze[r][c] = 0
            }
        }
        maze.add(line)
    }
    spreadFire(row, col)

    val answer = bfs(row, col)
    if (answer == -1) {
        println("IMPOSSIBLE")
    } else {
        println(answer)
    }
}

fun bfs(row: Int, col: Int): Int {
    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()
        val currentPosition = current.pos

        if (currentPosition.r == 0 || currentPosition.c == 0 || currentPosition.r == row-1 || currentPosition.c == col-1) {
            return current.count + 1
        }

        for (i in 0 .. 3) {
            val nr = currentPosition.r + dy[i]
            val nc = currentPosition.c + dx[i]
            if (0 <= nr && 0 <= nc && nr < row && nc < col) {
                if (visited[nr][nc] == 0 && maze[nr][nc] != "#" && fireMaze[nr][nc] > current.count + 1) {
                    visited[nr][nc] = 1
                    queue.add(JiHoon(Position(nr, nc), current.count + 1))
                }
            }
        }
    }
    return -1
}

fun spreadFire(row: Int, col: Int) {
    while (fireQueue.isNotEmpty()) {
        val pos = fireQueue.removeFirst()
        for (i in 0 .. 3) {
            val ny = pos.r + dy[i]
            val nx = pos.c + dx[i]

            if (ny >= 0 && nx >= 0 && ny < row && nx < col) {
                if (maze[ny][nx] != "#" && fireMaze[ny][nx] > fireMaze[pos.r][pos.c] + 1) {
                    fireMaze[ny][nx] = fireMaze[pos.r][pos.c] + 1
                    fireQueue.add(Position(ny, nx))
                }
            }
        }
    }
}