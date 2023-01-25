// 문제 : https://www.acmicpc.net/problem/2831

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.abs

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun main() {
    val n = inputInt()
    var answer = 0

    val boys = inputIntList().sorted()
    val girls = inputIntList()
    val taller = girls.filter { it > 0 }.sortedDescending()
    val lower = girls.filter { it < 0 }.map { abs(it) }.sorted()

    var tallerIndex = 0
    var lowerIndex = 0

    for (boy in boys) {
        if (boy > 0) {
            if (lower.isEmpty()) {
                continue
            }

            while (lowerIndex <= lower.lastIndex && boy >= lower[lowerIndex]) {
                lowerIndex++
            }

            if (lowerIndex <= lower.lastIndex) {
                answer++
                lowerIndex++
            }
        } else {
            if (taller.isEmpty()) {
                continue
            }

            while (tallerIndex <= taller.lastIndex && abs(boy) <= taller[tallerIndex]) {
                tallerIndex++
            }

            if (tallerIndex <= taller.lastIndex) {
                answer++
                tallerIndex++
            }
        }
    }

    println(answer)
}