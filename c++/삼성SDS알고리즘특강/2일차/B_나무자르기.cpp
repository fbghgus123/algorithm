#include <iostream>
#include <algorithm>

using namespace std;

long N, M;
long tree[1000001];
long maxx = 0;

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> tree[i];
        maxx = max(tree[i], maxx);
    }

    long left = 0;
    long right = maxx;
    long mid;

    while (left <= right) {
        mid = (left + right) / 2;
        
        long earn = 0;
        for (int i=0; i<N; i++) {
            earn += max(long(0), tree[i] - mid);
        }

        if (earn == M) { break; }

        if (earn > M) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    int earn = 0;
    for (int i=0; i<N; i++) {
        earn += max(long(0), tree[i] - mid);
    }
    if (earn < M) {
        cout << mid - 1 << endl;
    } else {
        cout << mid << endl;
    }
}