#include <iostream>
using namespace std;

int prices[10][10];
bool used[10][10] = { 0, };

int N;
int ans = 200 * 5 * 3; //지점당 최댓값 200
int sum = 0;

int dx[] = { 0, 0, 0, 1, -1 };
int dy[] = { 0, 1, -1, 0, 0 };

void func(int fixedCnt) {
    if (fixedCnt == 3) {
        if (sum < ans) ans = sum;
        return;
    }
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
            int sumForThisFlower = 0;
            for (int k = 0; k < 5; k++) {
                int newX = x + dx[k];
                int newY = y + dy[k];
                if (newX < 0 || newY < 0 || newX >= N || newY >= N || used[newX][newY]) {
                    sumForThisFlower = -1;
                    break;
                }
                sumForThisFlower += prices[newX][newY];
            }
            if (sumForThisFlower == -1) continue;
            for (int k = 0; k < 5; k++) {
                int newX = x + dx[k];
                int newY = y + dy[k];
                used[newX][newY] = true;
            }
            sum += sumForThisFlower;
            func(fixedCnt + 1);

            for (int k = 0; k < 5; k++) {
                int newX = x + dx[k];
                int newY = y + dy[k];
                used[newX][newY] = false;
            }
            sum -= sumForThisFlower;
        }
    }
}

int main(void) {
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> prices[i][j];
        }
    }

    func(0);

    cout << ans;
}
