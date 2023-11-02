// 문제 : https://www.acmicpc.net/problem/1992

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun isAllSame(sy: Int, sx: Int, ey: Int, ex: Int, data: List<String>): Boolean {
    val first = data[sy][sx]

    for (i in sy until ey) {
        for (j in sx until ex) {
            if (data[i][j] != first) return false
        }
    }
    return true
}

fun makeTree(y: Int, x: Int, n: Int, data: List<String>): String {
    if (n == 1 || isAllSame(y, x, y +n, x +n, data)) {
        return data[y][x].toString()
    }

    var result = "("
    val half = n/2

    // 왼쪽 위
    if (isAllSame(y, x, y + half, x + half, data)) {
        result += data[y][x]
    } else {
        result += makeTree(y, x, half, data)
    }

    // 오른쪽 위
    if (isAllSame(y, x + half, y + half, x + n, data)) {
        result += data[y][x + half]
    } else {
        result += makeTree(y, x + half, half, data)
    }

    // 왼쪽 아래
    if (isAllSame(y + half, x, y + n, x + half, data)) {
        result += data[y + half][x]
    } else {
        result += makeTree(y + half, x, half, data)
    }

    // 오른쪽 아래
    if (isAllSame(y + half, x + half, y + n, x + n, data)) {
        result += data[y + half][x + half]
    } else {
        result += makeTree(y + half, x + half, half, data)
    }

    result += ")"
    return result
}

fun main() {
    val n = inputInt()
    val data = mutableListOf<String>()

    repeat(n) {
        data.add(br.readLine())
    }

    println(makeTree(0, 0, n, data))
}