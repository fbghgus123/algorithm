// 문제 : https://www.acmicpc.net/problem/10845

#include <iostream>

using namespace std;

int queue[10000];
int p1 = 0;
int p2 = 0;

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    int N;
    cin >> N;
    for (int i=0; i<N; i++) {
        string cmd;
        cin >> cmd;

        if (cmd == "push") {
            cin >> queue[p2++];
        }
        else if (cmd == "front") {
            if (p1 == p2) {
                cout << -1 << endl;
            }
            else { 
                cout << queue[p1] << endl;
            }
        }
        else if (cmd == "back") {
            if (p1 == p2) {
                cout << -1 << endl;
            }
            else {
                cout << queue[p2-1] << endl;
            }
        }
        else if (cmd == "pop") {
            if (p1 == p2) {
                cout << -1 << endl;
            } else {
                cout << queue[p1++] << endl;
            }
        }
        else if (cmd == "size") {
            cout << p2 - p1 << endl;
        }
        else {
            if (p1 == p2) {
                cout << 1 << endl;
            } else {
                cout << 0 << endl;
            }
        }
    }
}