#include<iostream>
#include<algorithm>
#include<vector>
#include <set>
using namespace std;

int N,M;
int arr[51][51]={0};
int visited[51][51]={0};
int finish[51][51]={0};
int x[4]={0,0,-1,1};
int y[4]={-1,1,0,0};
int maxi=1;
bool is_loop=false;

int dfs(int row,int col,int num) {

    if(row<=0||row>N)
        return 1;
    if(col<=0||col>M)
        return 1;
    if(arr[row][col]==-1)
        return 1;
    if(visited[row][col]!=0) {
        if(finish[row][col]==0) {
            is_loop=true;
        }
        return visited[row][col];
    }


    visited[row][col]=1;
    int node=0;
    for(int i=0;i<4;i++) {
        int new_row=row+(x[i]*arr[row][col]);
        int new_col=col+(y[i]*arr[row][col]);

        node=max(node,dfs(new_row,new_col,num+1));
    }
    finish[row][col]=1;
    visited[row][col]=node+1;
    return visited[row][col];
}

int cal() {
    int num=dfs(1,1,0);
    if(is_loop)
        return -1;
    return num;

}
int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    cin>>N>>M;
    for(int i=1;i<=N;i++) {
        string str;
        cin>>str;
        for(int j=1;j<=M;j++) {
            char chr=str[j-1];

            if(chr=='H') {
                arr[i][j]=-1;
            }
            else {
                arr[i][j]=chr-'0';
            }
        }
    }
    int result=cal();
    if(result==-1) {
        cout<<-1;
        return 0;
    }
    cout<<result-1;



    return 0;

}
