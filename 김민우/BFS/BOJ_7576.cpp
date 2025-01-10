#include <bits/stdc++.h>

using namespace std;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

#define X first
#define Y second

int m,n;
int board[1005][1005] = {0};
bool vis[1005][1005] = {0};

int main() {
    cin >> m >> n;
    queue<pair<int, int>> Q;
    
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            cin >> board[i][j];
            if(board[i][j] == 1) {
                Q.push({i,j});
                vis[i][j] = 1;
            }
        }
    }
    
    while(!Q.empty()) {
        pair<int, int> t = Q.front(); Q.pop();
        int curX = t.X;
        int curY = t.Y; 
        for(int i=0; i<4; i++) {
            int nxtX = curX + dx[i];
            int nxtY = curY + dy[i];
            
            if(nxtX < 0 || nxtX >=n || nxtY < 0 || nxtY >=m) continue;
            if(vis[nxtX][nxtY] >= 1 || board[nxtX][nxtY] == -1) continue;
            board[nxtX][nxtY] = board[curX][curY] + 1;
            vis[nxtX][nxtY] = 1;
            Q.push({nxtX, nxtY});
        }
    }
    int maxt = -100;
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            
            if(board[i][j] == 0) {
                cout << -1;
                return 0;
            }
            if(maxt <= board[i][j]) maxt = board[i][j];
        }
    }
    cout << maxt-1;
}