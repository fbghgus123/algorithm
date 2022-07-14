// 문제 : https://www.acmicpc.net/problem/12015

#include <stdio.h>
#include <vector>

using namespace std;

int n;
vector<int> lts;

int lb(int num) {
    int l = 0, r = lts.size()-1;
    int mid, result = lts.size();

    while (l <= r) {
        mid = (l+r) / 2;
        if (lts[mid] >= num) {
            result = mid < result ? mid : result;
            r = mid - 1;
        }
        else {
            l = mid + 1;
        }
    }
    return result;
}

int main() {
    scanf("%d", &n);
    int num;
    for (int i=0; i<n; i++) {
        scanf("%d", &num);
        if (lts.empty() || lts.back() < num) {
            lts.push_back(num);
        }
        else {
            int idx = lb(num);
            lts[idx] = num;
        }
    }


    // for (int i=0; i<lts.size(); i++) printf("%d ", lts[i]);
    printf("%d\n", lts.size());
    // printf("%d\n", lb(11));
}