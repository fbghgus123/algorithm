// 문제 : https://www.acmicpc.net/problem/1516

#include <stdio.h>
#include <queue>
#include <vector>

using namespace std;

int N;
int times[501];
vector<int> path[501];
int degree[501];
int need[501];

int main() {
    scanf("%d", &N);
    for (int i=1; i<=N; i++) {
        degree[i] = 0;
    }
    for (int i=1; i<=N; i++) {
        scanf("%d", &times[i]);
        need[i] = times[i];
        while (true) {
            int tmp;
            scanf("%d", &tmp);
            if (tmp == -1) break;
            path[tmp].push_back(i);
            degree[i] += 1;
        }
    }
    
    queue<int> q;
    for (int i=1; i<=N; i++) {
        if (degree[i] == 0) q.push(i);
    }
    while (!q.empty()) {
        int c = q.front();
        q.pop();
        for (int i=0; i<path[c].size(); i++) {
            int next = path[c][i];
            degree[next] -= 1;
            need[next] = need[next] < need[c] + times[next] ? need[c]+times[next] : need[next];
            if (degree[next] == 0) {
                q.push(next);
            }
        }
    }
    for (int i=1; i<=N; i++) printf("%d\n", need[i]);
}