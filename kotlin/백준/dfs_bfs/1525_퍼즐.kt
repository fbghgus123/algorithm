// 문제 : https://www.acmicpc.net/problem/1525

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.collections.ArrayDeque

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Pos(val row: Int, val col: Int)
data class Puzzle(val state: List<List<Int>>, val count: Int, val zeroPosition: Pos)

val dy = intArrayOf(0, 1, 0, -1)
val dx = intArrayOf(1, 0, -1, 0)

fun exchangeZero(puzzle: Puzzle, row: Int, col: Int): List<List<Int>> {
    val tmp = mutableListOf<MutableList<Int>>()
    repeat(3) {
        tmp.add(puzzle.state[it].toMutableList())
    }
    tmp[row][col] = 0
    tmp[puzzle.zeroPosition.row][puzzle.zeroPosition.col] = puzzle.state[row][col]

    return tmp
}

fun main() {
    val data = HashMap<List<List<Int>>, Int>()

    val first = mutableListOf<List<Int>>()
    var firstPos = Pos(-1, -1)
    repeat(3) {
        val tmp = inputIntList()
        first.add(tmp)

        if (tmp.contains(0)) {
            firstPos = Pos(it, tmp.indexOf(0))
        }
    }
    data[first] = 0
    val queue = ArrayDeque<Puzzle>()
    queue.add(Puzzle(first, 0, firstPos))

    while(queue.isNotEmpty()) {
        val current = queue.removeFirst()

        if (current.count > data[current.state]!!) {
            continue
        }

        for (i in 0..3) {
            val cy = current.zeroPosition.row + dy[i]
            val cx = current.zeroPosition.col + dx[i]

            if (cy < 0 || cy > 2 || cx < 0 || cx > 2) {
                continue
            }

            val nextPuzzle = exchangeZero(current, cy, cx)
            if (!data.containsKey(nextPuzzle) || data[nextPuzzle]!! > current.count + 1) {
                queue.add(Puzzle(nextPuzzle, current.count + 1, Pos(cy, cx)))
                data[nextPuzzle] = current.count + 1
            }
        }
    }
    println(data[listOf(listOf(1, 2, 3), listOf(4, 5, 6), listOf(7, 8, 0))] ?: -1)
}