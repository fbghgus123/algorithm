// 문제 : https://www.acmicpc.net/problem/6091

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Edge(val s: Int, val e: Int, val cost: Int)

val edgeList = ArrayList<Edge>()
val mst = ArrayList<Edge>()

fun find(n: Int, parent: IntArray): Int {
    if (n == parent[n]) {
        return n
    }
    parent[n] = find(parent[n], parent)
    return parent[n]
}

fun join(a: Int, b: Int, parent: IntArray) {
    val aRoot = find(a, parent)
    val bRoot = find(b, parent)
    parent[bRoot] = aRoot
}

fun main() {
    val n = inputInt()
    val parent = (0..n+1).toList().toIntArray()

    for (s in 1 until n) {
        val edges = inputIntList()
        edges.forEachIndexed { index, cost ->
            edgeList.add(Edge(s, s + 1 + index, cost))
        }
    }

    edgeList.sortBy { it.cost }

    val answer = Array(n+1) { ArrayList<Int>() }

    for (edge in edgeList) {

        if (find(edge.s, parent) == find(edge.e, parent)) {
            continue
        }

        join(edge.s, edge.e, parent)
        answer[edge.e].add(edge.s)
        answer[edge.s].add(edge.e)

        if (mst.size >= n-1) {
            break
        }
    }

    for (i in 1 .. n) {
        println("${answer[i].size} ${answer[i].sorted().joinToString(" ")}")
    }
}


