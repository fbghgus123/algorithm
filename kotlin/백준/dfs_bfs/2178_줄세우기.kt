import java.util.*

val br = System.`in`.bufferedReader()
fun getSplitInt() = br.readLine().split(" ").map { it.toInt() }

class Point(
    val y: Int,
    val x: Int
)

fun main() {
    val (n, m) = getSplitInt()
    val arr = Array(n) { "" }

    for (i in IntRange(0, n-1)) {
        arr[i] = br.readLine()
    }

    bfs(n, m, arr)
}

val dy = arrayOf(1, -1, 0, 0)
val dx = arrayOf(0, 0, 1, -1)

fun bfs(n: Int, m: Int, arr: Array<String>) {
    val visited = Array(n) { Array(m) { 0 } }
    val queue: Queue<Point> = LinkedList()

    queue.add(Point(0, 0))
    visited[0][0] = 1

    while(queue.isNotEmpty()) {
        val cp = queue.poll()

        for (i in 0 .. 3) {
            val cy = cp.y + dy[i]
            val cx = cp.x + dx[i]
            if (0 <= cy && 0 <= cx && cy < n && cx < m) {
                if (arr[cy][cx] == '1' && visited[cy][cx] == 0) {
                    visited[cy][cx] = visited[cp.y][cp.x] + 1
                    queue.add(Point(cy, cx))
                }
            }
        }
    }

    println(visited[n-1][m-1])
}
