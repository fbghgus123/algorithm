// 문제 : https://www.acmicpc.net/problem/12886

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

data class ABC(val data: List<Int>)
val visited = HashMap<ABC, Boolean>()

fun main() {
    val abc = ABC(inputIntList().sorted())

    val queue = ArrayDeque<ABC>()
    queue.add(abc)
    visited[abc] = true

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()
        if(isAllSame(current.data)) {
            println(1)
            return
        }

        listOf<ABC>(ABC(listOf(current.data[0] * 2, current.data[1] - current.data[0], current.data[2]).sorted()),
            ABC(listOf(current.data[0], current.data[1] * 2, current.data[2] - current.data[1]).sorted()),
            ABC(listOf(current.data[0] * 2, current.data[1], current.data[2] - current.data[0]).sorted())
        ).forEach { value ->
            if (!visited.containsKey(value)) {
                queue.add(value)
                visited[value] = true
            }
        }
    }
    println(0)
}

fun isAllSame(list: List<Int>): Boolean {
    for (i in 1 .. list.lastIndex) {
        if (list[i-1] != list[i]) {
            return false
        }
    }
    return true
}