#include <stdio.h>
#include <vector>

using namespace std;

<<<<<<< HEAD
int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cout << "테스트" << endl;
=======
const int SIZE = (1 << 16);
int ALLVISITED;

int N;
int grid[15][15];
int dp[15][SIZE];

vector<int> answer;

void check() {
    for (int visited=1; visited<ALLVISITED; visited++) {
        // 하나 짜리 방문 패스
        for (int j=1; j < ALLVISITED; j = j<<1) {
            if (visited != 1 && visited == j) continue;
        }
        // 순회
        for (int curr=0; curr<N; curr++) {
            // 방문한 곳이라면,
            if (dp[curr][visited] != -1) {
                for (int k=0; k<N; k++) {
                    if (grid[curr][k] )
                    int isVisited = (1 << k) & visited;
                    int nextVisited = (1 << k) | visited;
                    if (!isVisited && dp[k][nextVisited] < dp[curr][visited] + 1) {
                        dp[k][nextVisited] = dp[curr][visited] + 1;
                    }
                }
            }
        }
    }
    
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            printf("%d ", dp[i][j]);
        }
        printf("\n");
    }
}

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            dp[i][j] = -1;
        }
    }
    dp[0][0] = 0;
    ALLVISITED = (1 << N) - 1;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            scanf("%1d", &grid[i][j]);
            if (!grid[i][j]) grid[i][j] = 200000000;
        }
    }
    check();
>>>>>>> 096890ae06b038bc437cba13e3ab3c561fd9cda0
}