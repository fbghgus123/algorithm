// 문제 : https://www.acmicpc.net/problem/10942
import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun main() {
    val n = inputInt()
    val arr = inputIntList()
    val bw = System.out.bufferedWriter()

    val dp = Array(n) { IntArray(n) }

    for (i in 0 until n) {
        dp[i][i] = 1
    }

    for (i in 0 until n - 1) {
        if (arr[i] == arr[i + 1]) {
            dp[i][i + 1] = 1
        }
    }

    for (k in 2 until n) {
        for (i in 0 until n - k) {

            val j = i + k
            if (arr[i] == arr[j] && dp[i + 1][j - 1] == 1) {
                dp[i][j] = 1
            }
        }
    }

    val m = inputInt()
    repeat(m) {
        val (s, e) = inputIntList()
        bw.write("${dp[s - 1][e - 1]}\n")
    }
    bw.flush()
}