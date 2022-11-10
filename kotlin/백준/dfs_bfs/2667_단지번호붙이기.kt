import java.util.*
import kotlin.collections.ArrayList

val br = System.`in`.bufferedReader()
var n: Int = 0
val arr = Array(25) { "" }
val visited = Array(25) { Array(25) { false } }
var answer = ArrayList<Int>()

class Pointer(
    val y: Int,
    val x: Int
)

fun main() {
    n = br.readLine().toInt()

    for (i in 0 until n) {
        arr[i] = br.readLine()
    }
    br.close()

    for (i in 0 until n) {
        for (j in 0 until n) {
            if (!visited[i][j] && arr[i][j] == '1') {
                bfs(Pointer(i, j))
            }
        }
    }

    println(answer.size)
    answer.sorted().forEach {
        println(it)
    }
}

val dy = arrayOf(0, 0, 1, -1)
val dx = arrayOf(1, -1, 0, 0)

fun bfs(p: Pointer) {
    var count = 1
    val queue: Queue<Pointer> = LinkedList()
    visited[p.y][p.x] = true
    queue.add(p)

    while (queue.isNotEmpty()) {
        val cp = queue.poll()
        for (i in 0 .. 3) {
            val cy = cp.y + dy[i]
            val cx = cp.x + dx[i]

            if (0 <= cy && 0 <= cx && cy < n && cx < n) {
                if (arr[cy][cx] == '1' && !visited[cy][cx]) {
                    count++
                    visited[cy][cx] = true
                    queue.add(Pointer(cy, cx))
                }
            }
        }
    }
    answer.add(count)
}