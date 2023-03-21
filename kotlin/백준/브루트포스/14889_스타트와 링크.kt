// 문제 : https://www.acmicpc.net/problem/14889

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Math.abs

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val arr = mutableListOf<List<Int>>()
var carr = mutableListOf<Int>()

var answer = 100000000

fun main() {
    val n = inputInt()
    repeat(n) {
        arr.add(inputIntList())
    }

    getComb(n, 0, 0)
    println(answer)
}

fun getComb(n: Int, current: Int, prev: Int) {
    if (current == n/2) {
        val result = abs(calcScore(carr) - calcScore((0 until n).filter { it !in carr }))
        answer = minOf(result, answer)
        return
    }

    for (i in prev until n) {
        carr.add(i)
        getComb(n, current + 1, i+1)
        carr.removeLast()
    }
}

fun calcScore(target: List<Int>): Int {
    var result = 0
    for (i in target.indices) {
        for (j in target.indices) {
            result += arr[target[i]][target[j]]
        }
    }
    return result
}