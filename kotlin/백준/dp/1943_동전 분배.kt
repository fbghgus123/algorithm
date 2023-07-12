// 문제 : https://www.acmicpc.net/problem/1943

import com.sun.org.apache.xpath.internal.operations.Bool
import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Coin(val money: Int, val count: Int)

fun main() {
    for (t in 0 until 3) {
        val n = inputInt()
        val pocket = mutableListOf(Coin(0, 0))
        var total = 0

        repeat(n) {
            val (money, count) = inputIntList()
            pocket.add(Coin(money, count))
            total += money * count
        }

        if (total % 2 == 1) {
            println(0)
            continue
        }


        pocket.sortBy { -it.money }
        val dp = BooleanArray(total / 2 + 1)
        dp [0] = true

        for (i in 0 until n) {
            val coin = pocket[i]
            for (j in total / 2 downTo coin.money) {
                if (!dp[j - coin.money]) continue
                for (k in 0 until coin.count) {
                    if (j + k * coin.money > total / 2) break
                    dp[j + k * coin.money] = true
                }
            }
        }

        println(
            if (dp[total / 2]) 1 else 0
        )
    }
}
