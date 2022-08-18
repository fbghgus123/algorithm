// 문제 : https://www.acmicpc.net/problem/6588

#include <stdio.h>

using namespace std;

bool arr[1000001];

int main() {
    for (int i=0; i<=1000000; i++) arr[i] = true;


    for (int i=2; i<=1024; i++) {
        for (int j=2; i*j <= 1000000; j++) {
            if (arr[i*j]) arr[i*j] = false;
        }
    }

    while (true) {
        int num;
        bool flag = true;
        scanf("%d", &num);
        if (num == 0) break;
        else {
            for (int i=3; i<num-1; i++) {
                if (arr[i] && arr[num-i]) {
                    printf("%d = %d + %d\n", num, i, num-i);
                    flag = false;
                    break;
                }
            }
            if (flag) printf("Goldbach's conjecture is wrong.\n");
        }
    }
}