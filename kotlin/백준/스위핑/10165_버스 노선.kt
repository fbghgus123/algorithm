// 문제 : https://www.acmicpc.net/problem/10165

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Line(val num: Int, val s: Int, val e: Int, val count: Int)
val lineList = mutableListOf<Line>()
var stack = ArrayDeque<Line>()

fun main() {
    val n = inputInt()
    val m = inputInt()

    repeat(m) {
        val (s, e) = inputIntList()

        val ts = if (s > e) s else s + n
        val te = e + n

        lineList.add(Line(it + 1, s, e, te - ts))
    }

    lineList.sortWith(compareBy(
        { it.s },
        {-it.count}
    ))

    for (line in lineList) {
        if (stack.isEmpty()) {
            stack.add(line)
            continue
        }

        val top = stack.last()

        if (top.s + top.count < line.s + line.count) {
            stack.add(line)
        }

        if (line.s > line.e) {
            stack = ArrayDeque(stack.filterNot { it.s < it.e && it.e <= line.e })
        }
    }

    println(stack.map { it.num }.sorted().joinToString(" "))
}