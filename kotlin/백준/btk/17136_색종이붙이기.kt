// 문제 : https://www.acmicpc.net/problem/17136
import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val board = mutableListOf<IntArray>()

class Pos(val row: Int, val col: Int)

val using = IntArray(6) { 5 }
var answer = Int.MAX_VALUE

fun check(pos: Pos, count: Int, num: Int = 0): Boolean {
    if (pos.row + count > 10 || pos.col + count > 10) return false
    for (row in pos.row until pos.row + count) {
        for (col in pos.col until pos.col + count) {
            if (board[row][col] == num) return false
        }
    }
    return true
}

fun setPaper(pos: Pos, count: Int, num: Int = 0) {
    for (row in pos.row until pos.row + count) {
        for (col in pos.col until pos.col + count) {
            board[row][col] = num
        }
    }
}

fun btk(n: Int, pos: Pos) {
    if (pos.row > 9) {
        if (check(Pos(0, 0), 10, 1)) {
            answer = minOf(answer, n)
        }
        return
    }

    if (answer <= n) return

    val nextPos = if (pos.col == 9) {
        Pos(pos.row + 1, 0)
    } else {
        Pos(pos.row, pos.col + 1)
    }

    if (board[pos.row][pos.col] == 1) {
        for (i in 5 downTo 1) {
            if (using[i] > 0 && check(pos, i)) {
                setPaper(pos, i)
                using[i] -= 1
                btk(n+1, nextPos)
                using[i] += 1
                setPaper(pos, i, 1)
            }
        }
    } else {
        btk(n, nextPos)
    }
}

fun main() {
    using[0] = 0

    repeat(10) {
        board.add(inputIntList().toIntArray())
    }

    btk(0, Pos(0, 0))
    println(if(answer == Int.MAX_VALUE) -1 else answer)
}