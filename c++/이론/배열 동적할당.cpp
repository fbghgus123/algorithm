#include <iostream>
#include <vector>
using namespace std;

int main() {
    // 1차원 배열 동적할당
    int N;
    cin >> N;
    int* arr = new int[N];
    delete[] arr;

    // 2차원 배열 동적할당
    int r, c;
    cin >> r >> c;

    int** arr;
    arr = new int* [r];
    for (int i=0;i<r;i++) {
        arr[i] = new int[c];
    }
    
    for (int i=0;i<r;i++) 
        delete[] arr[i];
    delete[] arr;
}