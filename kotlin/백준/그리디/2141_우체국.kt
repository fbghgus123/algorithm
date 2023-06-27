// 문제 : https://www.acmicpc.net/problem/2141

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Math.ceil
import java.util.PriorityQueue
import kotlin.collections.ArrayDeque
import kotlin.math.absoluteValue

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Town(val place: Int, val people: Long)

fun main() {
    val n = inputInt()

    val area = mutableListOf<Town>()

    repeat(n) {
        val (p, num) = inputIntList()
        area.add(Town(p, num.toLong()))
    }

    area.sortBy { it.place }
    var left = 0L
    var right = area.sumOf { it.people }

    var answer = Town(0, 1000000)
    for (i in area.indices) {
        right -= area[i].people

        val value = maxOf(right - left, left - right) - area[i].people

        if (answer.people > value) {
            answer = Town(area[i].place, value)
        }

        left += area[i].people
    }

    println(answer.place)
}