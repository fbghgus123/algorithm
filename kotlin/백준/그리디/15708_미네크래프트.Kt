// 문제 : https://www.acmicpc.net/problem/15708

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

val br= BufferedReader(InputStreamReader(System.`in`))
fun inputInt() =br.readLine().toInt()
fun inputIntList() =br.readLine().split(" ").map{ it.toInt()}

fun main() {
    val (n ,t ,p) =inputIntList()
    var queue = PriorityQueue<Int>()
    val rocks =inputIntList()
    var sel = 0
    var answer = 0
    var cnt = 0

    for(i in until minOf(n, t/p+1)) {
        sel += rocks[i]
        queue.add(-rocks[i])
        while (t-i*p < sel) {
            sel += queue.poll()
            cnt += 1
        }
        answer =maxOf(answer, i - cnt + 1)
    }
println(answer)
}