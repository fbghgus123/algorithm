import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

val br = BufferedReader(InputStreamReader(System.`in`))
fun inputInt() = br.readLine().toInt()
fun inputIntList() = br.readLine().split(" ").map { it.toInt() }

data class Pos(val row: Int, val col: Int)
val HALL = Pos(-1, -1)

var n = 0
var m = 0
var answer = 11

val maze = mutableListOf<String>()
var rPosition = Pos(0, 0)
var bPosition = Pos(0, 0)

fun main() {
    val (a, b) = inputIntList()
    n = a
    m = b

    repeat(n) { r ->
        var line = br.readLine()
        if ('R' in line) {
            rPosition = Pos(r, line.indexOf('R'))
        }

        if ('B' in line) {
            bPosition = Pos(r, line.indexOf('B'))
        }
        maze.add(line)
    }

    dfs(rPosition, bPosition, -1, 0)
    if (answer > 10) {
        println(-1)
    } else {
        println(answer)
    }
}

fun dfs(r: Pos, b: Pos, prev: Int, count: Int) {
    if (count > 9) {
        return
    }

    for (i in 0 until 4) {
        if (i == 0) {
            if (prev == 0) continue
            var nrPos = goLeft(r)
            var nbPos = goLeft(b)

            if (nbPos == HALL) {
                continue
            }

            if (nrPos == HALL) {
                answer = minOf(answer, count + 1)
                return
            }

            if (nbPos == nrPos) {
                if (r.col < b.col) {
                    nbPos = nbPos.copy(col = nbPos.col + 1)
                } else {
                    nrPos = nrPos.copy(col = nrPos.col + 1)
                }
            }

            if (nrPos == r && nbPos == b) {
                continue
            }

            dfs(nrPos, nbPos, i, count + 1)
        }

        if (i == 1) {
            if (prev == 1) continue

            var nrPos = goRight(r)
            var nbPos = goRight(b)

            if (nbPos == HALL) {
                continue
            }

            if (nrPos == HALL) {
                answer = minOf(answer, count + 1)
                return
            }

            if (nbPos == nrPos) {
                if (r.col > b.col) {
                    nbPos = nbPos.copy(col = nbPos.col - 1)
                } else {
                    nrPos = nrPos.copy(col = nrPos.col - 1)
                }
            }

            if (nrPos == r && nbPos == b) {
                continue
            }

            dfs(nrPos, nbPos, i, count + 1)
        }

        if (i == 2) {
            if (prev == 2) continue

            var nrPos = goUp(r)
            var nbPos = goUp(b)

            if (nbPos == HALL) {
                continue
            }

            if (nrPos == HALL) {
                answer = minOf(answer, count + 1)
                return
            }


            if (nbPos == nrPos) {
                if (r.row < b.row) {
                    nbPos = nbPos.copy(row = nbPos.row + 1)
                } else {
                    nrPos = nrPos.copy(row = nrPos.row + 1)
                }
            }

            if (nrPos == r && nbPos == b) {
                continue
            }

            dfs(nrPos, nbPos, i, count + 1)
        }

        if (i == 3) {
            if (prev == 3) continue

            var nrPos = goDown(r)
            var nbPos = goDown(b)

            if (nbPos == HALL) {
                continue
            }

            if (nrPos == HALL) {
                answer = minOf(answer, count + 1)
                return
            }


            if (nbPos == nrPos) {
                if (r.row > b.row) {
                    nbPos = nbPos.copy(row = nbPos.row - 1)
                } else {
                    nrPos = nrPos.copy(row = nrPos.row - 1)
                }
            }

            if (nrPos == r && nbPos == b) {
                continue
            }
            dfs(nrPos, nbPos, i, count + 1)
        }
    }

}

fun goLeft(pos: Pos): Pos {
    for (col in pos.col - 1 downTo 0) {
        when (maze[pos.row][col]) {
            '#' -> return pos.copy(col = col + 1)
            'O' -> return HALL
        }
    }
    return pos
}

fun goRight(pos: Pos): Pos {
    for (col in pos.col + 1 until m) {
        when (maze[pos.row][col]) {
            '#' -> return pos.copy(col = col - 1)
            'O' -> return HALL
        }
    }
    return pos
}

fun goUp(pos: Pos): Pos {
    for (row in pos.row - 1 downTo 0) {
        when (maze[row][pos.col]) {
            '#' -> return pos.copy(row = row + 1)
            'O' -> return HALL
        }
    }
    return pos
}

fun goDown(pos: Pos): Pos {
    for (row in pos.row + 1 until n) {
        when (maze[row][pos.col]) {
            '#' -> return pos.copy(row = row - 1)
            'O' -> return HALL
        }
    }
    return pos
}