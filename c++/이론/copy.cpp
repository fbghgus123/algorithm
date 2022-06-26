// copy는 알고리즘 인클루드 해줘야함
#include <algorithm>
#include <vector>

// arr 을 target 배열에다가 복사할 예정
// copy(복사 배열 시작지점, 복사 배열 끝 지점, 복사할 곳)
using namespace std;

int main() {
    // 1차원 배열 복사
    int arr[10];
    int target[10];
    copy(arr, arr + 10, target[0]);

    // 2차원 배열 복사
    int arr2[10][10];
    int target2[10][10];
    copy(arr2[0][0], arr2[0][0] + 100, target2[0][0]);

    // 벡터 복사
    vector<int> a;
    vector<int> t;
    copy(a.begin(), a.end(), t.begin());
}


