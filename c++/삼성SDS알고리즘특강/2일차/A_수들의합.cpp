// 문제 : https://www.acmicpc.net/problem/2003

#include <iostream>

using namespace std;

int N, M;
int A[10001];

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }

    int start = 0;
    int end = 0;
    int sum = 0;
    int count = 0;

    while (end <= N) {
        if (sum < M) {
            sum += A[end++];
        } 
        else if (sum > M) {
            sum -= A[start++];
        }
        else {
            count += 1;
            sum -= A[start++];
        }
    }
    cout << count << endl;
}