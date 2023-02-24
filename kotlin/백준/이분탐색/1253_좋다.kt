// 문제 : https://www.acmicpc.net/problem/1253

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val numMap = mutableMapOf<Int, Boolean>()
val numCount = mutableMapOf<Int, Int>()

fun main() {
    val n = inputInt()
    val num = inputIntList().sorted()

    num.forEach {
        if (numCount[it] == null) {
            numCount[it] = 0
        }
        numCount[it] = numCount[it]!! + 1
    }

    for (i in num.indices) {
        for (j in i + 1 until num.size) {
            val target = num[i] + num[j]
            if (numMap[target] != null) {
                continue
            }
            if(findExist(target, num, i, j)) {
                numMap[target] = true
            }
        }
    }

    var answer = 0
    numMap.forEach { (t, u) ->
        if (u) {
            answer += numCount[t]!!
        }
    }
    println(answer)
}

fun findExist(target: Int, num: List<Int>, i: Int, j: Int): Boolean {
    var left = 0
    var right = num.size - 1

    while (left <= right) {
        val mid = (left + right) / 2

        if (num[mid] == target) {
            if (num[i] == target || num[j] == target) {
                for (index in num.indices) {
                    if (num[index] == target && index != i && index != j) {
                        return true
                    }
                }
                return false
            }

            return true
        }

        if (num[mid] < target) {
            left = mid + 1
        } else {
            right = mid - 1
        }

    }
    return false
}