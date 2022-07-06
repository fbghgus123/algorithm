#include <iostream>
#include <queue>

using namespace std;

int N;
priority_queue<int, vector<int>, less<int>> smallq;
priority_queue<int, vector<int>, greater<int>> bigq;

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> N;
    int mid;
    cin >> mid;
    for (int i=1; i<N; i++) {
        int num;
        cin >> num;

        if (num <= mid) {
            smallq.push(num);
        } else {
            bigq.push(num);
        }

        if (smallq.size() > bigq.size() + 1) {
            bigq.push(max(mid, num);
            mid = smallq.top();
            smallq.pop();
        }
        else if (smallq.size() + 1 < bigq.size()) {
            smallq.push(mid);
            mid = bigq.top();
            bigq.pop();
        }
        else {
            
        }
        cout << mid << endl;
    }
}