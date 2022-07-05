#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>

using namespace std;

int N;
char grid[50][50];
int height[50][50];
int minn = 1000000;
int maxx = 0;

pair<int, int> direction[8] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}};

vector<pair<int, int>> target;
pair<int, int> start;

bool bfs(int l, int r) {
    int visited[N][N];
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            visited[i][j] = 0;
        }
    }

    queue<pair<int, int>> q;
    q.push(start);
    visited[start.first][start.second] = 1;
    while (!q.empty()) {
        pair<int, int> tmp = q.front();
        q.pop();

        int y = tmp.first;
        int x = tmp.second;
        for (int i=0; i<8; i++) {
            int dy = y + direction[i].first;
            int dx = x + direction[i].second;
            if (0 <= dy && 0 <= dx && dy < N && dx < N) {
                if (visited[dy][dx] == 0 && height[dy][dx] <= r && height[dy][dx] >= l) {
                    visited[dy][dx] = 1;
                    q.push({dy, dx});
                }
            }
        }
    }

    for (int i=0; i<target.size(); i++) {
        pair<int, int> p = target[i];
        if (visited[p.first][p.second] == 0) {
            return false;
        }
    }
    return true;
}

int two_pointer_end (int l, int r) {
    int s = l;
    int result = -1;
    int mid;
    while (l <= r) {
        mid = (l+r)/2;
        bool flag = bfs(s, mid);

        if (flag) {
            result = mid;
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    return result;
}

int two_pointer_start (int l, int r) {
    int e = r;
    int result = -1;
    int mid;
    while (l <= r) {
        mid = (l+r)/2;
        bool flag = bfs(mid, e);

        if (flag) {
            result = mid;
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }

    return result;
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> grid[i][j];
            if (grid[i][j] == 'P') {
                start = {i, j};
            }
            else if (grid[i][j] == 'K') {
                target.push_back({i, j});
            }
        }
    }

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> height[i][j];
            minn = min(minn, height[i][j]);
            maxx = max(maxx, height[i][j]);
        }
    }

    int l = minn;
    int r = minn;
    int answer = 1000000;
    
    while (l <= height[start.first][start.second] && r <= maxx && l <= r) {
        int lmp, rmp;
        int flag1 = false;
        if (bfs(l, r)) {
            answer = min(answer, r-l);
            lmp = two_pointer_start(minn, r);
            flag1 = true;
        } else {
            rmp = two_pointer_end(l, maxx);
        }

        if (flag1) {
            if (lmp == l) r++;
            else l = lmp;
        } else {
            if (rmp == -1) {
                r++;
            } else {
                r = rmp;
            }
        }
    }
    cout << answer << endl;
}