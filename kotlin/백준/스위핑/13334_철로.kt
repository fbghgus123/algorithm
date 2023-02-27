// 문제 : https://www.acmicpc.net/problem/13334

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Station(val s: Int, val e: Int)
var stations: MutableList<Station> = mutableListOf()

fun main() {
    val n = inputInt()
    var answer = 0
    repeat(n) {
        val (s, e) = inputIntList().sorted()
        stations.add(Station(s, e))
    }
    val budget = inputInt()

    stations = stations.filter { it.e - it.s <= budget }.sortedBy { it.e }.toMutableList()
    val queue = PriorityQueue<Station>() { a, b -> a.s - b.s }

    for (station in stations) {
        val limit = station.e - budget
        queue.add(station)

        while (queue.isNotEmpty() && queue.peek().s < limit) {
            queue.poll()
        }

        answer = maxOf(answer, queue.size)
    }
    println(answer)
}
