// 문제 : https://www.acmicpc.net/problem/13251

#include <stdio.h>
#include <vector>

#define ll long long int

using namespace std;

int M, K;
int N=0;
vector<int> stone;

int main() {
    scanf("%d", &M);
    for (int i=0; i<M; i++) {
        int num;
        scanf("%d", &num);
        stone.push_back(num);
        N += num;
    }
    scanf("%d", &K);

    double a=0, b=0, tmp=0;
    for (int i=0; i<stone.size(); i++) {
        tmp = 1.0;
        for (int j=0; j<K; j ++)
            tmp *= stone[i] - j;
        a += tmp;
    }
    b = 1.0;
    for (int i=0; i<K; i++) 
        b *= N - i;
    printf("%.15lf\n", (a/b));
    return 0;
}