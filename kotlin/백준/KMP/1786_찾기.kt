// 문제 : https://www.acmicpc.net/problem/1786

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun findCommon(pattern: String): IntArray {
    val length = pattern.length

    val pi = IntArray(length + 1)

    var pre = 0

    for (target in 1 until length) {
        while (pattern[pre] != pattern[target] && pre > 0) {
            pre = pi[pre]
        }

        if (pattern[pre] == pattern[target]) {
            pre += 1
            pi[target + 1] = pre
        }
    }
    return pi
}

fun main() {
    val t = br.readLine()
    val p = br.readLine()

    val answer = mutableListOf<Int>()

    val pi = findCommon(p)

    var s = 0
    var common = 0
    while (s + p.length <= t.length ) {

        if (t[s + common] == p[common]) {
            common++
        } else {
            if (common == 0) {
                s++
            }
            else {
                s += common - pi[common]
                common = 0
            }
        }

        if (common >= p.length) {
            answer.add(s + 1)
            s += common - pi[common]
            common = pi[common]
        }
    }

    println(answer.size)
    println(answer.joinToString(" "))
}