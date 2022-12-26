import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Math.abs

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }
fun inputInt() = br.readLine().toInt()
val nearBy = mutableListOf(intArrayOf())
var peopleNum = listOf(0)

val red = mutableListOf<Int>()
val blue = mutableListOf<Int>()
var answer = 10000

fun main() {
    val n = inputInt()
    peopleNum = peopleNum + inputIntList()
    repeat(n) {
        val near = inputIntList()
        nearBy.add(near.subList(1, near.size).toIntArray())
    }

    btk(n, 1)
    if (answer == 10000) {
        println(-1)
    } else {
        println(answer)
    }
}

fun btk(n: Int, current: Int) {
    if (n < current) {
        if (bfs(n)) {
            val redSum = red.sumOf { peopleNum[it] }
            val blueSum = blue.sumOf { peopleNum[it] }
            val ab = abs(redSum - blueSum)
            if (answer > ab) {
                answer = ab
            }
        }
        return
    }

    red.add(current)
    btk(n, current + 1)
    red.removeLast()

    blue.add(current)
    btk(n, current + 1)
    blue.removeLast()
}

class Place(val color: String, val num: Int)

fun bfs(n: Int): Boolean {
    val visited = IntArray(n + 1)
    val q = ArrayDeque<Place>()
    if (red.isNotEmpty()) {
        q.add(Place("R", red[0]))
        visited[red[0]] = 1
    }
    if (blue.isNotEmpty()) {
        q.add(Place("B", blue[0]))
        visited[blue[0]] = 1
    }

    while (q.isNotEmpty()) {
        val place = q.removeFirst()
        for (i in nearBy[place.num]) {
            if (visited[i] == 0) {
                if (place.color == "R" && i !in red) continue
                if (place.color == "B" && i !in blue) continue
                visited[i] = 1
                q.add(Place(place.color, i))
            }
        }
    }

    for (i in 1..n) {
        if (visited[i] == 0) {
            return false
        }
    }
    return true
}