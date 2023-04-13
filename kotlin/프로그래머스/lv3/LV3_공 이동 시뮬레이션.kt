// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/87391#qna

data class Range(var sRow: Long, var sCol: Long, var eRow: Long, var eCol: Long) {
    fun countRange(): Long {
        val row = eRow - sRow + 1
        val col = eCol - sCol + 1
        return row * col
    }
}

class Solution {
    val dont = Range(-1 ,-1 ,-1, -1)

    val dRow = intArrayOf(0, 0, 1, -1)
    val dCol = intArrayOf(1, -1, 0, 0)

    var lastRow = 0L
    var lastCol = 0L

    fun Long.safeRow(): Long {
        return if (this < 0) 0
        else if (this > lastRow) lastRow
        else this
    }

    fun Long.safeCol(): Long {
        return if (this < 0) 0
        else if (this > lastCol) lastCol
        else this
    }

    fun calcPrevRange(range: Range, query: IntArray): Range {
        val calcRange = Range(
            range.sRow + dRow[query[0]] * query[1],
            range.sCol + dCol[query[0]] * query[1],
            range.eRow + dRow[query[0]] * query[1],
            range.eCol + dCol[query[0]] * query[1]
        )

        when (query[0]) {
            0 -> {
                if (range.sCol == 0L) {
                    calcRange.sCol = 0
                }
                calcRange.eCol = calcRange.eCol.safeCol()
            }

            1 -> {
                if (range.eCol == lastCol) {
                    calcRange.eCol = lastCol
                }
                calcRange.sCol = calcRange.sCol.safeCol()
            }

            2 -> {
                if (range.sRow == 0L) {
                    calcRange.sRow = 0
                }
                calcRange.eRow = calcRange.eRow.safeRow()
            }

            3 -> {
                if (range.eRow == lastRow) {
                    calcRange.eRow = lastRow
                }
                calcRange.sRow = calcRange.sRow.safeRow()
            }
        }

        if (calcRange.sRow > calcRange.eRow || calcRange.sCol > calcRange.eCol) {
            return dont
        }

        return calcRange
    }

    fun solution(n: Int, m: Int, x: Int, y: Int, queries: Array<IntArray>): Long {
        var answerRange = Range(x.toLong(), y.toLong(), x.toLong(), y.toLong())
        lastRow = (n - 1).toLong()
        lastCol = (m - 1).toLong()

        for (i in queries.lastIndex downTo 0) {
            answerRange = calcPrevRange(answerRange, queries[i])
            if (answerRange == dont) {
                return 0L
            }
        }

        return answerRange.countRange()
    }
}

