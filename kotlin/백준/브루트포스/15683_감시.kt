// 문제 : https://www.acmicpc.net/problem/15683

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val dy = arrayOf(0, 1, 0, -1) // 우 하 좌 상
val dx = arrayOf(1, 0, -1, 0)
var answer = 64

val office = mutableListOf<IntArray>()
val watching = Array(8) { IntArray(8) }
val cctvList = mutableListOf<CCTV>()
val directions = mapOf<Int, Array<IntArray>>(
    1 to arrayOf(
        intArrayOf(0),
        intArrayOf(1),
        intArrayOf(2),
        intArrayOf(3)
    ),
    2 to arrayOf(
        intArrayOf(0, 2),
        intArrayOf(1, 3)
    ),
    3 to arrayOf(
        intArrayOf(0, 3),
        intArrayOf(0, 1),
        intArrayOf(1, 2),
        intArrayOf(2, 3)
    ),
    4 to arrayOf(
        intArrayOf(0, 1, 2),
        intArrayOf(0, 2, 3),
        intArrayOf(0, 1, 3),
        intArrayOf(1, 2, 3),
    ),
    5 to arrayOf(
        intArrayOf(0, 1, 2, 3)
    )
)

var n = 0
var m = 0

class Pos(val row: Int, val col: Int)
class CCTV(val pos: Pos, val type: Int)

fun main() {
    val data = inputIntList()
    n = data[0]
    m = data[1]

    repeat(n) { row ->
        val line = inputIntList()
        office.add(line.toIntArray())

        for (col in 0 until m) {
            val cctv = line[col]
            if (cctv in 1..5) {
                cctvList.add(CCTV(Pos(row, col), cctv))
            }
            if (cctv in 1 .. 6) {
                watching[row][col] = 1
            }
        }
    }

    btk(0)
    println(answer)
}

fun btk(num: Int) {
    if (num == cctvList.size) {
        setAnswer()
        return
    }

    val current = cctvList[num]
    for (points in directions[current.type]!!) {
        points.forEach {
            setWatch(current.pos, it, 1)
        }

        btk(num + 1)

        points.forEach {
            setWatch(current.pos, it, -1)
        }
    }
}

fun setAnswer() {
    var result = 0
    for (i in 0 until n) {
        for (j in 0 until m) {

            if (watching[i][j] == 0) {
                result += 1
            }

        }
    }
    if (answer > result) {
        answer = result
    }
}


fun setWatch(current: Pos, direction: Int, value: Int) {
    var watchRow = current.row + dy[direction]
    var watchCol = current.col + dx[direction]

    while (watchRow in 0 until n && watchCol in 0 until m && office[watchRow][watchCol] != 6) {
        watching[watchRow][watchCol] += value

        watchRow += dy[direction]
        watchCol += dx[direction]
    }
}