// 문제 : https://www.acmicpc.net/problem/1043

val br = System.`in`.bufferedReader()

fun main() {
    var answer = 0
    val (n, m) = br.readLine().split(" ").map { it.toInt() }
    var known = br.readLine().split(" ").map { it.toInt() }
    var knownPeople = makeSet(known)

    val parties = ArrayList<Set<Int>>()

    repeat(m) {
        val party = br.readLine().split(" ").map { it.toInt() }
        val knownParty = makeSet(party)
        parties.add(knownParty)

        if ((knownPeople - knownParty).size != knownPeople.size) {
            knownPeople += knownParty
        }
    }

    repeat(m-1) {
        for (party in parties) {
            if ((knownPeople - party).size != knownPeople.size) {
                knownPeople += party
            }
        }
    }


    for (party in parties) {
        if ((party - knownPeople).size == party.size) {
            answer++
        }
    }

    println(answer)
}

fun makeSet(list: List<Int>) = list.slice(1..list[0]).toSet()
