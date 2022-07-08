// 문제 : https://www.acmicpc.net/problem/15663

#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;
vector<int> nums;
int avail[10001];

void btk(vector<int> c) {
    if (c.size() == M) {
        for (int i=0; i<c.size(); i++) printf("%d ", c[i]);
        printf("\n");
    }
    else {
        for (int i=0; i<nums.size(); i++) {
            if (avail[nums[i]] > 0) {
                avail[nums[i]]--;
                c.push_back(nums[i]);
                btk(c);
                c.pop_back();
                avail[nums[i]]++;
            }    
        }
    }
}

int main() {
    scanf("%d %d", &N, &M);
    for (int i=0; i<10001; i++) avail[i] = 0;
    for (int i=0; i<N; i++) {
        int num;
        scanf("%d", &num);
        if (find(nums.begin(), nums.end(), num) == nums.end())
            nums.push_back(num);
        avail[num]++;
    }

    sort(nums.begin(), nums.end());
    btk({});
}