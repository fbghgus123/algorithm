// 문제 : https://www.acmicpc.net/problem/5582

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val nums = Array(4001) { IntArray(4001) }

fun main() {
    val p = br.readLine()!!
    val s = br.readLine()!!
    var answer = 0

    for (i in p.indices) {
        val target = p[i]

        for (j in s.indices) {
            if (target == s[j]) {
                if (i > 0 && j > 0) {
                    nums[i][j] = nums[i-1][j-1]
                }
                nums[i][j] += 1

                if (answer < nums[i][j]) {
                    answer = nums[i][j]
                }
            }
        }
    }

    println(answer)
}