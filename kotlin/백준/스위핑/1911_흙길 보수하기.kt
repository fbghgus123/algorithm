// 문제 : https://www.acmicpc.net/problem/1911

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Pos(val s: Int, val e: Int)
val posList = mutableListOf<Pos>()

fun main() {
    val (n, l) = inputIntList()
    repeat(n) {
        val (s, e) = inputIntList()
        posList.add(Pos(s, e))
    }
    posList.sortBy { it.s }

    var count = 0
    var current = 0
    for (pos in posList) {

        // 포함되는 경우
        if (pos.e <= current) {
            continue
        }

        // 아예 다른 경우
        if (pos.s > current) {
            current = pos.s
        }

        while (current < pos.e) {
            count += 1
            current += l
        }
    }
    println(count)
}
