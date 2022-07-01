#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compareWith (string a, string b) {
    if(a.length() == b.length())
        return a<b;
    return a.length()<b.length();
}

int main() {
    // sort(주소 시작, 주소 끝)

    // 배열 sort
    int arr[6] = {3, 4, 2, 5, 1};
    sort(arr, arr + 5);
    for (int i=0;i<5;i++) {
        cout << arr[i];
    }

    // 벡터 sort
    vector<int> v = {2, 3, 4, 5, 1};
    sort(v.begin(), v.end());
    for (int i=0;i<v.size();i++) {
        cout << v[i];
    }

    //원하는 대로 sort
    vector<string> vec;
    sort(vec.begin(), vec.end(), compareWith);

}