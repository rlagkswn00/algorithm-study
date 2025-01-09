#include<iostream>
#include<algorithm>
#include<vector>
#include <set>
using namespace std;

int N,M,K;
int arr[101][101]={0};
int visited[101][101]={0};
int x[8]={0,0,-1,1};
int y[8]={-1,1,0,0};
vector<int>vec;

void mark_node(int row1,int col1,int row2,int col2) {
    for(int i=row1;i<row2;i++) {
        for(int j=col1;j<col2;j++) {
            arr[i][j]=1;
        }
    }
}
int count1=0;
void dfs(int row,int col) {
    if(visited[row][col]!=0)
        return;
    visited[row][col]=1;
    count1++;
    for(int i=0;i<4;i++) {
        int new_row=row+x[i];
        int new_col=col+y[i];
        if(new_row<0||new_row>=N)
            continue;
        if(new_col<0||new_col>=M)
            continue;
        if(arr[new_row][new_col]!=0)
            continue;
        dfs(new_row,new_col);
    }
}
void cal(int row,int col) {
    count1=0;
    if(visited[row][col]!=0)
        return;
    if(arr[row][col]!=0)
        return;
    dfs(row,col);
    vec.push_back(count1);
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    cin>>M>>N>>K;
    for(int i=1;i<=K;i++) {
        int row1,row2,col1,col2;
        cin>>row1>>col1>>row2>>col2;
        mark_node(row1,col1,row2,col2);
    }

    for(int i=0;i<N;i++) {
        for(int j=0;j<M;j++) {

            cal(i,j);
        }
    }
    cout<<vec.size()<<"\n";
    sort(vec.begin(),vec.end());
    for(int i=0;i<vec.size();i++) {
        cout<<vec[i]<<" ";
    }

    return 0;

}
