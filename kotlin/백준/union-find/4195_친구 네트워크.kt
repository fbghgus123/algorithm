// 문제 : https://www.acmicpc.net/problem/4195

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

var hashNetwork = HashMap<String, String>()
var hashCount = HashMap<String, Int>()

fun main() {
    val t = inputInt()
    repeat(t) {
        val n = inputInt()
        hashNetwork = HashMap()
        hashCount = HashMap()

        repeat(n) {
            val (a, b) = br.readLine().split(" ").sorted()

            initHash(a)
            initHash(b)

            join(a, b)
            println(hashCount[find(b)])
        }
    }
}

fun join(a: String, b: String) {
    val rootA = find(a)
    val rootB = find(b)

    if (rootA == rootB) {
        return
    }

    val (c, d) = listOf(rootA, rootB).sorted()
    hashNetwork[c] = d
    hashCount[d] = hashCount[c]!! + hashCount[d]!!
}

fun find(a: String): String {
    if (hashNetwork[a] == a) {
        return a
    }
    hashNetwork[a] = find(hashNetwork[a]!!)
    return hashNetwork[a]!!
}

private fun initHash(a: String) {
    if (!hashNetwork.containsKey(a)) {
        hashNetwork[a] = a
        hashCount[a] = 1
    }
}