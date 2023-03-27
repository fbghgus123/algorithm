import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

fun main() {
    val (n, s) = inputIntList()
    val nums = inputIntList()

    var acc = 0
    var l = 0
    var r = 0
    var answer = 100001

    while (r < n) {
        acc += nums[r]
        r += 1
        if (acc >= s) {
            while (acc >= s) {
                acc -= nums[l]
                l += 1
            }
            answer = minOf(answer, r - l)
        }
    }
    if (answer == 100001) {
        println(0)
    } else {
        println(answer + 1)
    }
}
