// 문제 : https://www.acmicpc.net/problem/9466

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

lateinit var visited: IntArray
lateinit var student: List<Int>
lateinit var inStack: MutableSet<Int>
var answer = 0

fun main() {
    val t = inputInt()
    repeat(t) {
        val n = inputInt()
        answer = n
        student = listOf(0) + inputIntList()
        visited = IntArray(n+1)

        for (i in 1 .. n) {
            inStack = mutableSetOf()
            dfs(i)
            inStack.forEach {
                visited[it] = 1
            }
        }
        println(answer)
    }
}

fun dfs(index: Int) {
    if (visited[index] == 1) {
        return
    }

    if (inStack.contains(index)) {
        val a = inStack.indexOf(index)
        answer -= inStack.size - a
        return
    }

    inStack.add(index)
    val teamStudent = student[index]
    dfs(teamStudent)
}