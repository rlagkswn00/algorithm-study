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

int N,M;
int arr[1002][1002]={0};
int visited[1002][1002]={0};
int x[4]={0,0,-1,1};
int y[4]={-1,1,0,0};
int total=0;
queue<int>que1;
queue<int>que2;
queue<int>que3;

int bfs(){
    int result=0;
    while(!que1.empty()){
        int row=que1.front();
        que1.pop();
        int col=que2.front();
        que2.pop();
        int day=que3.front();
        que3.pop();

        if(visited[row][col]!=0)
            continue;
        visited[row][col]=1;
        arr[row][col]=1;
        result=max(result,day);
        for(int i=0;i<4;i++){
            int new_row=row+x[i];
            int new_col=col+y[i];
            if(arr[new_row][new_col]==-1)
                continue;
            if(new_row==0||new_row==N+1)
                continue;
            if(new_col==0||new_col==M+1)
                continue;
            que1.push(new_row);
            que2.push(new_col);
            que3.push(day+1);
        }
    }


    return result;
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    cin>>M>>N;
    for(int i=1;i<=N;i++){
        for(int j=1;j<=M;j++){
            cin>>arr[i][j];
            if(arr[i][j]==1){
                que1.push(i);
                que2.push(j);
                que3.push(0);
            }

        }
    }


    int result=bfs();
    bool stop=false;
    for(int i=1;i<=N;i++) {
        for (int j = 1; j <= M; j++) {
            if(arr[i][j]==0)
                stop=true;
        }
    }
    if(stop){
        cout<<-1;
        return 0;
    }
    cout<<result;
    return 0;
}

