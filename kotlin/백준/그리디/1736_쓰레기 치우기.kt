// 문제 : https://www.acmicpc.net/problem/1736

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Position(val r: Int, val c: Int)

val stack = mutableListOf<Position>()

fun main() {
    val (n, m) = inputIntList()
    repeat(n) { row ->
        val line = inputIntList()

        line.forEachIndexed { col, trash ->
            if (trash == 1) {
                val avail = isAvail(row, col)

                if (avail != -1) {
                    stack[avail] = Position(row, col)
                } else {
                    stack.add(Position(row, col))
                }
            }
        }
    }

    println(stack.size)
}

private fun isAvail(row: Int, col: Int): Int {
    for (index in 0..stack.lastIndex) {
        val pos = stack[index]
        if (row >= pos.r && col >= pos.c) {
            return index
        }
    }
    return -1
}

