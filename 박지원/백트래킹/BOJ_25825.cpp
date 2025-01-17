#include <bits/stdc++.h>
using namespace std;

int arr[13][13];
vector<int>vec1;
int mini=1000000000;
void cal3(vector<int>vec){
    int sum=0;
    for(int i=1;i<vec.size();i++){
        sum=sum+arr[vec[i-1]][vec[i]];
    }
    mini=min(mini,sum);
}
void cal2(int index,vector<int>path_vec){
    if(index==6){
        cal3(path_vec);
        return;
    }
    
    int temp=vec1[index];
    vector<int>path_vec1;
    for(int i=0;i<path_vec.size();i++){
        path_vec1.push_back(path_vec[i]);
    }
    path_vec1.push_back(temp*2-1);
    path_vec1.push_back(temp*2);
    cal2(index+1,path_vec1);

    vector<int>path_vec2;
    for(int i=0;i<path_vec.size();i++){
        path_vec2.push_back(path_vec[i]);
    }
    path_vec2.push_back(temp*2);
    path_vec2.push_back(temp*2-1);
    cal2(index+1,path_vec2);
    
}
void cal(vector<int>vec,int visited[7]){
    if(vec.size()==6){
        vec1=vec;
        vector<int>path_vec;
        cal2(0,path_vec);
        return;
    }
    for(int i=1;i<=6;i++){
        if(visited[i]!=0)
            continue;
        vector<int>new_vector;
        for(int j=0;j<vec.size();j++){
            new_vector.push_back(vec[j]);
        }
        new_vector.push_back(i);

        int new_visited[7]={0};
        for(int j=1;j<=6;j++){
            new_visited[j]=visited[j];
        }
        new_visited[i]=1;
        cal(new_vector,new_visited);
    }
}
int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    for(int i=1;i<=12;i++){
        for(int j=1;j<=12;j++){
            cin>>arr[i][j];
        }
    }
    vector <int>vec;
    int arr[7]={0};
    cal(vec,arr);
    //720*64=40000
    cout<<mini;

    return 0;
}