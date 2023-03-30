import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

class Kan(val value: Int, var red: Kan? = null, var blue: Kan? = null)
class Horse(var current: Kan)

val valuableKan = mutableListOf<Kan>()
val horses = mutableListOf<Horse>()
var dices = listOf<Int>()

fun setKan() {
    intArrayOf(0, 10, 20, 25, 30, 40, 0).forEach {
        valuableKan.add(Kan(it))
    }
    valuableKan[5].red = valuableKan[6]
    valuableKan[6].red = valuableKan[6]

    repeat(4) {
        horses.add(Horse(valuableKan[0]))
    }

    addRedKan(valuableKan[0], valuableKan[1], intArrayOf(2, 4, 6, 8))
    addRedKan(valuableKan[1], valuableKan[2], intArrayOf(12, 14, 16, 18))
    addRedKan(valuableKan[2], valuableKan[4], intArrayOf(22, 24, 26, 28))
    addRedKan(valuableKan[4], valuableKan[5], intArrayOf(32, 34, 36, 38))
    addRedKan(valuableKan[3], valuableKan[5], intArrayOf(30, 35))
    addBlueKan(valuableKan[1], valuableKan[3], intArrayOf(13, 16, 19))
    addBlueKan(valuableKan[2], valuableKan[3], intArrayOf(22, 24))
    addBlueKan(valuableKan[4], valuableKan[3], intArrayOf(28, 27, 26))
}

fun addRedKan(start: Kan, end: Kan, mid: IntArray) {
    var current: Kan = start
    mid.forEach {
        val next = Kan(it)
        current.red = next
        current = next
    }
    current.red = end
}

fun addBlueKan(start: Kan, end: Kan, mid: IntArray) {
    val next = Kan(mid[0])
    start.blue = next
    addRedKan(next, end, mid.sliceArray(1..mid.lastIndex))
}

fun move(horse: Horse, dice: Int): Boolean {
    var current = horse.current
    var count = dice

    current.blue?.let {
        current = it
        count -= 1
    }

    while (count > 0) {
        current = current.red!!
        count -= 1
    }

    for (i in horses) {
        if (i.current == current && current != valuableKan[6]) {
            return false
        }
    }

    horse.current = current
    return true
}

var answer = 0
var currentScore = 0

fun btk(n: Int) {
    if (n == 10) {
        answer = maxOf(answer, currentScore)
        return
    }

    for (i in horses) {
        val prev = i.current

        if (move(i, dices[n])) {
            val score = i.current.value
            currentScore += score
            btk(n + 1)
            currentScore -= score
            i.current = prev
        }
    }
}

fun main() {
    setKan()

    dices = inputIntList()
    btk(0)

    println(answer)
}