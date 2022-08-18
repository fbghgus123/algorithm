// 문제 : https://www.acmicpc.net/problem/2748

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    int n;
    cin >> n;
    
    long long mem[100];
    mem[0] = 0;
    mem[1] = 1;
    for (int i=2; i<=90; i++) {
        mem[i] = mem[i-1] + mem[i-2];
    }

    cout << mem[n] << endl;
}