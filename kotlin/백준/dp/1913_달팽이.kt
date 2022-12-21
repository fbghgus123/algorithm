// 문제 : https://www.acmicpc.net/problem/1913

import java.util.*
import kotlin.collections.ArrayList

val br = System.`in`.bufferedReader()
val arr = Array(1000) { Array(1000) { 0 } }

fun main() {

    val n = br.readLine().toInt()
    val num = br.readLine().toInt()

    val answer = snail(n, num)

    for (i in 0 until n) {
        println(arr[i].slice(0 until n).joinToString(" "))
    }

    print("${answer.first} ${answer.second}")
}

val dx = arrayOf(0, 1, 0, -1)
val dy = arrayOf(1, 0, -1, 0)

fun snail(n: Int, num: Int): Pair<Int, Int> {
    var direction = 0
    var current = n * n

    var y = 0
    var x = 0

    var answerY = 0
    var answerX = 0

    while(current > 0) {
        arr[y][x] = current
        if (current == num) {
            answerY = y
            answerX = x
        }

        current--

        // 방향 전환
        val ny = y + dy[direction % 4]
        val nx = x + dx[direction % 4]
        if (nx < 0 || ny < 0 || nx >= n || ny >= n || arr[ny][nx] != 0) {
            direction++
        }

        y += dy[direction % 4]
        x += dx[direction % 4]
    }

    return Pair(answerY + 1, answerX + 1)
}

