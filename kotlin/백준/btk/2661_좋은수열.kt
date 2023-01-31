// 문제 : https://www.acmicpc.net/problem/2661

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val arr = Array(81) { "" }
var n: Int = 0

fun main() {
    n = inputInt()
    arr[1] = "1"
    btk(2)
}

fun btk(a: Int): Boolean {
    if (a > n) {
        val builder = StringBuilder()
        for (i in 1 until a) {
            builder.append(arr[i])
        }
        println(builder.toString())
        return true
    }

    for (i in arrayOf("1", "2", "3")) {
        arr[a] = i
        if (isGood(a)) {
            if (btk(a + 1)) return true
        }
    }

    return false
}

fun isGood(a: Int): Boolean {
    val builder = StringBuilder()
    for (i in 1 .. a) {
        builder.append(arr[i])
    }
    val string = builder.toString()
    val lastIndex = string.lastIndex
    val num = a / 2

    for (i in 0 until num) {
        if (string.slice(lastIndex - i..lastIndex) == string.slice(lastIndex - i * 2 - 1 until lastIndex - i)) {
            return false
        }
    }

    return true
}