// 문제 : https://www.acmicpc.net/problem/1184

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

val land = mutableListOf<List<Int>>()
val landSize = Array(50) { IntArray(50) }

data class Area(val up: Int, val down: Int, val left: Int, val right: Int)
val areaCache = HashMap<Area, Int>()

var answer = 0

fun main() {
    val n = inputInt()

    repeat(n) {
        land.add(inputIntList())
    }
    setLandSize(n)

    for (r in 0 until n-1) {
        for (c in 0 until n-1) {
            val leftUp = getLeftUp(r, c)
            val rightUp = getRightUp(r, c, n)
            val leftDown = getLeftDown(r, c, n)
            val rightDown = getRightDown(r, c, n)

            checkAnswer(leftUp, rightDown)
            checkAnswer(rightUp, leftDown)
        }
    }

    println(answer)
}

private fun checkAnswer(a: List<Int>, b: List<Int>) {
    a.forEach { aValue ->
        for (i in b) {
            if (aValue == i) {
                answer += 1
            }
        }
    }
}

private fun getLeftUp(r: Int, c: Int): MutableList<Int> {
    val result = mutableListOf<Int>()

    for (up in 0..r) {
        for (left in 0..c) {
            result.add(getAreaSize(Area(up, r, left, c)))
        }
    }

    return result
}

private fun getRightUp(r: Int, c: Int, n: Int): MutableList<Int> {
    val result = mutableListOf<Int>()

    for (up in 0..r) {
        for (right in c+1 until n) {
            result.add(getAreaSize(Area(up, r, c+1, right)))
        }
    }

    return result
}

private fun getLeftDown(r: Int, c: Int, n: Int): MutableList<Int> {
    val result = mutableListOf<Int>()

    for (down in r+1 until n) {
        for (left in 0..c) {
            result.add(getAreaSize(Area(r+1, down, left, c)))
        }
    }

    return result
}

private fun getRightDown(r: Int, c: Int, n: Int): MutableList<Int> {
    val result = mutableListOf<Int>()

    for (down in r+1 until n) {
        for (right in c+1 until n) {
            result.add(getAreaSize(Area(r+1, down, c+1, right)))
        }
    }

    return result
}

fun getAreaSize(area: Area): Int {
    if (areaCache.containsKey(area)) {
        return areaCache[area]!!
    }

    var result = landSize[area.down][area.right]

    if (area.up > 0) {
        result -= landSize[area.up - 1][area.right]
    }

    if (area.left > 0) {
        result -= landSize[area.down][area.left - 1]
    }

    if (area.left > 0 && area.up > 0) {
        result += landSize[area.up - 1][area.left - 1]
    }

    areaCache[area] = result

    return result
}

private fun setLandSize(n: Int) {
    for (r in 0 until n) {
        for (c in 0 until n) {

            landSize[r][c] = land[r][c]

            if (r != 0) {
                landSize[r][c] += landSize[r - 1][c]
            }

            if (c != 0) {
                landSize[r][c] += landSize[r][c - 1]
            }

            if (r != 0 && c != 0) {
                landSize[r][c] -= landSize[r - 1][c - 1]
            }

        }
    }
}