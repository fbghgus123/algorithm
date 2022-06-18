// 문제 : https://www.acmicpc.net/problem/1149

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    cin.ignore(256,'\n');

    vector<vector<int>> scores;
    vector<vector<int>> dp;
    for(int i=0; i<N; i++) {
        vector<int> score;
        for(int j=0; j<3; j++) {
            int tmp;
            cin >> tmp;
            score.push_back(tmp);
        }
        scores.push_back(score);
        
        vector<int> dptmp(3, 0);
        dp.push_back(dptmp);
    }

    dp[0] = scores[0];
    for (int i=1; i<N; i++) {
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + scores[i][0];
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + scores[i][1];
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + scores[i][2];
    }

    cout << min(min(dp[N-1][0], dp[N-1][1]), dp[N-1][2]) << endl;
    return 0;
}