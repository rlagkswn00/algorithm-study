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

int T;
int visited[301][301] = {0};
int N;
pair<int, int> head;
pair<int, int> tail;
queue<int>que1;
queue<int>que2;
queue<int>que3;
int x[8]={-1,-2,-2,-1,1,2,2,1};
int y[8]={-2,-1,1,2,-2,-1,1,2};
void reset(){
    for(int i=0;i<=300;i++){
        for(int j=0;j<=300;j++){
            visited[i][j]=0;
        }
    }
}
int cal(){
    que1.push(head.first);
    que2.push(head.second);
    que3.push(0);
    bool end=false;
    int result=0;
    while(!que1.empty()){
        int row=que1.front();
        que1.pop();
        int col=que2.front();
        que2.pop();
        int day=que3.front();
        que3.pop();
        if(visited[row][col]!=0||end)
            continue;
        visited[row][col]=1;
        if(row==tail.first&&col==tail.second){
            end=true;
            result=day;
            continue;
        }
        for(int i=0;i<8;i++){
            int new_row=row+x[i];
            int new_col=col+y[i];
            if(new_row<0||new_row>=N)
                continue;
            if(new_col<0||new_col>=N)
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
    cin >> T;
    int temp1,temp2;
    while (T--) {
        reset();
        cin >> N;
        cin>>temp1>>temp2;
        head={temp1,temp2};
        cin>>temp1>>temp2;
        tail={temp1,temp2};
        cout<<cal()<<"\n";
    }

    return 0;
}

