#include <bits/stdc++.h>

using namespace std;
vector<pair<int, int>> pre_vec;
int arr[11][11];
int N, M, H;
int start_row, start_col;
int maxi=0;
void cal(int arr[10],int arr_size, int row, int col, int hp)
{
    int temp1=abs(start_row - row) + abs(start_col - col);
    if(temp1<=hp){
        maxi=max(maxi,arr_size);
    }
    if(arr_size==pre_vec.size()){
        return;
    }
    //cout<<row<<" "<<col<<" "<<arr_size<<" "<<hp<<endl;
    for (int i = 0; i < pre_vec.size(); i++)
    {
        if (arr[i] != 0)
            continue;
        pair<int, int> pair1 = pre_vec[i];
        int new_row = pair1.first;
        int new_col = pair1.second;
        int temp = abs(new_row - row) + abs(new_col - col);
        if(temp>hp)
            continue;
        int new_arr[10]={0};
        for(int j=0;j<10;j++){
            new_arr[j]=arr[j];
        }
        new_arr[i]=1;
        cal(new_arr,arr_size+1,new_row,new_col,hp-temp+H);
    }
}
int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    cin >> N >> M >> H;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 1)
            {
                start_row = i;
                start_col = j;
            }
            if (arr[i][j] == 2)
            {
                pre_vec.push_back({i, j});
            }
        }
    }
    int arr[10] = {0};
    cal(arr,0, start_row, start_col, M);
    cout<<maxi;
    // 3628800
}