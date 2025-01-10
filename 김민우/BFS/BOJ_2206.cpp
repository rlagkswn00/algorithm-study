#include <bits/stdc++.h>

using namespace std;
#define X first
#define Y second

int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

int ans[1001][1001][2];

int main(){
    
    int n,m;
    cin >> n >> m;
    
    string s[1001];
    
    for(int i=0; i<n; i++) {
        cin >> s[i];
    }

    queue<tuple<int, int, int>> q;
    q.push({0,0,1});
    ans[0][0][1] = 1;
    
    while(!q.empty()){
        auto t = q.front(); q.pop();
        int curX = get<0>(t);
        int curY = get<1>(t);
        int crash = get<2>(t);
        
        if(curX == n-1 && curY == m-1) {
            cout << ans[curX][curY][crash];
            return 0;
        }
        for(int i=0; i<4; i++){
            int nxtX = curX + dx[i];
            int nxtY = curY + dy[i];
            
            if(nxtX < 0 || nxtX >= n || nxtY < 0 || nxtY >=m) continue;
            if(s[nxtX][nxtY] == '1' && crash == 1) {
                q.push({nxtX, nxtY, 0});
                ans[nxtX][nxtY][0] = ans[curX][curY][crash] + 1;
            }
            if(s[nxtX][nxtY] == '0' && ans[nxtX][nxtY][crash] == 0){
                q.push({nxtX, nxtY, crash});
                ans[nxtX][nxtY][crash] = ans[curX][curY][crash] + 1;
            }
        }
    }
    cout << -1;
}