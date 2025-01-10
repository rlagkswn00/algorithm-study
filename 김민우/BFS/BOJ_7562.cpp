#include <bits/stdc++.h>
using namespace std;

int board[305][305];
int dx[8]= {-2, -1, 1, 2, 2, 1, -1, -2};
int dy[8]= {1, 2, 2, 1, -1, -2, -2, -1};

#define X first
#define Y second

int main() {
    int n;
    cin >> n;
    while(n--){
        int l;
        cin >> l;
        for(int i=0; i<l; i++) {
            for(int j=0; j<l; j++){
                board[i][j] = -1;
            }
        }
        queue<pair<int, int>> q;
        int x, y;
        cin >> x >> y;
        q.push({x,y});
        board[x][y] = 0;
        
        while(!q.empty()) {
            auto t = q.front(); q.pop();
            int curX = t.X;
            int curY = t.Y;
            
            for(int i=0; i<8; i++){
                int nxtX = curX + dx[i];
                int nxtY = curY + dy[i];
                
                if(nxtX < 0 || nxtX >= l || nxtY < 0 || nxtY >=l) continue;
                if(board[nxtX][nxtY] >= 0) continue;
                
                board[nxtX][nxtY] = board[curX][curY] + 1;
                q.push({nxtX, nxtY});
            }
        }
        cin >> x >> y;
        cout << board[x][y] << '\n';
    }
    
}