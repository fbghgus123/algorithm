#include <stdio.h>
#include <vector>

using namespace std;

int N, nums[50];
bool primeNumber[2001], avail[50];
int tmp;
vector<int> answer;

bool btk(int cnt) {
    if (cnt == N) {
        printf("아도!\n");
        return true;
    }
    for (int i=0; i<N; i++) {
        if (avail[i]) {
            avail[i] = false;
            for (int j=0; j<N; j++) {
                if (avail[j] && primeNumber[nums[j] + nums[i]]) {
                    // printf("%d %d\n", nums[i], nums[j]);
                    avail[j] = false;
                    if (btk(cnt+2)) {
                        avail[i] = true;
                        avail[j] = true;
                        return true;
                    };
                    avail[j] = true;
                }
            }
            avail[i] = true;
        }
    }
    return false;
}

void start() {
    avail[0] = false;
    int init = nums[0];
    for (int i=1; i<N; i++) {
        if (primeNumber[init + nums[i]]) {
            printf("가능 %d\n", nums[i]);
            avail[i] = false;
            if (btk(2)) answer.push_back(nums[i]);
            avail[i] = true;
        }
    }
}

int main() {
    scanf("%d", &N);
    for (int i=0; i<=2000; i++) primeNumber[i] = true;
    for (int i=0; i<50; i++) avail[i] = true;
    primeNumber[0] = primeNumber[1] = false;
    for (int i=2; i<=15; i++) {
        for (int j=i*2; j <= 2000; j+=i) primeNumber[j] = false;
    }

    for (int i=0; i<N; i++) scanf("%d", &nums[i]);
    start();

    if (answer.size() > 0) for (int i=0; i<answer.size(); i++) printf("%d ", answer[i]);
    else printf("-1");
}