// 문제 : https://www.acmicpc.net/problem/1039

#include <iostream>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;

string N;
int maxx = 0;
int K;
int visited[1000001][10];

string swap(string s, int i, int j) {
    char tmp = s[j];
    s[j] = s[i];
    s[i] = tmp;
    return s;
}

void bfs(string s) {
    int len = s.size();
    if (len < 2) {
        maxx = -1;
        return ;
    }
    queue<pair<string, int>> q;
    q.push({s, 0});

    while (!q.empty()) {
        pair<string, int> tmp = q.front();
        q.pop();

        string str = tmp.first;
        int count = tmp.second;

        if (count == K) {
            if (maxx < stoi(str)) maxx = stoi(str);
            continue;
        }

        for (int i=0; i<len-1; i++) {
            for (int j=i+1; j<len; j++) {
                string tmp = swap(str, i, j);
                int a = stoi(tmp);
                if (tmp[0] == '0' || visited[a][count] == 1) continue;
                visited[a][count] = 1;
                q.push({tmp, count + 1});
            }
        }
    }
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    for (int i=1; i<1000001; i++) {
        for (int j=0; j<10; j++) {
            visited[i][j] = 0;
        }
    }
    
    cin >> N >> K;
    bfs(N);
    if (maxx == 0) maxx = -1;
    cout << maxx << endl;
}