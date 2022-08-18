// 문제 : https://www.acmicpc.net/problem/10828

#include <iostream>

using namespace std;

int N;
int stack[10000];
int pointer = -1;

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        string cmd;
        cin >> cmd;

        if (cmd == "push") {
            int num;
            cin >> num;
            stack[++pointer] = num;
        }
        else if (cmd == "pop") {
            if (pointer == -1) {
                cout << -1 << endl;
            } else {
                cout << stack[pointer--] << endl;
            }
        }
        else if (cmd == "size") {
            cout << pointer + 1 << endl;
        }
        else if (cmd == "empty") {
            if (pointer == -1) {
                cout << 1 << endl;
            } else {
                cout << 0 << endl;
            }
        }
        else {
            if (pointer == -1) {
                cout << -1 << endl;
            } else {
                cout << stack[pointer] << endl;
            }
        }
    }
}