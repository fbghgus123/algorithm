// 문제 : https://www.acmicpc.net/problem/5569

#include <stdio.h>

using namespace std;

int w, h;
long long int grid[4][101][101];

// 0: 방향O 북 / 1: 방향O 동 / 2: 방향 X 북 / 3: 방향 X 동

int main() {
    scanf("%d %d", &w, &h);
    grid[0][0][0] = 1;
    for (int i=1; i<h; i++) grid[0][i][0] = 1;
    for (int i=1; i<w; i++) grid[1][0][i] = 1;
    for (int i=1; i<h; i++) {
        for (int j=1; j<w; j++) {
            grid[0][i][j] = (grid[0][i-1][j] + grid[2][i-1][j]) % 100000;
            grid[1][i][j] = (grid[1][i][j-1] + grid[3][i][j-1]) % 100000;
            grid[2][i][j] = grid[1][i-1][j] % 100000;
            grid[3][i][j] = grid[0][i][j-1] % 100000;
        }
    }
    printf("%lld\n", (grid[0][h-1][w-1] + grid[1][h-1][w-1] + grid[2][h-1][w-1] + grid[3][h-1][w-1])%100000);
}