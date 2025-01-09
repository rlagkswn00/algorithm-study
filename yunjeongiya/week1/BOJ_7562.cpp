#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
#define endl '\n'
#define MAX 300
int N, I;
int startX, startY, targetX, targetY;
int map[MAX][MAX];
bool visited[MAX][MAX];
queue<pair<int, int>> Q;
vector<pair<int, int>> d = 
{ {-2, 1}, {-1, 2}, {1, 2}, {2, 1},
    {-2, -1}, {-1, -2}, {1, -2}, {2, -1} };

void visit(pair<int, int> v) {
    for (int i = 0; i < 8; i++) {
        int a = v.first + d[i].first;
        int b = v.second + d[i].second;
        if (a >= 0 && a < I 
            && b >= 0 && b < I
            && !visited[a][b])
        {
            Q.push(pair<int, int>(a, b));
            map[a][b] = map[v.first][v.second] + 1;
            visited[a][b] = true;
        }
    }
}

void print() {
    cout << "------------------------" << endl;
    for (int i = 0; i < I; i++) {
        cout << endl;
        for (int j = 0; j < I; j++) {
            cout << map[i][j];
        }
    }
    cout << "------------------------" << endl;
}

void init() {
    for (int i = 0; i < I; i++) {
        for (int j = 0; j < I; j++) {
            map[i][j] = 0;
            visited[i][j] = false;
        }
    }
    Q = queue<pair<int, int>>();
}

int32_t main(void)
{
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> I;
        cin >> startX >> startY;
        cin >> targetX >> targetY;
        init();
        Q.push(pair<int, int>(startX, startY));
        visited[startX][startY] = true;
        pair<int, int> v = Q.front();
        while (v.first != targetX || v.second != targetY) {
            v = Q.front();
            Q.pop();
            visit(v);
            //print();
        }
        cout << map[targetX][targetY] << endl;
    }
}
