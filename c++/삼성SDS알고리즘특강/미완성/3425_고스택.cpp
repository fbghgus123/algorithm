#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>

using namespace std;

void pop(stack<int>st) {
    st.pop();
}

void inv(stack<int>st) {
    int tmp = st.top();
    st.pop();
    st.push(-tmp);
}

void dup(stack<int>st) {
    st.push(st.top());
}

void swp(stack<int>st) {
    if (st.size() < 2) {
        cout << "ERROR" << endl;
        return;
    }
    int tmp1 = st.top();
    st.pop();
    int tmp2 = st.top();
    st.pop();
    st.push(tmp1);
    st.push(tmp2);
}

void add(stack<int>st) {
    if (st.size() < 2) {
        cout << "ERROR" << endl;
        return;
    }
    int tmp1 = st.top();
    st.pop();

    int tmp2 = st.top();
    st.pop();
    st.push(tmp1 + tmp2);
}

void sub(stack<int>st) {
    if (st.size() < 2) {
        cout << "ERROR" << endl;
        return;
    }
    int tmp1 = st.top();
    st.pop();

    int tmp2 = st.top();
    st.pop();
    st.push(tmp2 - tmp1);
}

void mul(stack<int>st) {
    if (st.size() < 2) {
        cout << "ERROR" << endl;
        return;
    }
    int tmp1 = st.top();
    st.pop();

    int tmp2 = st.top();
    st.pop();
    st.push(tmp1 * tmp2);
}

void div(stack<int>st) {
    if (st.size() < 2) {
        cout << "ERROR" << endl;
        return;
    }
    int tmp1 = st.top();
    st.pop();

    int tmp2 = st.top();
    st.pop();
    int result = abs(tmp2) / abs(tmp1);
    if ((tmp2 < 0 and tmp1 < 0) or (tmp2 >= 0 and tmp1 >= 0)) {
        st.push(result);
    } else {
        st.push(-result);
    }
}
void mod(stack<int>st) {
    if (st.size() < 2) {
        cout << "ERROR" << endl;
        return;
    }
    int tmp1 = st.top();
    st.pop();

    int tmp2 = st.top();
    st.pop();
    int result = abs(tmp2) % abs(tmp1);
    if (tmp2 < 0) {
        st.push(-result);
    } else {
        st.push(result);
    }
}


int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    bool flag = true;
    while (flag) {
        string cmd;
        queue<string> q;
        
        while (true) {
            cin >> cmd;
            if (cmd == "END") break;

            if (cmd == "NUM") {
                cin >> cmd;
            }

            if (cmd == "QUIT") {
                flag = false;
                break;
            }
            q.push(cmd);
        }
        if (!flag) break;

        int n;
        cin >> n;
        for (int i=0; i<n; i++) {
            int num;
            stack<int>st;
            queue<string> endq;
            bool ok = false;
            
            cin >> num;
            st.push(num);

            while(!q.empty()) {
                cmd = q.front();
                q.pop();
                endq.push(cmd);

                if (isdigit(cmd)) {
                    st.push(stoi(cmd));
                }
                
                if (cmd == "POP") {
                    if (st.size() < 1) {
                        ok = true;
                        break;
                    }
                    pop(st);
                }
                if (cmd == "INV") {
                    if (st.size() < 1) {
                        ok = true;
                        break;
                    }
                    inv(st);
                }
                if (cmd == "DUP") {
                    if (st.size() < 1) {
                        ok = true;
                        break;
                    }
                    dup(st);
                }
                if (cmd == "SWP") {
                    if (st.size() < 2) {
                        ok = true;
                        break;
                    }
                    swp(st);
                }
                if (cmd == "ADD") {
                    if (st.size() < 2) {
                        ok = true;
                        break;
                    }
                    add(st);
                }
                if (cmd == "SUB") {
                    if (st.size() < 2) {
                        ok = true;
                        break;
                    }
                    sub(st);
                }
                if (cmd == "MUL") {
                    if (st.size() < 2) {
                        ok = true;
                        break;
                    }
                    mul(st);
                }
                if (cmd == "DIV") {
                    if (st.size() < 2) {
                        ok = true;
                        break;
                    }
                    div(st);
                }
                if (cmd == "MOD") {
                    if (st.size() < 2) {
                        ok = true;
                        break;
                    }
                    mod(st);
                }
            }
            while(!q.empty()) {
                endq.push(q.front());
                q.pop();
            }
            q = endq;
            if (st.size() != 1 || ok) {
                cout << "ERROR" << endl;
                continue;
            }
            cout << st.top() << endl;
        }
    }
}