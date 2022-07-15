// 문제 : https://www.acmicpc.net/problem/1197
// 프림 알고리즘 사용

#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

int v, e;
int visited[10001];
struct edge {
    int end;
    int v;
    bool operator<(const edge &ref) const {
        return this->v > ref.v;
    }
};

vector<edge> E[10001];
int sum = 0;

int main() {
    scanf("%d %d", &v, &e);
    int a, b, c;
    for (int i=0; i<e; i++) {
        scanf("%d %d %d", &a, &b, &c);
        E[a].push_back({b, c});
        E[b].push_back({a, c});
    }

    priority_queue<edge> pq;
    pq.push({1, 0});
    while (!pq.empty()) {
        edge curr = pq.top();
        pq.pop();
        if (visited[curr.end] == 0) {
            visited[curr.end] = 1;
            sum += curr.v;
            for (edge next : E[curr.end]) {
                pq.push(next);
            }
        }
    }
    printf("%d\n", sum);
    return 0;
}