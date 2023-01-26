// 문제 : https://www.acmicpc.net/problem/13560
import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Data(val index: Int, var value: Int)

fun main() {
    val n = inputInt()
    val nums = inputIntList()

    if (nums.sum() != (n * (n - 1)) / 2) {
        println(-1)
        return
    }

    val data = nums.mapIndexed { index, i ->
        Data(index, i)
    }.toMutableList()

    for (i in 1 until n) {
        var avail = n - i - data[i - 1].value
        val sorted = data.subList(i, data.size).sortedWith(compareBy({ -it.value }, { it.index }))

        sorted.forEach {
            if (avail > 0) {
                data[it.index].value -= 1
                avail -= 1

                if (data[it.index].value < 0) {
                    println(-1)
                    return
                }
            }
        }

        if (avail > 0) {
            println(-1)
            return
        }
    }
    println(1)
}