// 문제: https://www.acmicpc.net/problem/19238

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

data class Pos(val row: Int, val col: Int)
class Customer(val pos: Pos, val distance: Int)

val board = mutableListOf<IntArray>()
val arriveList = HashMap<Pos, Pos>()

val dy = intArrayOf(-1, 0, 0, 1)
val dx = intArrayOf(0, -1, 1, 0)

fun broadcastCustomer(current: Pos, n: Int): Customer {
    if (board[current.row][current.col] == 2) {
        return Customer(current, 0)
    }

    val result = PriorityQueue<Customer>() { a, b ->
        if (a.distance != b.distance) {
            a.distance - b.distance
        }
        else if (a.pos.row == b.pos.row) {
            a.pos.col - b.pos.col
        } else {
            a.pos.row - b.pos.row
        }
    }

    val queue = ArrayDeque<Pos>()
    queue.add(current)
    val visited = Array(n) { IntArray(n) { -1 } }
    visited[current.row][current.col] = 0

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()
        for (i in 0 until 4) {
            val cy = current.row + dy[i]
            val cx = current.col + dx[i]

            if (cy >= 0 && cx >= 0 && cy < n && cx < n && visited[cy][cx] == -1 && board[cy][cx] != 1) {
                visited[cy][cx] = visited[current.row][current.col] + 1
                queue.add(Pos(cy, cx))
                if (board[cy][cx] == 2) {
                    result.add(Customer(Pos(cy, cx), visited[cy][cx]))
                }
            }
        }
    }

    return if (result.isEmpty()) {
        Customer(Pos(-1, -1), -1)
    } else {
        result.remove()
    }
}

fun getDistance(start: Pos, destination: Pos, n: Int): Int {
    if (start == destination) {
        return 0
    }

    val queue = ArrayDeque<Pos>()
    queue.add(start)

    val visited = Array(n) { IntArray(n) { -1 } }
    visited[start.row][start.col] = 0

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()
        for (i in 0 until 4) {
            val cy = current.row + dy[i]
            val cx = current.col + dx[i]

            if (cy >= 0 && cx >= 0 && cy < n && cx < n && visited[cy][cx] == -1 && board[cy][cx] != 1) {
                visited[cy][cx] = visited[current.row][current.col] + 1
                queue.add(Pos(cy, cx))
                if (Pos(cy, cx) == destination) {
                    return visited[cy][cx]
                }
            }
        }
    }
    return -1
}

fun main() {
    val (n, m, f) = inputIntList()
    var fuel = f

    repeat(n) {
        board.add(inputIntList().toIntArray())
    }
    val (r, c) = inputIntList()
    var current = Pos(r - 1, c - 1)

    repeat(m) {
        val (cr, cc, ar, ac) = inputIntList()
        arriveList[Pos(cr - 1, cc - 1)] = Pos(ar - 1, ac - 1)
        board[cr - 1][cc - 1] = 2
    }

    repeat(m) {
        // 1. 손님 찾기 + 최단 거리
        val customer = broadcastCustomer(current, n)

        // 2. 남은 연료 확인
        if (fuel < customer.distance || customer.distance == -1) {
            println(-1)
            return
        }

        // 3. 목적지 확인 + 최단 거리
        val destinationDistance = getDistance(customer.pos, arriveList[customer.pos]!!, n)

        // 4. 남은 연료 확인
        if (fuel < customer.distance + destinationDistance || destinationDistance == -1) {
            println(-1)
            return
        }

        // 5. 이동 + 연료 감소 and 충전
        board[customer.pos.row][customer.pos.col] = 0
        current = arriveList[customer.pos]!!
        fuel = fuel - customer.distance + destinationDistance
    }
    println(fuel)
}