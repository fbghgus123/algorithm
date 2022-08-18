// 문제 : https://www.acmicpc.net/problem/14003

#include <stdio.h>
#include <stack>
#include <vector>

using namespace std;

int n;
vector<int> lts;
int idxs[1000001], nums[1000001], p=0;

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
    for (int i=0; i<n; i++) {
        scanf("%d", &nums[i]);
        if (lts.empty() || lts.back() < nums[i]) {
            idxs[p++] = lts.size();
            lts.push_back(nums[i]);
        }
        else {
            int idx = lb(nums[i]);
            lts[idx] = nums[i];
            idxs[p++] = idx;
        }
    }

    printf("%d\n", lts.size());

    stack<int> st;
    int last = lts.size() - 1;
    for (int i=p-1; i>=0; i--) {
        if (idxs[i] == last) {
            st.push(nums[i]);
            last--;
        }
    }
    while(!st.empty()) {
        printf("%d ", st.top());
        st.pop();
    }
    puts("");
}