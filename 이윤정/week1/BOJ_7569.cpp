#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
#define endl '\n'
#define MAX 100
int M, N, H; // 가로 세로 높이
// 안익은 0, 익은 1, 안들은 -1
int map[MAX][MAX][MAX];
bool visited[MAX][MAX][MAX];
queue<vector<int>> Q;
vector<vector<int>> d = { {1, 0, 0},{-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {0, 0, 1}, {0, 0, -1}};
int max = 0; // 각 토마토마다 도착할때까지 걸리는 시간의 최댓값 기록

int lookUpMap(vector<int> index) {
    return map[index[0]][index[1]][index[2]];
}
bool isEmpty(vector<int> index) {
    return lookUpMap(index) == -1;
}
bool isRipe(vector<int> index) {
    return lookUpMap(index) == 1;
}

void visit(vector<int> v) {
    for (int i = 0; i < 4; i++) {
        vector<int> nextV;
        for (int j = 0; j < 3; j++) {
            nextV[j] = v[j] + d[i][j];
        }
        if (nextV[0] >= 0 && nextV[0] < M 
            && nextV[1] >= 0 && nextV[1] < N
            && nextV[2] >= 0 && nextV[2] < H
            && map[nextV[0]][nextV[1]][nextV[2]]
            && !visited[nextV[0]][nextV[1]][nextV[2]]) // 이동 가능
        {
            Q.push(nextV);
            map[nextV[0]][nextV[1]][nextV[2]] = map[v[0]][v[1]][v[2]] + 1;
            visited[nextV[0]][nextV[1]][nextV[2]] = true;
        }
    }
}

void print() {
    for (int i = 0; i < H; i++) {
        cout << endl << endl;
        for (int j = 0; j < M; j++) {
            cout << endl;
            for (int k = 0; k < H; k++) {
                cout << map[i][j][k];
            }
        }
    }
}

int32_t main(void)
{
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    for (int i = 0; i < H; i++) {
        for (int j = 0; j < M; j++) {
            for (int k = 0; k < H; k++) {
                cin >> map[i][j][k];
            }
        }
    }

    Q.push(vector<int>{0, 0, 0});
    visited[0][0][0] = true;
    while (!Q.empty()) {
        vector<int> v = Q.front();
        Q.pop();
        visit(v);
        //print();
    }
}
