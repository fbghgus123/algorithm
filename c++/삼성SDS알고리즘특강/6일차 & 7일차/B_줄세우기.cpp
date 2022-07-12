// 문제 : https://www.acmicpc.net/problem/2252

#include <stdio.h>
#include <queue>

using namespace std;

int N, M;
int degree[32001];

int main () {
    scanf("%d %d", &N, &M);
    vector<int> path[N+1];
    for (int i=1; i<=N; i++) degree[i] = 0;
    for (int i=0; i<M; i++) {
        int A, B;
        scanf("%d %d", &A, &B);
        path[A].push_back(B);
        degree[B] += 1;
    }

    queue<int> q;
    for (int i=1; i<=N; i++) {
        if (degree[i] == 0) q.push(i);
    }
    while (!q.empty()) {
        int index = q.front();
        printf("%d ", index);
        q.pop();

        for (int i=0; i<path[index].size(); i++) {
            int next = path[index][i];
            degree[next] -= 1;
            if (degree[next] == 0) {
                q.push(next);
            }
        }
    }
}