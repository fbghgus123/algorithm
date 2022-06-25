// 문제 : https://www.acmicpc.net/problem/1082

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>

#define MAX_SIZE 50

using namespace std;

int N, M, P[10];

vector<string> dp;

bool isZero(string tmp) {
    for (int i=0; i<tmp.size(); i++) {
        if (tmp[i] != 48) {
            return false;
        }
    }
    return true;
}

bool isBigger(string a, string b) {
    if (a == "-1") { return true; }
    if (b == "-1") { return false; }
    if (a.size() < b.size()) { return true; }
    if (a.size() > b.size()) { return false; }
    for (int i=0; i<a.size(); i++) {
        if (a[i] < b[i]) {
            return true;
        }
    }
    return false;
}

bool isBigger2(string a, string b) {
    if (isZero(a)) { a = "0"; }
    if (isZero(b)) { b = "0"; }
    return isBigger(a, b);
}

int main() {
    dp.push_back("-1");

    // input
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        scanf("%d", &P[i]);
    }
    scanf("%d", &M);

    for (int i=1; i<=M; i++) {
        string stillMax = dp[i-1];
        for (int j=0; j<N; j++) {
            string tmp = "-1";
            if (P[j] <= i) {
                if (dp[i-P[j]] == "-1") {
                    tmp = to_string(j);
                } else {
                    tmp = dp[i-P[j]] + to_string(j);
                }
                sort(tmp.begin(), tmp.end(), greater<>());
            
            }
            if (i != M) {
                if (isBigger(stillMax, tmp)) {
                    stillMax = tmp;
                }
            } else {
                if (isBigger2(stillMax, tmp)) {
                    stillMax = tmp;
                }
            }
        }
        dp.push_back(stillMax);
    }

    if (isZero(dp[dp.size() - 1])) { dp[dp.size() - 1] = "0"; }
    cout << dp[dp.size() - 1] << endl;
}