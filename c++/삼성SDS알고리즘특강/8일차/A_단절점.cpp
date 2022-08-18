// 문제 : https://www.acmicpc.net/problem/11266

#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int V, E, a, b;
vector<int> AL[10001];
int visit_order[10001]; // 미방문 0, 방문 순서 저장
int cut_vertext[10001]; // 각 정점의 단절점 여부

int answer[10001], s_ans; // 출력할 단절점 정보와 개수

int order; // 방문 순서
int dfs(int, int);

int main() {
    scanf("%d %d", &V, &E);

    for (int i=0; i<E; i++) {
        scanf("%d %d", &a, &b);
        AL[a].push_back(b);
        AL[b].push_back(a);
    }

    // 주어진 그래프가 연결 그래프가 아니므로 for문으로 하나씩 체크
    for (int i = 1; i<= V; i++) {
        if (visit_order[i] == 0) dfs(i, 0);
    }

    // 단절점 정보 출력
    for (int i=1; i<=V; i++) {
        if (cut_vertext[i] == 1) {
            answer[s_ans++] = i;
        }
    }
    sort(answer, answer + s_ans);
    printf("%d\n", s_ans);
    for (int i=0; i<s_ans; i++) printf("%d ", answer[i]);
    puts("");
    return 0;
}

int dfs(int curr, int parent) {
    visit_order[curr] = ++order; // 방문 order 저장

    // 내 부모에게 넘겨줄 low (현재 나의 return 값) 저장하는 변수
    // 나와 연결된 점을 방문했을 때, 방문한 연결점이 방문했던 점들 중 order가 가장 빠른 것
    int minOrder = visit_order[curr];
    int child = 0;

    // 다음 방문 예정인 점을 탐색
    for (int next : AL[curr]) {
        if (next == parent) continue; // 부모 노드로는 돌아가지 않겠당
        // 루트 노드인 경우
        if (visit_order[next] > 0) { // next를 이미 방문한 경우
            minOrder = visit_order[next] < minOrder ? visit_order[next] : minOrder;
        }
        else { // next가 미방문인 경우
            ++child;
            int low = dfs(next, curr);
            // 현재 노드가 유일한 통로인 경우 단절점 표시(자식 노드의 가장 낮은 값이 나보다 크거나 같아야함)
            // 루트 노드인 경우 항상 참
            if (parent != 0 && visit_order[curr] <= low) cut_vertext[curr] = 1;
            minOrder = low < minOrder ? low : minOrder;
        }
    }
    if (parent == 0 && child > 1) {
        cut_vertext[curr] = 1;
    }
    return minOrder;
}