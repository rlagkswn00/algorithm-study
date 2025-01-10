#include <bits/stdc++.h>

using namespace std;

int arr[1005][3];
int color[1005][3];

int main() {
    int n;
    cin >> n;
    
    for(int i=1; i<=n; i++){
        cin >> color[i][0];
        cin >> color[i][1];
        cin >> color[i][2];
    }
    
    arr[1][0] = color[1][0];
    arr[1][1] = color[1][1];
    arr[1][2] = color[1][2];
    
    for(int i=2; i<=n; i++) {
        arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + color[i][0];
        arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + color[i][1];
        arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + color[i][2];
    }
    
    cout << min({arr[n][0], arr[n][1], arr[n][2]});
}