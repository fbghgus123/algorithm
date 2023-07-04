// 문제 : https://www.acmicpc.net/problem/2503

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val num = IntArray(3)

class Rule(val number: List<Int>, val s: Int, val b: Int)

fun main() {
    val n = inputInt()
    var answer = 0

    val baseball = mutableListOf<Rule>()

    repeat(n) {
        val (number, s, b) = inputIntList()

        val one = number / 100
        val two = (number % 100) / 10
        val three = number % 10

        baseball.add(Rule(listOf(one, two, three), s, b))
    }

    fun dp(index: Int) {
        if (index == 3) {
            for (i in num) {
                if (num.count { it == i } > 1) {
                    return
                }
            }

            baseball.forEach {
                var strike = 0
                var ball = 0

                for (i in 0 .. 2) {
                    if (it.number[i] == num[i]) {
                        strike += 1
                        continue
                    }

                    if (it.number[i] in num) {
                        ball += 1
                    }
                }

                if (strike != it.s || ball != it.b) {
                    return
                }
            }

            answer += 1
            return
        }

        for (i in 1 .. 9) {
            num[index] = i
            dp(index + 1)
        }
    }

    dp(0)
    println(answer)
}