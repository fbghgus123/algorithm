// 문제 : https://www.acmicpc.net/problem/2492

#include <stdio.h>
#include <vector>

using namespace std;

int N, M, T, K;
int answer = 0;
int ay, ax;
pair<int, int> stone[100];

int find_stone(int y, int x) {
    int result = 0;
    for (int i=0; i<T; i++) {
        if (y <= stone[i].first && stone[i].first <= y+K && x <= stone[i].second && stone[i].second <= x + K) {
            result ++;
        }
    }
    return result;
}

int main() {
    scanf("%d %d %d %d", &N, &M, &T, &K);
    for (int i=0; i<T; i++) {
        int y, x;
        scanf("%d %d", &x, &y);
        stone[i] = {y, x};
    }

    for (int i=0; i<T; i++) {
        for (int j=0; j<T; j++) {
            int yy, xx;
            if (stone[i].first + K > M) yy = M - K;
            else yy = stone[i].first;
            if (stone[i].second + K > N) xx = N - K;
            else xx = stone[i].second;
            int a = find_stone(yy, xx);
            if (answer < a) {
                answer = a;
                ay = yy+K;
                ax = xx;
            }
        }
    }
    printf("%d %d\n", ax, ay);
    printf("%d\n", answer);
}