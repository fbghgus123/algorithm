// 문제 : https://www.acmicpc.net/problem/15732

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.collections.ArrayDeque

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Rule(val start: Int, val end: Int, val distance: Int) {
    fun getCount (mid: Int): Long {
        if (mid < start) return 0
        val final = minOf(end, mid).toLong()
        return (final - start) / distance + 1
    }
}

fun main() {
    val (n, k, d) = inputIntList()
    val rules = Array<Rule>(k) { Rule(0, 0, 0) }
    repeat(k) {
        val (s, e, dis) = inputIntList()
        rules[it] = Rule(s, e, dis)
    }

    fun checkCount(mid: Int): Long {
        var count = 0L
        rules.forEach {
            count += it.getCount(mid)
        }
        return count
    }

    var left = 1
    var right = n
    var answer = 1000000

    while (left <= right) {
        val mid = (left + right) / 2

        if (checkCount(mid) >= d) {
            answer = minOf(mid, answer)
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    println(answer)
}