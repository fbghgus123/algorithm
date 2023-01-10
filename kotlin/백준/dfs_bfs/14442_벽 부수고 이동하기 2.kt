// 문제 : https://www.acmicpc.net/problem/14442

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val field = mutableListOf<List<Int>>()
val visited = Array(11) { Array(1000) { IntArray(1000) } }

val dx = arrayOf(0, 1, 0, -1)
val dy = arrayOf(1, 0, -1, 0)

class Position(val r: Int, val c: Int, val z: Int)

fun main() {
    val (n, m, k) = inputIntList()

    repeat(n) {
        field.add(br.readLine().split("")
            .filter { it.isNotBlank() }
            .map { it.toInt() })
    }

    bfs(n, m, k)

    println(getAnswer(n, m, k))
}

fun getAnswer(n: Int, m: Int, k: Int): Int {
    var answer = 10_000_000

    for (ck in 0 .. k) {
        val value = visited[ck][n - 1][m - 1]
        if (answer > value && value != 0) {
            answer = value
        }
    }

    return if (answer != 10_000_000) {
        answer
    } else {
        -1
    }
}

fun bfs(n: Int, m: Int, k: Int) {
    val queue = ArrayDeque<Position>()
    queue.add(Position(0, 0, 0))
    visited[0][0][0] = 1

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()

        for (i in 0..3) {
            val cy = current.r + dy[i]
            val cx = current.c + dx[i]
            val cz = current.z

            if (0 <= cy && 0 <= cx && cy < n && cx < m) {

                // 가려는 데가 벽인 경우
                if (field[cy][cx] == 1 && cz < k && (visited[cz + 1][cy][cx] == 0 || visited[cz + 1][cy][cx] > visited[cz][current.r][current.c] + 1)) {
                    queue.add(Position(cy, cx, cz + 1))
                    visited[cz + 1][cy][cx] = visited[cz][current.r][current.c] + 1
                }

                // 가려는 데가 벽이 아닌 경우
                if (field[cy][cx] == 0 && (visited[cz][cy][cx] == 0 || visited[cz][cy][cx] > visited[cz][current.r][current.c] + 1)) {
                    queue.add(Position(cy, cx, cz))
                    visited[cz][cy][cx] = visited[cz][current.r][current.c] + 1
                }
            }
        }
    }
}
