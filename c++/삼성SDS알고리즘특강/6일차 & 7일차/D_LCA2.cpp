// 문제 : https://www.acmicpc.net/problem/11438

#include <stdio.h>
#include <vector>
#include <deque>

using namespace std;

int N, M; // N: 노드 개수, M: 질문의 개수
int a, b; // 입력 받은 노드 정보

int abs (int a) {
    return a < 0 ? -a : a;
}

vector<int> AL[100001]; // 인접 리스트
int depth[100001];

int parent[18][100001]; // [k][v] 현재 정점에서 2의 k제곱번째 부모의 정점 번호를 저장

int LCA(int, int);

int main() {
    scanf("%d", &N);
    for (int i=1; i<N; i++) {
        scanf("%d %d", &a, &b);
        // 인접 정보 입력
        AL[a].push_back(b);
        AL[b].push_back(a);
    }
    // bfs를 이용한 depth 구하기. 탐색의 시작은 Root node
    for (int i=1; i<=N; i++) depth[i] = -1;
    deque<int> q;
    q.push_back(1);
    depth[1] = 0;
    while (!q.empty()) {
        int curr = q.front();
        q.pop_front();
        for (int next : AL[curr]) {
            if (depth[next] == -1) { // 미방문 시 탐색
                q.push_back(next);
                depth[next] = depth[curr] + 1;
                parent[0][next] = curr;
            }
        }
    }

    // 점핑 테이블(희소 테이블)을 만들기
    for (int r=1; r<18; r++) {
        for (int i=1; i<=N; i++) {
            // parent[r][i]는 parent[r-1][i]의 2의 r-1제곱번째 부모
            parent[r][i] = parent[r-1][parent[r-1][i]];
        }
    }

    scanf("%d", &M);
    for (int i=0; i<M; i++) {
        scanf("%d %d", &a, &b);
        // a, b의 LCA 구하여 출력
        printf("%d\n", LCA(a, b));
    }
    return 0;
}

int LCA(int a, int b) {
    // 1. Depth 맞추기
    // 항상 a의 depth가 크도록 맞추고 시작
    if (depth[a] < depth[b]) {
        int tmp = a;
        a = b;
        b = tmp;
    }
    int diff = depth[a] - depth[b];
    for (int r=0; diff; r++) {
        if (diff & 1) {
            a = parent[r][a];
        }
        diff >>= 1;
    }
    // 2. LCA 찾기
    while (a != b) {
        int r;
        for (r=0; r<18; r++) {
            if (parent[r][a] == parent[r][b]) break;
        }
        if(r > 0) --r;
        a = parent[r][a]; 
        b = parent[r][b];
    }
    return a;
}