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