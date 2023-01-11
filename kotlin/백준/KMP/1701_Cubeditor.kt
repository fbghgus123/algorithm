// 문제 : https://www.acmicpc.net/problem/1701

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }



fun findCommon(pattern: String): Int {
    val length = pattern.length

    val p = IntArray(length + 1)

    var pre = 0

    for (target in 1 until length) {
        while (pattern[pre] != pattern[target] && pre > 0) {
            pre = p[pre]
        }

        if (pattern[pre] == pattern[target]) {
            pre += 1
            p[target + 1] = pre
        }
    }
    return p.max()
}

fun main() {
    val string = br.readLine()
    var answer = 0

    for (i in 0 until string.length - 1) {
        val maxx = findCommon(string.substring(i))
        if (answer < maxx) {
            answer = maxx
        }
    }
    println(answer)
}

