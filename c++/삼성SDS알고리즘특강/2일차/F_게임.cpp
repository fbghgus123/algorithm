// 문제 : https://www.acmicpc.net/problem/1072

#include <iostream>
#include <algorithm>

using namespace std;

long x, y;

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> x >> y;
    long rate = (y*100/ x) ;

    int left = 1;
    int right = x;
    int mid;
    int answer = -1;
    while (left <= right) {
        mid = (left + right) / 2;
        int tmp = (y + mid)* 100 / (x + mid);

        if (tmp <= rate) {
            left = mid + 1;
        } else {
            answer = mid;
            right = mid - 1;
        }
    }
    cout << answer << endl;
}