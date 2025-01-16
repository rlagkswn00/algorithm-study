#include <iostream>
#include <vector>
using namespace std;
int A[8];
bool used[8] = { 0, };
int cnt = 0;
int N, K;
int weight = 500;

void func(int cur) {
    if (cur == N) {
        cnt++;
        return;
    }
    for (int i = 0; i < N; i++) {
        if (used[i]) continue;
        int newWeight = weight - K + A[i];
        if (newWeight < 500) continue;
        used[i] = true;
        int oldWeight = weight;
        weight = newWeight;
        func(cur + 1);
        weight = oldWeight;
        used[i] = false;
    }
}

int main(void) {
    cin >> N >> K;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    func(0);

    cout << cnt;
}
