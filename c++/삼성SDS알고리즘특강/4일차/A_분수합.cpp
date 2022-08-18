// 문제 : https://www.acmicpc.net/problem/1735

#include <stdio.h>

using namespace std;

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a%b);
}

int main() {
    int a, b, c, d;
    scanf("%d %d", &a, &b);
    scanf("%d %d", &c, &d);

    int s, m;
    m = b * d;
    s = a*d + b*c;
    int g = gcd(m,s);
    while (g != 1) {
        m /= g;
        s /= g;
        g = gcd(m, s);
    }
    printf("%d %d\n", s, m);
}