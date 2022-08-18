// 문제 : https://www.acmicpc.net/problem/1837

#include <stdio.h>

using namespace std;

char P[100];
int K;
bool arr[1000001];
bool flag = true;

bool check (int n) {
    int sum =0;
    for (int i=0; P[i]; i++) {
        sum = (sum*10 + (P[i] - '0')) % n;
    }
    if (sum == 0) {
        return true;
    }
    return false;
}

int main() {
    scanf ("%s %d", &P, &K);

    for (int i=0; i<=1000000; i++) arr[i] = true;
    for (int i=2; i<1024; i++) {
        for (int j=2; j*i <= 1000000; j++) {
            if (arr[i*j]) arr[i*j] = false;
        }
    }

    for (int i=2; i<K; i++) {
        if (arr[i] && check(i)) {
            printf("BAD %d\n", i);
            flag = false;
            break;
        }
    }
    if (flag) {
        printf("GOOD\n");
    }
}