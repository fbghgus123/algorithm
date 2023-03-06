// 문제 : https://www.acmicpc.net/problem/3584

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun main() {
    val t = inputInt()
    repeat(t) {
        val n = inputInt()
        val parent = (0 .. n).toMutableList()
        val children = mutableMapOf<Int, MutableList<Int>>()
        val depth = IntArray(n+1)
        var root = 0

        repeat(n-1) {
            val (a, b) = inputIntList()
            parent[b] = a

            if (!children.containsKey(a)) {
                children[a] = mutableListOf()
            }

            children[a]!!.add (b)
        }

        for (i in 1 .. n) {
            if (parent[i] == i) {
                root = i
            }
        }

        fun dfs(node: Int, d: Int) {
            depth[node] = d
            children[node]?.let {
                for (child in it) {
                    dfs(child, d+1)
                }
            }
        }

        dfs(root, 0)
        var (a, b) = inputIntList().sortedBy { depth[it] }
        val diff = depth[b] - depth[a]

        repeat(diff) {
            b = parent[b]
        }

        while (a != b) {
            a = parent[a]
            b = parent[b]
        }

        println(a)
    }
}