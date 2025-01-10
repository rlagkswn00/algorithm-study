#include <bits/stdc++.h>

using namespace std;

int arr[505][505];
int ans[505][505];

int main(){
    int n;
    cin >> n;
    
    for(int i=0; i<n; i++){
        for(int j=0; j<=i; j++){
            cin >> arr[i][j];
        }
    }
    ans[0][0] = arr[0][0];
    
    for(int i=0; i<n; i++){
        for(int j=0; j<=i; j++){
            ans[i+1][j] = max(ans[i+1][j], ans[i][j] + arr[i+1][j]);
            ans[i+1][j+1] = max(ans[i+1][j+1], ans[i][j] + arr[i+1][j+1]);
        }
    }
    int maxt = -1;
    for(int i=0; i<n; i++){
         maxt = max(maxt, ans[n-1][i]);
    }
    cout << maxt;
}