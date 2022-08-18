// 문제 : https://www.acmicpc.net/problem/1644

#include <stdio.h>

using namespace std;

bool arr[4000001];
int prime[4000001];
int pointer = 0;

int main() {
    for (int i=0; i<=4000000; i++) arr[i] = true;

    for (int i=2; i<=2048; i++) {
        for (int j=2; i*j <= 4000000; j++) {
            if (arr[i*j]) arr[i*j] = false;
        }
    }

    int N;
    scanf("%d", &N);

    for (int i=2; i<4000000; i++) {
        if (arr[i]) {
            prime[pointer++] = i;
        }
        if (i > N) {
            break;
        }
    }

    int p1=0; int p2=0; int sum=2; int count=0;
    if (N == 1) {
        printf("0");
    } 
    else {
        while (p2 < pointer) {
            if (sum > N) sum -= prime[p1++];
            else if (sum < N) sum += prime[++p2];
            else {
                count++;
                sum += prime[++p2];
            }
        }
        printf("%d\n", count);
    }
}