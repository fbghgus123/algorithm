// 문제 : https://www.acmicpc.net/problem/1854

#include <stdio.h>
#include <queue>
#include <vector>

using namespace std;

struct n_t {
    int node;
    int cost;
    bool operator<(const n_t & ref) const {
        return this->cost > ref.cost;
    }
};

int N, M, K;
vector<n_t> AL[1001];
priority_queue<int> visited[1001];
priority_queue<n_t> pq;

int main() {
    scanf("%d %d %d", &N, &M, &K);
    int a, b, c;
    for (int i=1; i<=M; i++) {
        scanf("%d %d %d", &a, &b, &c);
        AL[a].push_back({b, c});
    }
    visited[1].push(0);
    pq.push({1, 0});
    while (!pq.empty()) {
        n_t curr = pq.top();
        pq.pop();
        for (n_t next : AL[curr.node]) {
            int ncost = curr.cost + next.cost;
            if (visited[next.node].size() == K && ncost < visited[next.node].top()) {
                visited[next.node].pop();
            }
            if (visited[next.node].size() < K) {
                visited[next.node].push(ncost);
                pq.push({next.node, ncost});
            }
        }

    }

    for (int i=1; i<=N; i++) {
        if (visited[i].size() < K) puts("-1");
        else printf("%d\n", visited[i].top());
    }
    return 0;
}