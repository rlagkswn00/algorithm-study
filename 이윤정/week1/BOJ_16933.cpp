#include <iostream>
#include <queue>
#include <vector>
using namespace std;
#define endl '\n';

typedef vector<vector<int>> Map;
struct Data {
    int broken;
    int x;
    int y;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(0);

    int N, M, K;
    cin >> N >> M >> K;
    Map map(N + 1, vector<int>(M + 1));
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            char c;
            cin >> c;
            map[i][j] = c - '0';
        }
    }

    //int K = 1; // 부술 수 있는 최대 수
    //index == 해당 경로에 포함된 부순 벽 수
    vector<Map> distMaps(K + 1, Map(N + 1, vector<int>(M + 1, -1)));

    // 부수기 수 제한 때문에 다익스트라처럼 그리디하게 경로 확정 불가
    // 완전탐색 해가면서 찾아야 함 -> dfs로 해도 같은 결과 나오나?
    // 큐에 거리정보 저장해 둘 필요 x 의미 없음!
    // but 큐에 몇 번 부순 경로인 지는 같이 기록해야 함
    queue<Data> q;
    q.push({ 0, 1, 1 });
    distMaps[0][1][1] = 1;
    while (!q.empty()) {
        int broken = q.front().broken;
        int x = q.front().x;
        int y = q.front().y;
        q.pop();
        const int dx[] = { 0, 0, 1, -1 };
        const int dy[] = { 1, -1, 0, 0 };
        for (int i = 0; i < 4; i++) {
            int nextX = x + dx[i];
            int nextY = y + dy[i];
            if (nextX < 1 || nextX > N || nextY < 1 || nextY > M) continue;
            if (map[nextX][nextY] == 1) {
                if (broken + 1 > K) continue;
                int oldDist = distMaps[broken + 1][nextX][nextY];
                int newDist = distMaps[broken][x][y] + 1;
                if (distMaps[broken][x][y] % 2 == 0) { // 밤
                    newDist++;
                }
                if (oldDist != -1 && oldDist <= newDist) continue;
                distMaps[broken + 1][nextX][nextY] = newDist;
                q.push({ broken + 1, nextX, nextY });
            }
            else {
                int oldDist = distMaps[broken][nextX][nextY];
                int newDist = distMaps[broken][x][y] + 1;
                if (oldDist != -1 && oldDist <= newDist) continue;
                distMaps[broken][nextX][nextY] = newDist;
                q.push({ broken, nextX, nextY });
            }
        }
    }

    int ans = -1;
    for (Map& distMap : distMaps) {
        if (distMap[N][M] == -1) continue;
        if (ans == -1 || distMap[N][M] < ans)
            ans = distMap[N][M];
    }
    cout << ans;
}
