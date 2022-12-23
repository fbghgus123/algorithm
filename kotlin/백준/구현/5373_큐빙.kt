// 문제 : https://www.acmicpc.net/problem/5373

import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputStringList() = br.readLine().split(" ")
fun inputInt() = br.readLine().toInt()

class Cube {
    val f = Screen('r')
    val u = Screen('w')
    val d = Screen('y')
    val r = Screen('b')
    val b = Screen('o')
    val l = Screen('g')

    fun rotate(direction: String) {
        when (direction) {
            "F-" -> {
                val temp = u.down.reversed().toCharArray()
                u.down = r.left.clone()
                r.left = d.down.reversed().toCharArray()
                d.down = l.right.clone()
                l.right = temp
                f.rotateMinus()
            }
            "F+" -> {
                val temp = u.down.clone()
                u.down = l.right.reversed().toCharArray()
                l.right = d.down.clone()
                d.down = r.left.reversed().toCharArray()
                r.left = temp
                f.rotatePlus()
            }
            "L-" -> {
                val temp = u.left.reversed().toCharArray()
                u.left = f.left.clone()
                f.left = d.left.reversed().toCharArray()
                d.left = b.right.clone()
                b.right = temp
                l.rotateMinus()
            }
            "L+" -> {
                val temp = u.left.clone()
                u.left = b.right.reversed().toCharArray()
                b.right = d.left.clone()
                d.left = f.left.reversed().toCharArray()
                f.left = temp
                l.rotatePlus()
            }
            "R-" -> {
                val temp = u.right.clone()
                u.right = b.left.reversed().toCharArray()
                b.left = d.right.clone()
                d.right = f.right.reversed().toCharArray()
                f.right = temp
                r.rotateMinus()
            }
            "R+" -> {
                val temp = u.right.reversed().toCharArray()
                u.right = f.right.clone()
                f.right = d.right.reversed().toCharArray()
                d.right = b.left.clone()
                b.left = temp
                r.rotatePlus()
            }
            "B-" -> {
                val temp = u.up.clone()
                u.up = l.left.reversed().toCharArray()
                l.left = d.up.clone()
                d.up = r.right.reversed().toCharArray()
                r.right = temp
                b.rotateMinus()
            }
            "B+" -> {
                val temp = u.up.reversed().toCharArray()
                u.up = r.right.clone()
                r.right = d.up.reversed().toCharArray()
                d.up = l.left.clone()
                l.left = temp
                b.rotatePlus()
            }
            "U-" -> {
                val temp = b.up.clone()
                b.up = r.up.clone()
                r.up = f.up.clone()
                f.up = l.up.clone()
                l.up = temp
                u.rotateMinus()
            }
            "U+" -> {
                val temp = b.up.clone()
                b.up = l.up.clone()
                l.up = f.up.clone()
                f.up = r.up.clone()
                r.up = temp
                u.rotatePlus()
            }
            "D-" -> {
                val temp = b.down.clone()
                b.down = l.down.clone()
                l.down = f.down.clone()
                f.down = r.down.clone()
                r.down = temp
                d.rotatePlus()
            }
            "D+" -> {
                val temp = b.down.clone()
                b.down = r.down.clone()
                r.down = f.down.clone()
                f.down = l.down.clone()
                l.down = temp
                d.rotateMinus()
            }
        }
    }
}

class Screen(color: Char) {
    val current = Array(3) { CharArray(3) { color } }
    var down get() = current[2]
        set(value) {
            current[2] = value
        }
    var up get() = current[0]
        set(value) {
            current[0] = value
        }
    var left get() = charArrayOf(current[0][0], current[1][0], current[2][0])
        set(value) {
            current[0][0] = value[0]
            current[1][0] = value[1]
            current[2][0] = value[2]
        }
    var right get() = charArrayOf(current[0][2], current[1][2], current[2][2])
        set(value) {
            current[0][2] = value[0]
            current[1][2] = value[1]
            current[2][2] = value[2]
        }

    fun rotatePlus() {
        val temp = current[0][0]
        current[0][0] = current[2][0]
        current[2][0] = current[2][2]
        current[2][2] = current[0][2]
        current[0][2] = temp
        val temp2 = current[0][1]
        current[0][1] = current[1][0]
        current[1][0] = current[2][1]
        current[2][1] = current[1][2]
        current[1][2] = temp2
    }

    fun rotateMinus() {
        val temp = current[0][0]
        current[0][0] = current[0][2]
        current[0][2] = current[2][2]
        current[2][2] = current[2][0]
        current[2][0] = temp
        val temp2 = current[0][1]
        current[0][1] = current[1][2]
        current[1][2] = current[2][1]
        current[2][1] = current[1][0]
        current[1][0] = temp2
    }

    fun printScreen() {
        current.forEach {
            println("${it[0]}${it[1]}${it[2]}")
        }
    }
}

fun main() {
    val n = inputInt()
    repeat (n) {
        val count = inputInt()
        val cube = Cube()
        inputStringList().forEach {
            cube.rotate(it)
        }
        cube.u.printScreen()
    }
}


