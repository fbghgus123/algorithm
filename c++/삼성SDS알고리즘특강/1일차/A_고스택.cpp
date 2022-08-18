// 문제 : https://www.acmicpc.net/problem/3425

#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <math.h>

#define MAX 1000000000

using namespace std;

bool isNumber(const string& str)
{
    for (char const &c : str) {
        if (std::isdigit(c) == 0) return false;
    }
    return true;
}

void run_program(int num, string cmd[], int count) {
    stack<long long> st;
    bool flag = false;
    st.push(num);

    for (int i=0; i<count; i++) {
        string current = cmd[i];
        if (isNumber(current)) {
            st.push(stoi(current));
        }

        if (current == "POP") {
            if (st.size() < 1) {
                flag = true;
                break;
            }
            st.pop();
        }

        if (current == "INV") {
            if (st.size() < 1) {
                flag = true;
                break;
            }
            long long tmp = st.top();
            st.pop();
            st.push(-tmp);
        }

        if (current == "DUP") {
            if (st.size() < 1) {
                flag = true;
                break;
            }
            long long tmp = st.top();
            st.push(tmp);
        }

        if (current == "SWP") {
            if (st.size() < 2) {
                flag = true;
                break;
            }
            long long tmp1 = st.top();
            st.pop();
            long long tmp2 = st.top();
            st.pop();
            st.push(tmp1);
            st.push(tmp2);
        }

        if (current == "ADD") {
            if (st.size() < 2) {
                flag = true;
                break;
            }
            long long tmp1 = st.top();
            st.pop();
            long long tmp2 = st.top();
            st.pop();
            long long tmp = tmp1 + tmp2;
            if (abs(tmp) > MAX) {
                flag = true;
                break;
            } else {
                st.push(tmp);
            }
        }

        if (current == "SUB") {
            if (st.size() < 2) {
                flag = true;
                break;
            }
            long long tmp1 = st.top();
            st.pop();
            long long tmp2 = st.top();
            st.pop();

            long long tmp = tmp2 - tmp1;
            if (abs(tmp) > MAX) {
                flag = true;
                break;
            } else {
                st.push(tmp);
            }
        }

        if (current == "MUL") {
            if (st.size() < 2) {
                flag = true;
                break;
            }
            long long tmp1 = st.top();
            st.pop();
            long long tmp2 = st.top();
            st.pop();
            long long tmp = tmp2 * tmp1;
            if (abs(tmp) > MAX) {
                flag = true;
                break;
            } else {
                st.push(tmp);
            }
        }

        if (current == "DIV") {
            if (st.size() < 2) {
                flag = true;
                break;
            }
            int tmp1 = st.top();
            st.pop();
            int tmp2 = st.top();
            st.pop();
            if (tmp1 == 0) {
                flag = true;
                break;
            }
            int tmp = abs(tmp2) / abs(tmp1);
            if ((tmp1 < 0 && tmp2 > 0) || (tmp1 > 0 && tmp2 < 0)) {
                st.push(-tmp);
            } else {
                st.push(tmp);
            }
        }

        if (current == "MOD") {
            if (st.size() < 2) {
                flag = true;
                break;
            }
            int tmp1 = st.top();
            st.pop();
            int tmp2 = st.top();
            st.pop();
            if (tmp1 == 0) {
                flag = true;
                break;
            }
            int tmp = abs(tmp2) % abs(tmp1);
            if (tmp2 < 0) {
                st.push(-tmp);
            } else {
                st.push(tmp);
            }
        }
    }
    if (st.size() != 1 || flag) {
        cout << "ERROR" << endl;
    } else {
        cout << st.top() << endl;
    }
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    while (true) {
        int count = 0;
        string cmd[100000];
        bool flag = false;

        // 명령어 입력
        while (true) {
            cin >> cmd[count];
            if (cmd[count] == "NUM") {
                cin >> cmd[count];
            }
            if (cmd[count] == "END") {
                break;
            }
            if (cmd[count] == "QUIT") {
                flag = true;
                break;
            }
            count++;
        }
        if (flag) break;

        int repeat;
        cin >> repeat;

        for (int i=0; i<repeat; i++) {
            int num;
            cin >> num;
            run_program(num, cmd, count);
        }
        cout << endl;
    }
}