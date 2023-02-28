// 문제 : https://www.acmicpc.net/problem/2239

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
class Pos(val row: Int, val col: Int)

val sdoku = mutableListOf<MutableList<Int>>()
val btkPos = mutableListOf<Pos>()

fun main() {
    repeat(9) { row ->
        val nums = br.readLine().split("").filter { it.isNotEmpty() }.map { it.toInt() }
        for (col in nums.indices) {
            if (nums[col] == 0) {
                btkPos.add(Pos(row, col))
            }
        }
        sdoku.add(nums.toMutableList())
    }

    btk(0)
}

fun btk(i: Int): Boolean {
    if (i > btkPos.lastIndex) {
        sdoku.forEach {
            it.forEach { num -> print(num) }
            println()
        }
        return true
    }

    val current = btkPos[i]
    for (num in 1 .. 9) {
        if (checkRow(num, current) && checkCol(num, current) && checkArea(num, current)) {
            sdoku[current.row][current.col] = num
            if (btk(i + 1)) return true
            sdoku[current.row][current.col] = 0
        }
    }
    return false
}

fun checkRow(num: Int, pos: Pos) = num !in sdoku[pos.row]
fun checkCol(num: Int, pos: Pos): Boolean {
    for (i in 0 until 9) {
        if (sdoku[i][pos.col] == num) {
            return false
        }
    }
    return true
}
fun checkArea(num: Int, pos: Pos): Boolean {
    val startRow = pos.row / 3 * 3
    val startCol = pos.col / 3 * 3

    for (i in startRow until startRow + 3) {
        for (j in startCol until startCol + 3) {
            if (sdoku[i][j] == num) {
                return false
            }
        }
    }
    return true
}