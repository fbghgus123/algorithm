#include <queue>

using namespace std;

int main() {
    queue<int> q;
    q.push(1);
    q.pop(); // 반환하지 않고 삭제만 함
    q.front(); // 큐 맨 앞 값 반환
    q.back(); // 큐 맨 뒷 값 반환
    q.size();
    q.empty(); // 큐 비어있는지 확인
}