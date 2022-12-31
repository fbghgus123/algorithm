// 문제 : https://www.acmicpc.net/problem/1774

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.abs
import kotlin.math.hypot

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }
fun inputInt() = br.readLine().toInt()

val positionList = mutableListOf<Position>(Position(0, 0))
val edgeList = mutableListOf<Edge>()

class Position(val x: Int, val y: Int)
class Edge(val pot: Array<Int>, val distance: Double)

val parent = (0 .. 1000).toMutableList()

fun find(a: Int): Int {
    if (parent[a] == a) return a
    return find(parent[a])
}

fun join(a: Int, b: Int) {
    val rootA = find(a)
    val rootB = find(b)
    parent[rootB] = rootA
}

fun isSameSet(a: Int, b: Int): Boolean {
    val rootA = find(a)
    val rootB = find(b)
    return rootA == rootB
}

fun getDistance(a: Position, b: Position): Double {
    val xDis = abs(a.x - b.x).toDouble()
    val yDis = abs(a.y - b.y).toDouble()
    return hypot(xDis, yDis)
}

fun main() {
    var answer: Double = 0.0
    val (n, m) = inputIntList()

    repeat(n) {
        val (x, y) = inputIntList()
        positionList.add(Position(x, y))
    }

    repeat(m) {
        val (a, b) = inputIntList().sorted()
        join(a, b)
    }

    for (i in 1 .. n) {
        for (j in 1 .. n) {
            if (i == j) {
                continue
            }
            edgeList.add(Edge(arrayOf(i, j), getDistance(positionList[i], positionList[j])))
        }
    }

    edgeList.sortBy { it.distance }

    for (edge in edgeList) {
        val a = edge.pot[0]
        val b = edge.pot[1]

        if (isSameSet(a, b)) {
            continue
        }

        join(a, b)
        answer += edge.distance
    }

    println(String.format("%.2f", answer))
}