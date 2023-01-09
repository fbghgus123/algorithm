// 문제 : https://www.acmicpc.net/problem/2933

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputString() = br.readLine()
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val mineral = mutableListOf<CharArray>()
var count = 0

class Position(val r: Int, val c: Int)
val dy = arrayOf(0, 1, 0, -1)
val dx = arrayOf(1, 0, -1, 0)

var visited: Array<IntArray> = emptyArray()

fun main() {
    val (r, c) = inputIntList()

    repeat(r) {
        mineral.add(inputString().toCharArray())
    }

    mineral.add(CharArray(c) { 'x' })
    mineral.reverse()

    val n = inputInt()
    val floor = inputIntList()

    for (f in floor) {
        throwStick(f, c)
        bfs(r, c)
        goDown(r, c)
    }
    mineral.reversed().forEachIndexed { index, chars ->
        if (index != r) {
            println(chars.joinToString(""))
        }
    }
}

fun goDown(r: Int, c: Int) {
    var downCount = r
    var check = IntArray(c)
    val target = mutableListOf<Position>()

    for (i in 1 .. r) {
        for (j in 0 until c) {
            if (mineral[i][j] == 'x' && visited[i][j] == 0) {
                target.add(Position(i, j))

                if (mineral[i-1][j] == '.' && check[j] == 0) {
                    check[j] = 1
                    var count = 0
                    for (row in 1 .. i) {
                        if (mineral[i - row][j] == 'x') {
                            break
                        }
                        count += 1
                    }

                    if (downCount > count) {
                        downCount = count
                    }
                }
            }
        }
    }

    target.forEach {
        mineral[it.r][it.c] = '.'
    }

    target.forEach {
        mineral[it.r - downCount][it.c] = 'x'
    }
}

fun throwStick(floor: Int, c: Int) {
    // 왼쪽
    if (count % 2 == 0) {
        for (i in 0 until c) {
            if (mineral[floor][i] == 'x') {
                mineral[floor][i] = '.'
                break
            }
        }
    }

    //오른쪽
    else {
        for (i in 1 .. c) {
            if (mineral[floor][c - i] == 'x') {
                mineral[floor][c - i] = '.'
                break
            }
        }
    }

    count += 1
}

fun bfs(r: Int, c: Int) {
    visited = Array(r+1) { IntArray(c) }
    val queue = ArrayDeque<Position>()

    for (i in 0 until c) {
        visited[0][i] = 1
        queue.add(Position(0, i))
    }

    while (queue.isNotEmpty()) {
        val pos = queue.removeFirst()

        for (i in 0 .. 3) {
            val cy = pos.r + dy[i]
            val cx = pos.c + dx[i]

            if (0 < cy && 0 <= cx && cy <= r && cx < c && mineral[cy][cx] == 'x' && visited[cy][cx] == 0) {
                queue.add(Position(cy, cx))
                visited[cy][cx] = -1
            }
        }
    }
}
