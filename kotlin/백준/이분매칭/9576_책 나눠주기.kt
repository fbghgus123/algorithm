// 문제 : https://www.acmicpc.net/problem/9576

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

var visited = BooleanArray(1)
var availBookList = mutableListOf<List<Int>>(emptyList())
var allocate = IntArray(1)

fun dfs(x: Int): Boolean {
    for (p in availBookList[x]) {
        if (visited[p]) {
            continue
        }
        visited[p] = true

        if (allocate[p] == 0 || dfs(allocate[p])) {
            allocate[p] = x
            return true
        }
    }
    return false
}

fun main() {
    val t = inputInt()

    repeat(t) {
        val (n, m) = inputIntList()
        var answer = 0

        availBookList = mutableListOf<List<Int>>(emptyList())
        allocate = IntArray(n+1)

        for (i in 1 .. m) {
            val (a, b) = inputIntList()

            availBookList.add((a..b).toList())
            visited = BooleanArray(n + 1)
            if (dfs(i)) {
                answer += 1
            }
        }

        println(answer)
    }
}