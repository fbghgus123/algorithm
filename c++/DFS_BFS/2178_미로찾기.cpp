// 문제 : https://www.acmicpc.net/problem/2178

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    pair<int, int> s;
    cin >> s.first >> s.second;
    cin.ignore(256,'\n');
    

    vector<string> maze;
    vector<vector<int>> visited;
    for(int i=0; i<s.first; i++) {
        string tmp;
        getline(cin, tmp);
        maze.push_back(tmp);

        vector<int> vect(s.second, 0);
        visited.push_back(vect);
    }
    

    vector<vector<int>> queue;
    vector<int> start{0, 0, 1};
    queue.push_back(start);

    vector<int> dy = {0, 1, 0, -1};
    vector<int> dx = {1, 0, -1, 0};
    
    while (queue.size() > 0) {
        vector<int> tmp = queue.front();
        queue.erase(queue.begin());
        for(int i=0; i<4; i++) {
            int cy = tmp[0] + dy[i];
            int cx = tmp[1] + dx[i];
            int count = tmp[2];

            if (cy >= 0 && cx >= 0 && cy < s.first && cx < s.second) {
                if (cy == s.first - 1 && cx == s.second - 1) {
                    cout << count + 1 << endl;
                    return 0;
                }
                if (maze[cy][cx] == '1' && visited[cy][cx] == 0) {
                    vector<int> vect{cy, cx, count+1};
                    queue.push_back(vect);
                    visited[cy][cx] = 1;
                }
            }
        }
    }
}