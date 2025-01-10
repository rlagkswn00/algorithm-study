#include <bits/stdc++.h>

using namespace std;

int n,m,st;
vector<int> adj[1005];
bool vis[1005];

void dfs(int cur) {
    vis[cur] = true;
    cout << cur << ' ';
    for(auto nxt: adj[cur]){
        if(vis[nxt]) continue;
        dfs(nxt);
    }
}

void bfs(){
    queue<int> q;
    q.push(st);
    vis[st] = true;
    cout << st << ' ';
    while(!q.empty()){
        auto cur = q.front(); q.pop();
        
        for(auto nxt: adj[cur]){
            if(vis[nxt]) continue;
            vis[nxt] = true;
            cout << nxt << ' ';
            q.push(nxt);
        }
    }
}

int main(){
    cin >> n >> m >> st;
    while(m--) {
        int v, u;
        cin >> v >> u;
        adj[v].push_back(u);
        adj[u].push_back(v);
    }
    for(int i=1; i<=n; i++) {
        sort(adj[i].begin(), adj[i].end());
    }
    
    dfs(st);
    fill(vis+1, vis+n+1, false);
    cout << '\n';
    bfs();
}
