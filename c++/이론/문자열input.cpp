#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // input은 처음 개수 N 과 N 개의 문자열을 입력받는다고 가정한다.
    int N;
    cin >> N;

    // 문자열을 cin으로 받게 되면 공백으로 끊어져서 입력받게 되는데,
    // 이때는 getline()을 사용하면 효율적이다.
    // 하지만 getline 이전에 cin을 사용하였다면, 버퍼를 없애줘야하는데
    cin.ignore(256,'\n');
    // 위 코드를 getline 이전에 한 번 사용해주면 된다.
    for(int i=0; i<N; i++) {
        string tmp;
        getline(cin, tmp);
    }
}