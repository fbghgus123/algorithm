// 문제 : https://www.acmicpc.net/problem/2179

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val words = mutableMapOf<String, String>()
var answerS = ""
var answerT = ""
var sameCount = 0

fun main() {
    val n = inputInt()
    repeat(n) {
        val word = br.readLine()

        for (i in word.indices) {
            val chars = word.substring(0, i + 1)
            if (!words.containsKey(chars)) {
                words[chars] = word
            } else if (sameCount <= i) {
                answerS = words[chars]!!
                answerT = word
                sameCount = i + 1
            }
        }
    }
    println(answerS)
    println(answerT)
}