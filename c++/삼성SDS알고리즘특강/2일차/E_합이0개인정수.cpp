// 문제 : https://www.acmicpc.net/problem/7453

#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

int N;
int a[4000], b[4000], c[4000], d[4000];
long arr1[16000000], arr2[16000000];

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> a[i] >> b[i] >> c[i] >> d[i];
    }

    long long  count = 0;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            arr1[count] = a[i] + b[j];
            arr2[count] = c[i] + d[j];
            count ++;
        }
    }

    sort(arr1, arr1+N*N);
    sort(arr2, arr2+N*N, greater<int>());

    int p1 = 0;
    int p2 = 0;
    count = 0;

    while (p1 < N*N && p2 < N*N) {
        int tmp = arr1[p1] + arr2[p2];
        if (tmp == 0) {
            long long  c1 = 1;
            long long  c2 = 1;
            while (p1 < N*N-1 && arr1[p1] == arr1[p1+1]) {
                p1++;
                c1++;
            }
            while (p2 <N*N-1 && arr2[p2] == arr2[p2+1]) {
                p2++;
                c2++;
            }
            count += c1 * c2;
            if (c1 * c2 == 1) {
                if (p1 < N*N-1 && arr1[p1+1] + arr2[p2] == 0) count ++;
                if (p2 < N*N-1 && arr1[p1] + arr2[p2+1] == 0) count ++;    
            }
            p1++;
            p2++;
        }
        else if (tmp < 0) {
            p1++;
        }
        else {
            p2++;
        }
    }
    cout << count << endl;
}