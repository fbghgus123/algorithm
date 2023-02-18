// 문제 : https://www.acmicpc.net/problem/14658

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Pos(val row: Int, val col: Int)

val fallingStars = mutableListOf<Pos>()
val startPos = mutableListOf<Pos>()

var rowSet = setOf<Int>()
var colSet = setOf<Int>()

fun main() {
    val (n, m, l, k) = inputIntList()
    repeat(k) {
        val (y, x) = inputIntList()
        fallingStars.add(Pos(y, x))
        rowSet = rowSet.plus(y)
        colSet = colSet.plus(x)
    }

    val minRow = n - l
    val minCol = m - l

    rowSet.forEach { row ->
        colSet.forEach { col ->
            startPos.add(Pos(minOf(row, minRow), minOf(col, minCol)))
        }
    }

    var answer = 100
    startPos.forEach {
        val up = it.row
        val down = it.row + l
        val left = it.col
        val right = it.col + l

        var temp = k
        fallingStars.forEach { it ->
            if (it.row in up .. down && it.col in left .. right) {
                temp -= 1
            }
        }
        answer = minOf(answer, temp)
    }
    println(answer)
}