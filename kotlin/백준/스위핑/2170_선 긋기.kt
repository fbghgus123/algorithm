// 문제 : https://www.acmicpc.net/problem/2170

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Line(val start: Int, var end: Int)
val lineList = mutableListOf<Line>()
val stack = ArrayDeque<Line>()
var answer = 0

fun main() {
    val n = inputInt()
    repeat(n) {
        val (s, e) = inputIntList()
        lineList.add(Line(s, e))
    }

    lineList.sortBy { it.start }

    for (line in lineList) {
        if (stack.isNotEmpty() && stack.last().end >= line.start) {
            if (stack.last().end < line.end) {
                stack.last().end = line.end
            }
            continue
        }
        stack.add(line)
    }

    stack.forEach {
        answer += it.end - it.start
    }

    println(answer)
}