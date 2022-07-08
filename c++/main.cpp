#include <stdio.h>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int N;
int height[50][50];
int low = 1000000; int high = 0;
int answer = 1000000;
pair<int, int> home;
vector<pair<int, int>> target;

int dy[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dx[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

bool bfs(int minn, int maxx) {
    if (minn > height[home.first][home.second]) return false;
    int visited[50][50];
    for (int i=0; i<50; i++) for(int j=0; j<50; j++) visited[i][j] = 0;
    queue<pair<int ,int>> q;
    q.push(home);

    while (!q.empty()) {
        pair<int, int> tmp = q.front();
        q.pop();

        int y = tmp.first;
        int x = tmp.second;
        for (int i=0; i<8; i++) {
            int cy = y + dy[i];
            int cx = x + dx[i];
            // 범위 확인
            if (0 <= cy && 0 <= cx && cy < N && cx < N) {
                // 방문 가능 체크
                if (visited[cy][cx] == 0 && height[cy][cx] >= minn && height[cy][cx] <= maxx) {
                    visited[cy][cx] = 1;
                    q.push({cy, cx});
                }
            }
        }
    }
    for (int i=0; i<target.size(); i++) {
        pair<int, int> t = target[i];
        if (!visited[t.first][t.second]) {
            return false;
        };
    }
    return true;
}

int find_maxx(int l) {
    int r = high+1;
    int mid;
    int answer = 1000001;
    while (l <= r) {
        mid = (l + r) / 2;
        if (bfs(low, mid)) {
            if (answer > mid) answer = mid;
            r = mid - 1;
        }
        else {
            l = mid + 1;
        }
    }
    return answer;
}

int find_minn(int r) {
    int l = low;
    int answer = l, mid;
    while (l <= r) {
        mid = (l + r) / 2;
        if (bfs(mid, r)) {
            answer = mid;
            l = mid + 1;
        }
        else {
            r = mid - 1;
        }
    }
    return answer;
}

void find_answer() {
    int l; int h;
    while (low <= high) {
        h = find_maxx(low);
        if (h == 1000001) break;
        l = find_minn(h);
        int tmp = h - l;
        if (tmp < answer) answer = tmp;
        
        high = h;
        low = l + 1;
    }
    printf("%d\n", answer);
}

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        char str[N];
        scanf("%s", str);
        for (int j=0; j<N; j++) {
            if (str[j] == 'K') target.push_back({i, j});
            if (str[j] == 'P') home = {i, j};
        }
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            scanf("%d", &height[i][j]);
            if (low > height[i][j]) low = height[i][j];
            if (high < height[i][j]) high = height[i][j];
        }
    }
    find_answer();
    return 0;
}