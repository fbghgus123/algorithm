// 문제: https://www.acmicpc.net/problem/13164

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Math.ceil
import java.util.PriorityQueue
import kotlin.collections.ArrayDeque

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun main() {
    val (n, k) = inputIntList()
    val heights = inputIntList()

    val differences = mutableListOf<Int>()
    for (i in 0 until heights.lastIndex) {
        differences.add(heights[i+1] - heights[i])
    }

    val answer = differences.sortedDescending().slice((k-1) .. differences.lastIndex).sum()
    println(answer)
}