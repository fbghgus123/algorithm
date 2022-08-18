// 문제 : https://www.acmicpc.net/problem/2042

#include <stdio.h>

using namespace std;

int N, M, K;
int tmpN;

long long int tree[1024 * 1024 * 2];

void update(int a, long long int b) {
    int index = a + tmpN - 1;
    tree[index] = b;
    index = index >> 1;
    while (index > 0) {
        tree[index] = tree[index*2] + tree[index*2+1];
        index = index >> 1;
    }
}

long long int get_sum(int a, int b) {
    int left = a + tmpN - 1; // 시작 노드의 인덱스
    int right = b + tmpN - 1; // 끝 노드의 인덱스
    long long int sum = 0;
    while (left <= right) { // 서로 꼬이지 않는 한 반복
        // 왼쪽 노드가 오른쪽 자식에 있을 경우 (인덱스 값이 홀수인 경우) sum에 값을 추가
        if ((left & 1) == 1) {
            sum += tree[left];
        }
        // 오른쪽 노드가 왼쪽 자식에 있을 경우 (인덱스 값이 짝수인 경우) sum에 값을 추가
        if ((right & 1) == 0) {
            sum += tree[right];
        }
        left = (left+1) >> 1; // 부모 노드로 이동
        right = (right-1) >> 1; // 부모 노드로 이동
    }
    return sum;
}

int main() {
    scanf("%d %d %d", &N, &M, &K);
    for (tmpN = 1; tmpN<N; tmpN = tmpN << 1); // N 포함하는 2의 제곱 수 중 최대의 값으로 tmpN을 초기화 시켜줌
    for (int i=1; i<tmpN * 2; i++) tree[i] = 0; // 트리 전체 초기화

    for (int i=tmpN; i < tmpN + N; i++) { // 리프 노드 입력 받아서 채우기
        scanf("%lld", &tree[i]);
    }

    for (int i=tmpN-1; i > 0; i--) { // internal 노드 채우기
        tree[i] = tree[i*2] + tree[i*2+1];
    }

    long long int a, b, c;
    for (int i=0; i< M+K; i++) {
        scanf("%lld %lld %lld ", &a, &b, &c);
        // 업데이트
        if (a == 1) {
            update(b, c);
        } 
        // 출력
        else {
            printf("%lld\n", get_sum(b, c));
        }
    }
    return 0;
}