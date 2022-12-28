// 문제 : https://www.acmicpc.net/problem/13975

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }
fun inputInt() = br.readLine().toInt()

fun main() {
    val t = inputInt()
    repeat(t) {
        val n = inputInt()
        val list = inputIntList()

        val sumArray = Array(n) { IntArray(n) { Int.MAX_VALUE } }

        for (i in 0 until n) {
            for (j in 0 until n - i) {
                if (i == 0) {
                    sumArray[j][j] = 0
                    continue
                }
                val summ = list.subList(j, j+i+1).sum()
                for (k in j until j + i) {
                    sumArray[j][j + i] = when {
                        sumArray[j][j + i] > sumArray[j][k] + sumArray[k + 1][j + i] + summ -> {
                            sumArray[j][k] + sumArray[k + 1][j + i] + summ
                        }
                        else -> { sumArray[j][j + i] }
                    }
                }
            }
        }
        println(sumArray[0][n-1])
    }
}