#include<iostream>
#include<algorithm>
#include<vector>
#include <set>
using namespace std;

int N;
int arr[11][11];
int mini=100000000;
int x[5]={0,0,-1,1,0};
int y[5]={-1,1,0,0,0};
void print(vector<pair<int,int>>vec){
    cout<<"#######################\n";
    for(int i=0;i<vec.size();i++){
        cout<<vec[i].first<<" "<<vec[i].second<<endl;
    }
    cout<<endl;
}
bool cal3(pair<int,int>pair1,pair<int,int>pair2){
    if(abs(pair1.first-pair2.first)<=1&&abs(pair1.second-pair2.second)<=1){
        return false;
    }
    if(abs(pair1.first-pair2.first)<=2&&abs(pair1.second-pair2.second)==0){
        return false;
    }

    if(abs(pair1.first-pair2.first)==0&&abs(pair1.second-pair2.second)<=2){
        return false;
    }
    return true;
}
void cal2(vector<pair<int,int>>vec) {

    int sum=0;
    bool istrue=true;
    //print(vec);
    for(int i=0;i<vec.size();i++){
        for(int j=i+1;j<vec.size();j++){
            if(!cal3(vec[i],vec[j]))
                istrue=false;
        }
    }
    if(!istrue)
        return;

    for(int i=0;i<vec.size();i++){
        for(int j=0;j<5;j++){
            sum=sum+arr[vec[i].first+x[j]][vec[i].second+y[j]];
        }

    }

    mini=min(mini,sum);
}


void cal(vector<pair<int,int>>vec){

    if(vec.size()==3){
        //print(vec);
        //return;
        cal2(vec);
        return;
    }
    for(int i=1+1;i<=N-1;i++){
        for(int j=1+1;j<=N-1;j++) {
            vector<pair<int,int>>new_vec;
            for(int k=0;k<vec.size();k++){
                new_vec.push_back(vec[k]);
            }
            new_vec.push_back({i,j});
            cal(new_vec);

        }
    }
}
int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    cin>>N;
    for(int i=1;i<=N;i++){
        for(int j=1;j<=N;j++){
            cin>>arr[i][j];
        }
    }
    for(int i=1+1;i<=N-1;i++){
        for(int j=1+1;j<=N-1;j++){
            vector<pair<int,int>>vec;
            vec.push_back({i,j});
            cal(vec);
        }
    }
    cout<<mini;
//100000000
    return 0;
}
