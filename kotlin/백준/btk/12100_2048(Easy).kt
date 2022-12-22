// 문제 : https://www.acmicpc.net/problem/12100

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun getIntList() = br.readLine().split(' ').map { it.toInt() }
fun getInt() = br.readLine().toInt()

const val LEFT = 0
const val RIGHT = 1
const val UP = 2
const val DOWN = 3

var maxBlock = 0

fun combineBlock(line: IntArray): IntArray {
    val lineSize = line.size
    val result = mutableListOf<Int>()
    var unCombineNum = -1
    line.forEach { num ->
        unCombineNum = when {
            num == 0 -> {
                unCombineNum
            }

            unCombineNum == -1 -> {
                num
            }

            num == unCombineNum -> {
                result.add(unCombineNum * 2)
                -1
            }

            else -> {
                result.add(unCombineNum)
                num
            }
        }
    }
    if (unCombineNum != -1) {
        result.add(unCombineNum)
    }

    for (i in result.size until lineSize) {
        result.add(0)
    }
    return result.toIntArray()
}

fun goDirection(direction: Int, table: Array<IntArray>): Array<IntArray> {
    val result = Array(table.size) { IntArray(table.size) }
    when (direction) {
        LEFT -> {
            table.forEachIndexed { index, arr ->
                result[index] = combineBlock(arr)
            }
        }

        RIGHT -> {
            table.forEachIndexed { index, arr ->
                result[index] = combineBlock(arr.reversedArray()).reversedArray()
            }
        }

        UP -> {
            repeat(table.size) { index ->
                val line = mutableListOf<Int>()
                table.forEach { line.add(it[index]) }
                combineBlock(line.toIntArray()).forEachIndexed { col, value ->
                    result[col][index] = value
                }
            }
        }

        DOWN -> {
            repeat(table.size) { index ->
                val line = mutableListOf<Int>()
                table.forEach { line.add(it[index]) }
                combineBlock(line.toIntArray().reversedArray())
                    .reversedArray()
                    .forEachIndexed { col, value ->
                        result[col][index] = value
                    }
            }
        }
    }
    return result
}

fun getMaxBlock(table: Array<IntArray>): Int {
    var result = 0
    table.forEach {
        val maxx = it.max()
        if (result < maxx) {
            result = maxx
        }
    }
    return result
}

fun btk(count: Int, table: Array<IntArray>) {
    if (count == 5) {
        val maxx = getMaxBlock(table)
        if (maxBlock < maxx) {
            maxBlock = maxx
        }
        return
    }

    repeat(4) { direction ->
        btk(count + 1, goDirection(direction, table))
    }
}

fun main() {
    val n = getInt()
    val table = Array(n) { IntArray(n) { 0 } }

    repeat(n) {
        table[it] = getIntList().toIntArray()
    }

    btk(0, table)
    println(maxBlock)
}