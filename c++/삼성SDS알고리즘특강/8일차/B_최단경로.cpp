// 문제 : https://www.acmicpc.net/problem/1753

#include <stdio.h>
#include <vector>
#include <queue>

const int INF = 2000000000;

using namespace std;

int V, E, start;

struct e_t {
    int node;
    int cost;
    e_t(int _node, int _cost) : node(_node), cost(_cost) {}
    bool operator<(const e_t &ref) const {
        return this->cost > ref.cost;
    }
};

vector<e_t> AL[20001];
int visited[20001];

int main() {
    scanf("%d %d", &V, &E);
    scanf("%d", &start);
    int a, b, c;
    for (int i=0; i<E; i++) {
        scanf("%d %d %d", &a, &b, &c);
        AL[a].push_back(e_t(b, c));
    }

    // processing
    priority_queue<e_t> pq; // cost에 대한 min heap

    for (int i=1; i<=V; i++) visited[i] = INF;
    visited[start] = 0;
    pq.push(e_t(start, 0));
    while (!pq.empty()) {
        e_t curr = pq.top();
        pq.pop();
        for (e_t next : AL[curr.node]) {
            int cost = curr.cost + next.cost;
            if (cost < visited[next.node]) {
                visited[next.node] = cost;
                pq.push(e_t(next.node, cost));
            }
        }
    }
    for (int i=1; i<=V; i++) {
        if (visited[i] == INF) {
            printf("INF\n");
            continue;
        }
        printf("%d\n", visited[i]);
    }


    return 0;
}