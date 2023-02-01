// 문제 : https://www.acmicpc.net/problem/4386

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder
import kotlin.math.pow
import kotlin.math.sqrt

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()

val parent = (0 until 100).toList().toIntArray()

class Star(val x: Double, val y: Double)
val starList = mutableListOf<Star>()

class Edge(val s: Int, val e: Int, val distance: Double)
val edgeList = mutableListOf<Edge>()

fun getDistance(a: Star, b: Star): Double {
    return sqrt((a.x - b.x).pow(2.0) + (a.y - b.y).pow(2.0))
}

var count = 0
var answer = 0.0

fun find(a: Int): Int {
    if (parent[a] != a) parent[a] = find(parent[a])
    return parent[a]
}

fun join(a: Int, b: Int) {
    val (c, d) = listOf(a, b).sorted()
    val rootA = find(c)
    val rootB = find(d)
    parent[rootA] = rootB
}

fun main() {
    val n = inputInt()

    repeat(n) {
        val (a, b) = br.readLine().split(" ").map { it.toDouble() }
        starList.add(Star(a, b))
    }

    for (i in 0 until n - 1) {
        for (j in i + 1 until n) {

            val starA = starList[i]
            val starB = starList[j]
            edgeList.add(Edge(i, j, getDistance(starA, starB)))

        }
    }

    edgeList.sortBy { it.distance }
    for (edge in edgeList) {
        if (count == n-1) {
            break
        }

        if (find(edge.s) == find(edge.e)) {
            continue
        }

        answer += edge.distance
        join(edge.s, edge.e)
        count ++
    }

    println(String.format("%.2f", answer))
}