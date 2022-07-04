// 문제 : https://www.acmicpc.net/problem/9663

#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int answer = 0;
int N;
int grid[14][14];

void change(int n, int s, bool status) {
    if (status) {
        grid[n][s] = 9;
    } else {
        grid[n][s] = 0;
    }

    for (int i=1; i<N-n; i++) {
        if (status) {
            if (s-i >= 0) grid[n+i][s-i]++;
            grid[n+i][s]++;
            if (s+i < 14) grid[n+i][s+i]++;
        } else {
            if (s-i >= 0) grid[n+i][s-i]--;
            grid[n+i][s]--;
            if (s+i < 14) grid[n+i][s+i]--;
        }
    }
}

void btk(int n) {
    if (n == N) {
        // for (int i=0; i<N; i++) {
        //     for (int j=0; j<N; j++) {
        //         cout << grid[i][j] << " ";
        //     }
        //     cout << endl;
        // }
        // cout << endl;

        answer++;
        return;
    }

    for (int i=0; i<N; i++) {
        if (grid[n][i] == 0) {
            change(n, i, true);
            btk(n+1);
            change(n, i, false);
        }
    }
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> N;
    btk(0);
    cout << answer << endl;
}