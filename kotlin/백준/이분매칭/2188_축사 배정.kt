// 문제 : https://www.acmicpc.net/problem/2188

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val availWork = mutableListOf<List<Int>>(emptyList())
var visited = BooleanArray(1)
var allocate = IntArray(1)

fun dfs(x: Int): Boolean {
    for (i in availWork[x]) {
        if (visited[i]) {
            continue
        }
        visited[i] = true
        if (allocate[i] == 0 || dfs(allocate[i])) {
            allocate[i] = x
            return true
        }
    }
    return false
}

fun main() {
    val (n, m) = inputIntList()
    var answer = 0
    allocate = IntArray(m + 1)

    for (i in 1 .. n) {
        val tmp = br.readLine()!!
        if (tmp[0] == '0') {
            availWork.add(emptyList())
            continue
        }
        val work = tmp.split(" ").map { it.toInt() }.filterIndexed { index, _ -> index != 0 }
        availWork.add(work)
        visited = BooleanArray(m + 1)

        if (dfs(i)) {
            answer += 1
        }
    }
    println(answer)
}