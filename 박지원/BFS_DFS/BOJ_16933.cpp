#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <sstream>

using namespace std;

int N, M, K;
int arr[1001][1001];
int visited[1001][1001][11] = {0};
int x[4] = {0, 0, -1, 1};
int y[4] = {-1, 1, 0, 0};


int bfs() {
    queue<tuple<int, int, int, int, bool>> que;
    que.push(make_tuple(1, 1, 1, 0, true));
    int result = -1;
    while (!que.empty()) {
        tuple<int, int, int, int, bool> tuple1 = que.front();
        int row = get<0>(tuple1);
        int col = get<1>(tuple1);
        int day = get<2>(tuple1);
        int indent = get<3>(tuple1);
        bool sun = get<4>(tuple1);
        que.pop();


        if (row == N && col == M) {
            return day;
        }

        for (int i = 0; i < 4; i++) {
            int new_row = row + x[i];
            int new_col = col + y[i];
            if (new_row <= 0 || new_row > N)
                continue;
            if (new_col <= 0 || new_col > M)
                continue;
            if (visited[new_row][new_col][indent + arr[new_row][new_col]] != 0)
                continue;

            if (arr[new_row][new_col] == 1) {
                if (indent == K)
                    continue;
                if (sun) {
                    visited[new_row][new_col][indent + arr[new_row][new_col]] = 1;
                    que.push(make_tuple(new_row, new_col, day + 1, indent + arr[new_row][new_col], !sun));

                }
                else {

                    que.push(make_tuple(row, col, day + 1, indent, !sun));

                }
            }
            else {
                visited[new_row][new_col][indent + arr[new_row][new_col]] = 1;
                que.push(make_tuple(new_row, new_col, day + 1, indent + arr[new_row][new_col], !sun));
            }


        }

    }
    return result;
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    cin >> N >> M >> K;
    for (int i = 1; i <= N; i++) {
        string str;
        cin >> str;
        for (int j = 1; j <= M; j++) {
            arr[i][j] = str[j - 1] - '0';
        }
    }
    cout << bfs();


    return 0;
}

