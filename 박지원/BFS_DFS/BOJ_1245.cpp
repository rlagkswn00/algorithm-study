#include<iostream>
#include<algorithm>
#include<vector>
#include <set>
using namespace std;

int N,M;
int arr[101][101]={0};
int visited[101][101]={0};
int x[8]={0,0,-1,1,-1,-1,1,1};
int y[8]={-1,1,0,0,-1,1,-1,1};
vector<tuple<int,int,int>>vec;

void dfs(int row,int col) {
    if(visited[row][col]!=0)
        return;
    visited[row][col]=1;
    for(int i=0;i<8;i++) {
        int new_row=row+x[i];
        int new_col=col+y[i];
        if(new_row<=0||new_row>N) {
            continue;
        }
        if(new_col<=0||new_col>M) {
            continue;
        }
        if(arr[new_row][new_col]>arr[row][col]) {
            continue;
        }
        dfs(new_row,new_col);
    }
}
int count1=0;
void cal(int row,int col) {


    if(visited[row][col]==0) {
        count1++;
        dfs(row,col);
    }

}
bool compare(tuple<int,int,int>a,tuple<int,int,int>b) {
    return get<0>(a)>get<0>(b);
}
int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    cin>>N>>M;
    for(int i=1;i<=N;i++) {
        for(int j=1;j<=M;j++) {
            cin>>arr[i][j];
            vec.push_back(make_tuple(arr[i][j],i,j));
        }
    }
    sort(vec.begin(),vec.end(),compare);
    for(int i=0;i<vec.size();i++) {
        tuple<int,int,int>t=vec[i];
        //cout<<get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<"\n ";
        cal(get<1>(t),get<2>(t));
    }
    cout<<count1;
    return 0;

}
