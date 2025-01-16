#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
#define endl '\n'
#define MAX 1000

int N, M;
int box[MAX][MAX]; //익은 토마토 1, 안 익은 0, 비어 있는 -1
queue<vector<int>> Q; //x, y, day 저장
int unripe_tomato_cnt = 0;
int day_passed = 0;

void ripen(vector<int> tomato) {
    int x = tomato[0];
    int y = tomato[1];
    int day = tomato[2];

    int directions[4][2] = { {1, 0}, {0, 1}, {-1, 0},{0, -1} };
    for (int* direction : directions) {
        int nextX = x + direction[0];
        int nextY = y + direction[1];

        int today = tomato[2] + 1;

        if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= M || box[nextX][nextY] == -1) {
            continue;
        }
        if (box[nextX][nextY] == 0) {
            box[nextX][nextY] = 1;
            unripe_tomato_cnt--;
            Q.push(vector<int> {nextX, nextY, today});
            day_passed = today > day_passed ? today : day_passed; // 토마토 익혔을 때만 시간 흐름 (안익혔으면 그 날 필요 없음)
        }
    }
}

int32_t main(void)
{
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> box[i][j];
            if (box[i][j] == 1) {
                Q.push(vector<int> {i, j, 0});
                continue;
            }
            if (box[i][j] == 0) {
                unripe_tomato_cnt++;
            }
        }
    }


    while (!Q.empty()) {
        vector<int> tomato = Q.front();
        Q.pop();
        ripen(tomato);
    }

    if (unripe_tomato_cnt) {
        cout << -1;
    }
    else {
        cout << day_passed;
    }
}
