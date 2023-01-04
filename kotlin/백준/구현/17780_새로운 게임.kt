// 문제 : https://www.acmicpc.net/problem/17780

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

const val WHITE = 0
const val RED = 1
const val BLUE = 2

const val RIGHT = 1
const val LEFT = 2
const val UP = 3
const val DOWN = 4

val boardStack = Array(13) { Array(13) { ArrayDeque<Int>() } }
val board = mutableListOf<List<Int>>(listOf())
val chessList = mutableListOf<Chess>()

class Chess(
    var row: Int,
    var col: Int,
    var direction: Int
)

val dy = arrayOf(0, 0, 0, -1, 1)
val dx = arrayOf(0, 1, -1, 0, 0)

fun main() {
    val (n, k) = inputIntList()

    repeat(n) {
        board.add(listOf(0) +  inputIntList())
    }

    repeat(k) {
        val (r, c, d) = inputIntList()
        val chess = Chess(r, c, d)
        chessList.add(chess)
        boardStack[r][c].add(it)
    }

    var count = 0
    while (count < 1000) {
        count++
        progress(n)
        if (isEndOfGame()) {
            println(count)
            return
        }
    }
    println(-1)
}

fun isEndOfGame(): Boolean {
    val chess = chessList[0]
    for (i in 1..12) {
        for (j in 1 .. 12) {
            if (boardStack[i][j].size >= 4) {
                return true
            }
        }
    }
    return false
}

fun progress(n: Int) {
    for (i in 0 until chessList.size) {
        val chess = chessList[i]

        if (boardStack[chess.row][chess.col][0] != i) {
            continue
        }

        val nr = chess.row + dy[chess.direction]
        val nc = chess.col + dx[chess.direction]

        checkNext(nr, nc, n, chess)
    }
}

private fun checkNext(nr: Int, nc: Int, n: Int, chess: Chess) {
    when {
        isOutOfBoard(nr, nc, n) || board[nr][nc] == BLUE -> {
            doBlue(chess, n)
        }

        board[nr][nc] == RED -> {
            doRed(chess, nr, nc)
        }

        board[nr][nc] == WHITE -> {
            doWhite(chess, nr, nc)
        }
    }
}

private fun isOutOfBoard(nr: Int, nc: Int, n: Int) = nr == 0 || nc == 0 || nr > n || nc > n

private fun doBlue(chess: Chess, n: Int) {
    chess.direction = when (chess.direction) {
        RIGHT -> LEFT
        LEFT -> RIGHT
        UP -> DOWN
        else -> UP
    }

    val nr = chess.row + dy[chess.direction]
    val nc = chess.col + dx[chess.direction]

    when {
        isOutOfBoard(nr, nc, n) || board[nr][nc] == BLUE -> {}

        board[nr][nc] == RED -> {
            doRed(chess, nr, nc)
        }

        board[nr][nc] == WHITE -> {
            doWhite(chess, nr, nc)
        }
    }
}

private fun doRed(chess: Chess, nr: Int, nc: Int) {
    val targetRow = chess.row
    val targetCol = chess.col

    while (boardStack[targetRow][targetCol].isNotEmpty()) {
        val tempChessIndex = boardStack[targetRow][targetCol].removeLast()
        val tempChess = chessList[tempChessIndex]
        tempChess.apply {
            row = nr
            col = nc
        }
        boardStack[nr][nc].add(tempChessIndex)
    }
}

private fun doWhite(chess: Chess, nr: Int, nc: Int) {
    val targetRow = chess.row
    val targetCol = chess.col

    while (boardStack[targetRow][targetCol].isNotEmpty()) {
        val tempChessIndex = boardStack[targetRow][targetCol].removeFirst()
        val tempChess = chessList[tempChessIndex]
        tempChess.apply {
            row = nr
            col = nc
        }
        boardStack[nr][nc].add(tempChessIndex)
    }
}