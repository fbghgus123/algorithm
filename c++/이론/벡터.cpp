#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> v;
    for (int i=0;i<N;i++) {
        int a;
        cin >> a;
        v.push_back(a);
    }
    for (int i=0; i<v.size();i++) {
        cout << v[i];
    }

    /*
    vector<int>v; : int 타입을 요소로 가지는 벡터 v 선언
    v.push_back(a) : 벡터 v의 맨 뒤에 a 추가
    v.pop_back() : 벡터 v의 맨 뒤 요소 삭제
    v.size() : 벡터 v의 크기 반환
    v.begin() : v의 첫 번째 요소의 주소
    v.end() : v의 마지막 요소의 주소
    */
}