#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

int N;

pair<int, int> arr[1000];
int p = 0;

int find_less(int myday) {
    int result = 0;
    for (int i=0; i<p; i++) {
        if (arr[i].first <= myday) {
            result++;
        }
    }
    return result;
}

struct cmp {
    bool operator()(pair<int, int> a, pair<int, int> b) {
        return a.second < b.second;
    }
};

priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> q;

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        pair<int, int> tmp;
        scanf("%d %d",&tmp.first, &tmp.second);
        q.push(tmp);
    }
    int day = 1, answer = 0;
    while (!q.empty()) {
        pair<int, int> tmp = q.top();
        q.pop();

        if (tmp.first - find_less(tmp.first) > day && q.size() > 0) {
            arr[p++] = tmp;
        }
        else {
            if (tmp.first >= day) {
                answer += tmp.second;
                day ++;
                while (p > 0) {
                    q.push(arr[--p]);
                }
            }
        }
        if (q.empty() && p > 0) {
            while (p > 0) {
                q.push(arr[--p]);
            }
        }
    }
    printf("%d\n", answer);
    return 0;
}