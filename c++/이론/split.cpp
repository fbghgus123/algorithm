#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

vector<string> split (string s, string div) {
    vector<string> result;
    istringstream ss(s);
    string stringBuffer;
    while (getline(ss, stringBuffer, ',')) {
        result.push_back(stringBuffer);
    }
    return result;
}

int main() {
    string as = "this,is,string";
    vector<string> result = split(as, ",");

    for (int i=0;i<result.size();i++) {
        cout << result[i] << "\n";
    }
}