#include <stdio.h>

using namespace std;

long long int k, c;

long long int gcd(long long int a, long long int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a%b);
}

long long extended_gcd(long long A, long long B){
    long long r, q, tmpA = A, t, t1 = 0, t2 = 1;
    while (B != 0){
        q = A / B;
        r = A%B;
        t = t1 - q*t2;
        A = B;
        B = r;
        t1 = t2;
        t2 = t;
    }
    while (t1<0) t1 += tmpA;
    return t1;
}

int main() {
    int t;
    scanf("%d", &t);

    for (int i=0; i<t; i++) {
        scanf("%lld %lld", &k, &c);

        if (c == 1) {
            if (k + 1 > 1e9)
                printf("IMPOSSIBLE\n");
            else
                printf("%lld\n", k + 1);
            continue;
        }
        else if (k == 1) {
            printf("1\n");
            continue;
        }
        else if (gcd(k, c) != 1) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        long long int ans =  extended_gcd(k, c);
        if (ans > ans > 1e9) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%lld\n", ans);
        }
    }
}