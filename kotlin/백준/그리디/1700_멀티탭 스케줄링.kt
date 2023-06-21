import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.collections.ArrayDeque

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun main() {
    val (n, k) = inputIntList()
    val appliances = inputIntList()
    val expected = Array(k + 1) { mutableListOf<Int>() }
    val plug = mutableListOf<Int>()
    var answer = 0

    for (i in 0 until k) {
        expected[appliances[i]].add(i)
    }

    for (i in 0 until k) {
        val current = appliances[i]
        expected[current].removeFirst()

        if (current in plug) {
            continue
        }

        if (plug.size < n) {
            plug.add(current)
            continue
        }

        val order = plug.map { expected[it].firstOrNull() ?: (k + 1) }
        val target = order.indexOf(order.max())
        plug[target] = current
        answer += 1
    }
    println(answer)
}