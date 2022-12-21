// 문제 : https://www.acmicpc.net/problem/9084

val br = System.`in`.bufferedReader()

fun main() {

    val t = br.readLine().toInt()

    repeat(t) {
        val n = br.readLine().toInt()
        val coins = br.readLine().split(" ").map { it.toInt() }
        val m = br.readLine().toInt()

        testCase(n, coins, m)
    }
}

fun testCase(n: Int, coins: List<Int>, m: Int) {

    val dp = Array(n + 1) { Array(m + 1) { 0 } }

    for (i in 0..n) {
        dp[i][0] = 1
    }

    for (i in 0 until n) {
        val coin = coins[i]
        for (current in 1..m) {
            dp[i+1][current] = dp[i][current]
            if (current >= coin) {
                dp[i+1][current] += dp[i+1][current - coin]
            }
        }
    }
    println(dp[n][m])
}

