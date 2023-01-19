// 문제 : https://www.acmicpc.net/problem/2931

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val blueprint = mutableListOf<String>()
val target = arrayOf(
    arrayOf('|', '+', '1', '4'),
    arrayOf('|', '+', '2', '3'),
    arrayOf('-', '+', '1', '2'),
    arrayOf('-', '+', '3', '4')
)

fun IntArray.isSame(target: IntArray): Boolean {
    for (i in target.indices) {
        if (this[i] != target[i]) {
            return false
        }
    }
    return true
}

fun mapper(data: IntArray) = when {
    intArrayOf(1, 1, 0, 0).isSame(data) -> '|'
    intArrayOf(0, 0, 1, 1).isSame(data) -> '-'
    intArrayOf(1, 1, 1, 1).isSame(data) -> '+'
    intArrayOf(0, 1, 0, 1).isSame(data) -> '1'
    intArrayOf(1, 0, 0, 1).isSame(data) -> '2'
    intArrayOf(1, 0, 1, 0).isSame(data) -> '3'
    intArrayOf(0, 1, 1, 0).isSame(data) -> '4'
    else -> '.'
}

fun main() {
    val (r, c) = inputIntList()

    repeat(r) {
        blueprint.add(br.readLine()!!)
    }

    for (i in 0 until r) {
        for (j in 0 until c) {

            if (blueprint[i][j] == '.') {
                val check = IntArray(4)

                // 상
                if (i != 0 && blueprint[i-1][j] in target[0]) {
                    check[0] = 1
                }

                // 하
                if (i != r-1 && blueprint[i+1][j] in target[1]) {
                    check[1] = 1
                }

                // 좌
                if (j != 0 && blueprint[i][j-1] in target[2]) {
                    check[2] = 1
                }

                // 우
                if (j != c-1 && blueprint[i][j+1] in target[3]) {
                    check[3] = 1
                }

                if (check.sum() > 0) {
                    println("${i+1} ${j+1} ${mapper(check)}")
                    return
                }
            }
        }
    }
}