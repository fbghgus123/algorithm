#include <stdio.h>

using namespace std;

long long int k, c;

long long int gcd(long long int a, long long int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a%b);
}

long long int get_candy(long long int A, long long int B, long long int C, long long int D) {
    long long int first = c*A + k*B;
    long long int second = c*C + k*D;
    long long int mod = first % second;
    long long int quantity = first / second;

    printf("%lld %lld %lld\n%lld %lld %lld\n\n", A, B, first, C, D, second);

    long long int tmpC = A - C * quantity;
    long long int tmpD = B - D * quantity;

    if (mod == 1) {
        if (tmpC > 0) {
            return tmpC;
        } else {
            return C - tmpC;
        }
    } else {
        return get_candy(C, D, tmpC, tmpD);
    }
}

int main() {
    int t;
    scanf("%d", &t);

    for (int i=0; i<t; i++) {
        scanf("%lld %lld", &k, &c);
        if (gcd(k, c) != 1) {
            printf("IMPOSSIBLE\n");
        }
        else if (c == 1) {
            if (k == 1000000000) {
                printf("IMPOSSIBLE\n");
            } 
            else {
                printf("%lld\n", k+1);
            }
        }
        else {
            long long int ans =  get_candy(0, 1, 1, 0);
            if (ans > 1000000000) {
                printf("IMPOSSIBLE\n");
            } else {
                printf("%lld\n", ans);
            }
        }
    }
}