// 문제 : https://www.acmicpc.net/problem/1132

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.max
import kotlin.math.pow

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val alphaValue = HashMap<Char, Long>()
val isNotFirst = mutableSetOf<Char>()

fun main() {
    val n = inputInt()
    arrayOf('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J').forEach {
        alphaValue[it] = 0L
    }

    val inputs = mutableListOf<String>()
    repeat(n) {
        val str = br!!.readLine()
        inputs.add(str)
        isNotFirst.add(str[0])
        str.forEachIndexed { index, c ->
            alphaValue[c] = alphaValue[c]!! + 10.0.pow(str.length - index).toLong()
        }
    }

    val ordering = alphaValue.entries.sortedBy { it.value }.map { it.key }.toMutableList()
    var targetIndex = 0
    for (i in ordering) {
        if (i !in isNotFirst) {
            break
        }
        targetIndex++
    }

    val converter = HashMap<Char, Int>()
    (listOf(ordering.removeAt(targetIndex)) + ordering).forEachIndexed { index, c ->
        converter[c] = index
    }

    println(
        inputs.map {
            it.map { char -> converter[char] }.joinToString("").toLong()
        }.sum()
    )
}