// 문제 : https://www.acmicpc.net/problem/18870

#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

int N;
int a[1000000];
int m[1000000];

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> a[i];
    }

    copy(a, a+N, m);
    sort(m, m+N);
    
    map<int, int> s;
    int count = 0;
    
    for (int i=0; i<N; i++) {
        s[m[i]] = count;
        if (i != N-1 && m[i] != m[i+1]) {
            count ++;
        }
    }

    for (int i=0; i<N; i++) {
        int num = a[i];
        cout << s[num] << " ";
    }
    cout << endl;
}