// 문제 : https://www.acmicpc.net/problem/14725

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }


class Node(val value: String, val children: HashMap<String, Node> = hashMapOf())

fun main() {
    val n = inputInt()
    val root = Node("root")

    repeat(n) {
        val tmp = br.readLine().split(" ")
        val data = tmp.subList(1, tmp.size)

        var current = root
        for (char in data) {
            if (!current.children.containsKey(char)) {
                current.children[char] = Node(char)
            }
            current = current.children[char]!!
        }
    }

    recur(root)
}

fun recur(node: Node, depth: Int = -1) {
    if (node.value != "root") {
        val stringBuilder = StringBuilder()
        repeat(depth) {
            stringBuilder.append("--")
        }
        stringBuilder.append(node.value)
        println(stringBuilder.toString())
    }

    node.children.values.toList().sortedBy { it.value }.forEach {
        recur(it, depth + 1)
    }
}