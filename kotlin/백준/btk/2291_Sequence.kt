// 문제 : https://www.acmicpc.net/problem/2291

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Math.ceil
import kotlin.collections.ArrayDeque

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun main() {
    val (n, m, k) = inputIntList()
    val answer = IntArray(n)
    var total = 0
    var count = 0

    fun btk(c: Int, prev: Int): Boolean {
        if (n - 1 == c) {
            if (m - total >= prev) {
                count += 1
                if (count == k) {
                    answer[c] = m - total
                    println(answer.joinToString(" "))
                    return true
                }
            }
            return false
        }

        val final = ceil((m - total).toDouble() / (n - c).toDouble()).toInt()

        for (i in prev..final) {
            total += i
            answer[c] = i
            if (btk(c + 1, i)) return true
            total -= i
        }
        return false
    }
    btk(0, 1)
}