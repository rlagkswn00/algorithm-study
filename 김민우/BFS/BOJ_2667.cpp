#include <bits/stdc++.h>

using namespace std;

#define X first
#define Y second

int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

int vis[30][30];

int main() {
    int n;
    cin >> n;
    string S[30];
    for(int i=0; i<n; i++) {
        cin >> S[i];
    }
    
    queue<pair<int,int>> q;
    
    vector<int> v;
    for(int i=0; i<n; i++) {
        for (int j=0; j<n; j++){
            
            if (S[i][j] == '1' && vis[i][j] == false) {
                q.push({i,j});
                int tmp = 1;
                vis[i][j] = true;
                
                while(!q.empty()) {
                    auto t = q.front(); q.pop();
                    int x = t.X;
                    int y = t.Y;
                    
                    for(int i=0; i<4; i++){
                        int nxtX = x + dx[i];
                        int nxtY = y + dy[i];
                    
                        if (nxtX < 0 || nxtX >= n || nxtY < 0 || nxtY >= n) continue;
                        if (vis[nxtX][nxtY] || S[nxtX][nxtY] == '0') continue;
                        vis[nxtX][nxtY] = true;
                        tmp++;
                        q.push({nxtX, nxtY});
                    }
                }
                v.push_back(tmp);
                
            }
        }
    }
    
    sort(v.begin(), v.end());
    cout << v.size() << '\n';
    for(int i=0; i<v.size(); i++) {
        cout << v[i] << '\n';
    }
    
}