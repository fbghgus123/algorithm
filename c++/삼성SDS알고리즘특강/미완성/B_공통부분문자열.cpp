#include <stdio.h>
#include <string>

using namespace std;

char a[4000];
char b[4000];

string A;
string B;
int dp[4000];

int main() {
    int answer = 0;
    scanf("%s", &a);
    scanf("%s", &b);
    A = a;
    B = b;

    for (int i=0; i<B.size(); i++) {
        if (A[0] == B[i]) dp[i] = 1;
    }

    for (int i=1; i<A.size(); i++) {
        char prev = A[i-1];
        char curr = A[i];
        int tmp;
        for (int j=1; j<B.size(); j++) {
            if (curr == B[j]) {
                if (prev == B[j-1]) dp[j] = dp[j] > dp[j-1]+1 ? dp[j] : dp[j-1]+1;
                else dp[j] = dp[j] > 1 ? dp[j] : 1;
                answer = dp[j] > answer ? dp[j] : answer;
            } 
        }
    }
    printf("%d\n", answer);
}