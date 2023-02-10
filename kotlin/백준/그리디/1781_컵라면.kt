// 문제 : https://www.acmicpc.net/problem/1781

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val date = IntArray(200001)
val ramens = mutableListOf<Ramen>()
class Ramen(val deadline: Int, val count: Int)


fun main() {
    val n = inputInt()
    var answer = 0
    date.forEachIndexed { index, i ->
        date[index] = index
    }

    repeat(n) {
        val (d, c) = inputIntList()
        ramens.add(Ramen(d, c))
    }

    val queue = PriorityQueue<Ramen>() { a, b -> b.count - a.count }
        .also { it.addAll(ramens) }

    while (queue.isNotEmpty()) {
        val current = queue.poll()
        val target = find(current.deadline)
        if (target == 0) {
            continue
        }

        join(find(target - 1), target)
        answer += current.count
    }
    println(answer)
}

fun find(a: Int): Int {
    if (a == date[a]) {
        return a
    }
    date[a] = find(date[a])
    return date[a]
}

// b가 더 큼
fun join(a: Int, b: Int) {
    val parent = find(a)
    date[b] = parent
}