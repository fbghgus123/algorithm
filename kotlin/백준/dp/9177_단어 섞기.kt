// 문제 : https://www.acmicpc.net/problem/9177
import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun main() {
    val n = inputInt()
    repeat(n) { order ->
        val (a, b, ab) = br.readLine()!!.split(" ")
        val memo = Array(a.length + 1) { BooleanArray(b.length + 1) }
        memo[0][0] = true

        for (i in 1 .. a.length) {
            memo[i][0] = if (a[i - 1] == ab[i - 1]) {
                memo[i-1][0]
            } else {
                false
            }
        }

        for (i in 1 .. b.length) {
            memo[0][i] = if (b[i - 1] == ab[i - 1]) {
                memo[0][i-1]
            } else {
                false
            }
        }

        for (i in 1 .. a.length) {
            for (j in 1 .. b.length) {

                memo[i][j] = when {
                    a[i - 1] != ab[i + j - 1] && b[j - 1] != ab[i + j - 1] -> false
                    a[i - 1] == ab[i + j - 1] && b[j - 1] != ab[i + j - 1] ->  memo[i-1][j]
                    a[i - 1] != ab[i + j - 1] && b[j - 1] == ab[i + j - 1] ->  memo[i][j-1]
                    else ->  memo[i-1][j] || memo[i][j-1]
                }

            }
        }

        if (memo[a.length][b.length]) {
            println("Data set ${order + 1}: yes")
        } else {
            println("Data set ${order + 1}: no")
        }
    }
}