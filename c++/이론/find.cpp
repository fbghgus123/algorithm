#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // 배열에서의 find
    int myints[] = {10, 20, 30, 40};
    int* p;

    p = find(myints, myints + 4, 30);
    
    //  벡터에서의 find
    vector<int> myvector (myints, myints + 4);
    vector<int>::iterator it;
    it = find(myvector.begin(), myvector.end(), 30);

    cout << it << endl;
}