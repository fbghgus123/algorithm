// 문제 : https://www.acmicpc.net/problem/2749

#include <iostream>
#include <algorithm>

using namespace std;

unsigned long long n;

struct matrix {
    bool empty = true;
    unsigned long long v[2][2];
};

// 행렬의 곱셈
matrix cal(matrix a, matrix b) {
    matrix result;
    result.empty = false;
    result.v[0][0] = (a.v[0][0] * b.v[0][0] + a.v[0][1] * b.v[1][0]) % 1000000;
    result.v[0][1] = (a.v[0][0] * b.v[0][1] + a.v[0][1] * b.v[1][1]) % 1000000;
    result.v[1][0] = (a.v[1][0] * b.v[0][0] + a.v[1][1] * b.v[1][0]) % 1000000;
    result.v[1][1] = (a.v[1][0] * b.v[0][1] + a.v[1][1] * b.v[1][1]) % 1000000;
    return result;
}

matrix m[60];

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n;
    if (n < 3) {
        cout << 1 << endl;
    } 
    else if (n == 3) {
        cout << 2 << endl;
    }
    else {
        // 초기행렬 tmp
        matrix tmp;
        tmp.empty = false;
        tmp.v[0][0] = 1;
        tmp.v[0][1] = 1;
        tmp.v[1][0] = 1;
        tmp.v[1][1] = 0;
        m[0] = tmp;
        
        // 필요 항 2진수로 나타냄
        string str = "";
        n -= 2;
        while (n != 0) {
            int last = n % 2;
            n /= 2;
            str += last + '0';
        }

        matrix answer;
        if (str[0] == '1') {
            answer = tmp;
        }
        for (int i=1; i<str.size(); i++) {
            m[i] = cal(m[i-1], m[i-1]);
            // 필요 항이면 정답에 추가6
            if (str[i] == '1') {
                if (answer.empty) {
                    answer.empty = false;
                    answer = m[i];
                } else {
                    answer = cal(answer, m[i]);
                }
            }
        }
        cout << (answer.v[0][0] + answer.v[0][1]) % 1000000 << endl;
    }    
}