// 문제 : https://www.acmicpc.net/problem/7573

#include <stdio.h>
#include <vector>

using namespace std;

int N, I, M;
int p=0;
pair<int, int> web[50];
vector<pair<int, int>> fish;
int answer = 0;

int find_fish(int y, int x, pair<int, int> current_web) {
    int result = 0;
    int height = current_web.first;
    int width = current_web.second;

    if (x + width < N) {
        for (int i=0; i<=height; i++) {
            int tmp = 0;
            int tmpy = y-height+i;
            for (int j=0; j<fish.size(); j++) {
                int cy = fish[j].first;
                int cx = fish[j].second;
                if (tmpy <= cy && cy <= tmpy+height && x <= cx && cx <= x+width ) tmp++;
            }
            result = result < tmp ? tmp : result;
        }
    }
    return result;
}

void fishing(int y, int x) {
    for (int i=0; i<p; i++) {
        int tmp = find_fish(y, x, web[i]);
        answer = tmp > answer ? tmp : answer;
    }
}

int main() {
    scanf("%d %d %d", &N, &I, &M);
    for (int w=1; w<I/2; w++) {
        web[p++] = {w, I/2-w};
    }

    for (int i=0; i<M; i++) {
        int w, h;
        scanf("%d %d", &h, &w);
        fish.push_back({h-1, w-1});
    }

    for (int i=0; i<fish.size(); i++) {
        fishing(fish[i].first, fish[i].second);
    }
    printf("%d\n", answer);

}