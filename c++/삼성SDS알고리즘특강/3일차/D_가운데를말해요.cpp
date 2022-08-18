// 문제 : https://www.acmicpc.net/problem/1655

#include <stdio.h>
#include <queue>

using namespace std;

int N;
priority_queue<int, vector<int>, less<int>> smallq;
priority_queue<int, vector<int>, greater<int>> bigq;

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        int num;
        scanf("%d", &num);

        if (smallq.empty()) smallq.push(num);
        else if (num > smallq.top()) {
            bigq.push(num);
        } 
        else {
            smallq.push(num);
        }

        if (smallq.size() < bigq.size()) {
            smallq.push(bigq.top());
            bigq.pop();
        }
        else if (smallq.size() > bigq.size()+1) {
            bigq.push(smallq.top());
            smallq.pop();
        }
        printf("%d\n", smallq.top());
    }
}