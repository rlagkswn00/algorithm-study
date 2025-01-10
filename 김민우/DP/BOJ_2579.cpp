#include <bits/stdc++.h>

using namespace std;

int arr[305][2];
int value[305];

int main() {
    int n; 
    cin >> n;
    for(int i=1; i<=n; i++) {
        cin >> value[i];
    }
    
    arr[1][1] = value[1];
    arr[1][2] = 0;
    
    arr[2][1] = value[1] + value[2];
    arr[2][2] = value[2];
    
    for(int i=3; i<=n; i++) {
        arr[i][1] = arr[i-1][2] + value[i];
        arr[i][2] = max(arr[i-2][1], arr[i-2][2]) + value[i];
    }
    
    cout << max(arr[n][1], arr[n][2]);
    
}