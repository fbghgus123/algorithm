#include <iostream>

using namespace std;

int arr[1000001];
int p = 1;

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    int N;
    cin >> N;
    for (int i=0; i<N; i++) {
        int num;
        cin >> num;
        // 삽입
        if (num > 0) {
            int current = p;
            arr[p++] = num;
            
            while (current != 0) {
                int next = (current >> 1);
                if (arr[current] < arr[next]) {
                    swap(arr[current], arr[next]);
                    current = next;
                } else {
                    break;
                }
            }
        } 
        // 삭제
        else {
            // 힙이 비어 있는 경우
            if (p == 1) {
                cout << 0 << endl;
            } 
            else {
                // 루트 노드 출력
                cout << arr[1] << endl;

                // 루트 노드에 마지막 노드를 삽입
                arr[1] = arr[--p];
                int current = 1;
                // 자녀가 존재하는 경우
                while (current * 2 < p) {
                    int leftchild = current * 2; int rightchild = current * 2 + 1;
                    // 자녀가 2개 존재하는 경우
                    if (rightchild < p) {
                        // 왼쪽 자녀가 더 작은 경우 왼쪽 자식과 교체
                        if (arr[leftchild] < arr[current] && arr[leftchild] < arr[rightchild]) {
                            swap(arr[leftchild], arr[current]);
                            current = leftchild;
                        }
                        // 오른쪽 자식이 더 작은 경우 오른쪽 자식과 교체
                        else if (arr[rightchild] < arr[current] && arr[leftchild] >= arr[rightchild]) {
                            swap(arr[rightchild], arr[current]);
                            current = rightchild;
                        }
                        else {
                            break;
                        }
                    }
                    // 자녀가 1개 존재하는 경우 자식과 교체
                    else if (arr[current] > arr[leftchild]) {
                        swap(arr[current], arr[leftchild]);
                        current = leftchild;
                    } // 현재 노드가 더 작거나 같은 경우     
                    else {
                        break;
                    }
                }
            }
        }
    }
}