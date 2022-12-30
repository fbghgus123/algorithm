// 문제 : https://www.acmicpc.net/problem/24337

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }
fun inputInt() = br.readLine().toInt()

fun main() {
    val (total, left, right) = inputIntList()

    if (total < left + right - 1) {
        println(-1)
        return
    }

    val maxHeight = max(left, right)
    val leftBuilding = (1..left - 1).toList()
    val rightBuilding = (1..right - 1).reversed().toList()

    val temp = leftBuilding + listOf(maxHeight) + rightBuilding

    val answer = if (left + right - 1 < total) {
        if (left == 1) {
            listOf(maxHeight) + Array(total - (left + right - 1)) { 1 }.toList() + rightBuilding
        } else {
            Array(total - (left + right - 1)) { 1 }.toList() + temp
        }
    } else {
        temp
    }

    println(answer.joinToString(" "))
}